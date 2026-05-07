# -*- coding: utf-8 -*-
"""
Inventario de imagenes del gestor de conocimiento.

Genera un Excel que lista:
- Todos los archivos dentro de imagenes/
- Formato actual (extension)
- Ruta y nombre
- Si tiene espacios o mayusculas en el nombre (problematicos para web)
- Si esta referenciado en algun script Python (y cuales)
- Si es huerfano (existe pero nadie lo usa) o roto (referenciado pero no existe)

Util para decidir que renombrar, que convertir de formato y que borrar.
"""

import os
import re
from pathlib import Path
from urllib.parse import unquote

import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
CARPETA_IMAGENES = RAIZ / "imagenes"
CARPETA_SCRIPTS = RAIZ / "scripts"
SALIDA = CARPETA_IMAGENES / "inventario_imagenes.xlsx"

EXTENSIONES = {".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif", ".pdf", ".xlsx"}


def listar_archivos():
    """Recorre imagenes/ y devuelve lista de dicts con info de cada archivo."""
    filas = []
    for ruta in sorted(CARPETA_IMAGENES.rglob("*")):
        if not ruta.is_file():
            continue
        if ruta.suffix.lower() not in EXTENSIONES:
            continue
        rel = ruta.relative_to(RAIZ).as_posix()  # ej: imagenes/alertas.jpeg
        nombre = ruta.name
        filas.append({
            "archivo": nombre,
            "ruta_relativa": rel,
            "subcarpeta": ruta.parent.relative_to(CARPETA_IMAGENES).as_posix() or "(raiz)",
            "formato": ruta.suffix.lower().lstrip("."),
            "tiene_espacios": " " in nombre,
            "tiene_mayusculas": any(c.isupper() for c in nombre),
            "tamano_kb": round(ruta.stat().st_size / 1024, 1),
        })
    return filas


def encontrar_referencias():
    """Busca referencias a 'imagenes/...' en los scripts Python.

    Solo considera cadenas entre comillas, para poder capturar rutas con
    espacios (ej: 'imagenes/Header - gestor.jpeg'). Ignora el propio
    script de inventario y su cache.

    Devuelve dict: ruta_relativa_normalizada -> lista de 'script:linea'.
    """
    referencias = {}
    # Captura el contenido entre comillas que inicia con (../)?imagenes/
    patron = re.compile(r"""["']((?:\.\./)?imagenes/[^"']+)["']""", re.IGNORECASE)

    for ruta_script in CARPETA_SCRIPTS.rglob("*.py"):
        # No escanear el propio script de inventario
        if ruta_script.name == "inventario_imagenes.py":
            continue
        with open(ruta_script, encoding="utf-8") as f:
            for num_linea, linea in enumerate(f, start=1):
                for match in patron.findall(linea):
                    # Limpia prefijo ../ y decodifica %20 a espacio
                    ref = match
                    if ref.startswith("../"):
                        ref = ref[3:]
                    ref = unquote(ref)
                    referencias.setdefault(ref, []).append(
                        f"{ruta_script.name}:{num_linea}"
                    )
    return referencias


def construir_inventario():
    archivos = listar_archivos()
    referencias = encontrar_referencias()

    # Marca cada archivo como usado o huerfano
    rutas_en_disco = {fila["ruta_relativa"] for fila in archivos}

    for fila in archivos:
        refs = referencias.get(fila["ruta_relativa"], [])
        fila["referenciado"] = "Si" if refs else "No (huerfano)"
        fila["scripts_que_lo_usan"] = "; ".join(refs) if refs else ""

    # Encuentra referencias rotas: algo que el codigo pide pero no existe
    rotas = []
    for ref, ubicaciones in referencias.items():
        if ref not in rutas_en_disco:
            rotas.append({
                "archivo": ref.split("/")[-1],
                "ruta_relativa": ref,
                "subcarpeta": "/".join(ref.split("/")[:-1]),
                "formato": ref.split(".")[-1].lower() if "." in ref else "",
                "tiene_espacios": " " in ref,
                "tiene_mayusculas": any(c.isupper() for c in ref.split("/")[-1]),
                "tamano_kb": None,
                "referenciado": "ROTO - referencia sin archivo",
                "scripts_que_lo_usan": "; ".join(ubicaciones),
            })

    df = pd.DataFrame(archivos + rotas)
    # Ordena: rotas arriba, luego huerfanos, luego usados
    df["_orden"] = df["referenciado"].map({
        "ROTO - referencia sin archivo": 0,
        "No (huerfano)": 1,
        "Si": 2,
    })
    df = df.sort_values(["_orden", "ruta_relativa"]).drop(columns="_orden").reset_index(drop=True)
    return df


def guardar_excel(df):
    with pd.ExcelWriter(SALIDA, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="inventario")
        # Ajusta ancho de columnas
        ws = writer.sheets["inventario"]
        anchos = {
            "A": 35, "B": 55, "C": 20, "D": 10, "E": 16,
            "F": 18, "G": 10, "H": 30, "I": 60,
        }
        for col, ancho in anchos.items():
            ws.column_dimensions[col].width = ancho


if __name__ == "__main__":
    df = construir_inventario()
    guardar_excel(df)

    # Resumen por consola
    total = len(df)
    rotas = (df["referenciado"] == "ROTO - referencia sin archivo").sum()
    huerfanos = (df["referenciado"] == "No (huerfano)").sum()
    usadas = (df["referenciado"] == "Si").sum()
    print(f"Inventario generado: {SALIDA}")
    print(f"Total filas: {total}")
    print(f"  - Referencias rotas (codigo pide, archivo no existe): {rotas}")
    print(f"  - Archivos huerfanos (existen, nadie los usa): {huerfanos}")
    print(f"  - Archivos usados: {usadas}")
    print(f"\nFormatos actuales:")
    print(df[df["referenciado"] == "Si"]["formato"].value_counts().to_string())
