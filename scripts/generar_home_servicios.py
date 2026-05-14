# Genera el home (index.html) y las páginas placeholder de cada servicio
# de la Subdirección para la Juventud.
# Todos comparten el mismo CSS base y estructura de navegación.

import os
import sys
import pandas as pd
import folium

# CSS compartido con los demás generadores
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _comun.estilos import css_para

# Raíz del proyecto (un nivel arriba de scripts/)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(BASE, "datos")

# --- Iframe de Power BI (mismo para todos los servicios) ---
POWERBI_SRC = "https://app.powerbi.com/view?r=eyJrIjoiMzRiNWRkMDQtNThmNC00Yzk5LThjNTItOWI4MzZkYzYwM2EzIiwidCI6ImIzZTMwODA4LWU5YTgtNGYyYS05YmMxLWE3NjBhZTkxMGNmNSIsImMiOjR9"

# =====================================================================
# CSS compartido (mismo estilo que Casas de Juventud)
# =====================================================================
CSS_BASE = css_para("home")

# =====================================================================
# JavaScript compartido (navegación sidebar)
# =====================================================================
JS_BASE = """
function toggleSection(el) {
    el.classList.toggle('active');
    var items = el.nextElementSibling;
    if (items) items.classList.toggle('show');
}
function showContent(id) {
    document.querySelectorAll('.content-section').forEach(function(s) { s.classList.remove('active'); });
    document.querySelectorAll('.sidebar-item').forEach(function(s) { s.classList.remove('active'); });
    var el = document.getElementById(id);
    if (el) el.classList.add('active');
    if (event && event.target && event.target.classList.contains('sidebar-item')) {
        event.target.classList.add('active');
    }
}
"""

# =====================================================================
# Función auxiliar: genera HTML completo de un servicio
# =====================================================================
# Colores por servicio: (accent, accent-bg, accent-border)
COLORES_SERVICIO = {
    "jco":     ("#8e6bbf", "#f3eef9", "#e5ddf0"),      # morado atenuado
    "forjar":  ("#5f9ea0", "#edf6f6", "#d4eaeb"),      # teal (azul-verde Forjar)
    "alertas": ("#e67e22", "#fdf2e9", "#f5d9b5"),      # naranja (Parche seguro)
}

def generar_pagina_servicio(titulo, subtitulo, sidebar_html, contenido_html, archivo, logo_img="", color_key=""):
    """Genera un HTML con la estructura estándar del gestor."""
    # Override de color si se especifica
    css_override = ""
    if color_key in COLORES_SERVICIO:
        ac, bg, bd = COLORES_SERVICIO[color_key]
        css_override = f":root {{ --accent: {ac}; --accent-bg: {bg}; --accent-border: {bd}; }}"

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestor de conocimiento - {titulo}</title>
    <style>{CSS_BASE}
    {css_override}</style>
</head>
<body>
    <header class="header">
        <div>
            <h1>Gestor de conocimiento - {titulo}</h1>
            <div class="subtitle">{subtitulo}</div>
        </div>
        <div class="header-btns">
            <a class="home-btn" href="index.html" title="Todos los servicios">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8F4E1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
            </a>
            <div class="home-btn" onclick="showContent('welcome')" title="Inicio {titulo}">
                <img src="{logo_img}" alt="{titulo}" style="height:32px; border-radius:16px; object-fit:contain; vertical-align:middle;">
            </div>
        </div>
    </header>
    <div class="container">
        <nav class="sidebar">
{sidebar_html}
            <div class="sidebar-section">
                <div class="sidebar-title" onclick="showContent('estadisticas')" style="cursor:pointer;">
                    <span>Estad&iacute;sticas</span>
                </div>
            </div>
        </nav>
        <main class="main-content">
{contenido_html}

            <div class="content-section" id="estadisticas">
                <div class="card">
                    <h2 class="card-title">Estad&iacute;sticas</h2>
                    <iframe title="Seguimiento t&eacute;cnico" width="100%" height="600" src="{POWERBI_SRC}" frameborder="0" allowFullScreen="true" style="border:1px solid #e0e0e0; border-radius:8px;"></iframe>
                </div>
            </div>
        </main>
    </div>
    <script>{JS_BASE}</script>
</body>
</html>"""
    ruta = os.path.join(BASE, archivo)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Generado: {archivo} ({len(html):,} caracteres)".replace(",", "."))


# =====================================================================
# INDEX.HTML — Home de todos los servicios
# =====================================================================
def generar_index():
    # Cada servicio tiene:
    #   alt     → texto alternativo del logo (para accesibilidad)
    #   archivo → HTML destino del gestor
    #   imagen  → logo del servicio
    #   desc    → descripcion que aparece sobre el logo
    servicios = [
        {
            "alt": "Casas de Juventud",
            "archivo": "gestion_conocimiento_juventud_2025.html",
            "imagen": "imagenes/servicios/casas-de-juventud.png",
            "desc": "Espacios distritales para j&oacute;venes entre 14 y 28 a&ntilde;os. Oferta integral a trav&eacute;s de 5 ejes: bienestar, cultura, inclusi&oacute;n, liderazgo y SIDICU.",
        },
        {
            "alt": "J&oacute;venes con oportunidades",
            "archivo": "gestion_conocimiento_jco_2025.html",
            "imagen": "imagenes/servicios/jovenes-con-oportunidades.png",
            "desc": "Formaci&oacute;n, apoyo psicosocial, transferencias monetarias condicionadas y acompa&ntilde;amiento laboral para j&oacute;venes de 14 a 28 a&ntilde;os en condici&oacute;n de vulnerabilidad.",
        },
        {
            "alt": "Servicio Forjar Restaurativo",
            "archivo": "gestion_conocimiento_forjar_2025.html",
            "imagen": "imagenes/servicios/forjar.png",
            "desc": "Servicio de atenci&oacute;n integral, especializada y diferencial que se brinda a adolescentes/j&oacute;venes vinculados al SRPA y sus redes familiares, en el marco de modalidades de atenci&oacute;n no privativas de la libertad, desde un enfoque pedag&oacute;gico y restaurativo.",
        },
        {
            "alt": "Parche seguro",
            "archivo": "gestion_conocimiento_alertas_2025.html",
            "imagen": "imagenes/servicios/alertas.png",
            "desc": "Sistema de identificaci&oacute;n y seguimiento de alertas tempranas para la protecci&oacute;n integral de la poblaci&oacute;n joven.",
        },
    ]

    # Colores de acento por servicio (borde hover)
    # Azul rey, lila, verde-menta (forjar), naranja (Parche seguro)
    colores = ["#1a237e", "#663A93", "#80cbc4", "#e67e22"]

    tarjetas = ""
    for i, s in enumerate(servicios):
        color = colores[i]
        tarjetas += f"""
            <a class="service-card" href="{s['archivo']}" style="--accent:{color};">
                <div class="service-desc">{s['desc']}</div>
                <div class="service-logo">
                    <img src="{s['imagen']}" alt="{s['alt']}">
                </div>
            </a>
"""

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestor de conocimiento - Subdirecci&oacute;n para la Juventud</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Anton&family=Figtree:wght@400;500;600;700;800&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Figtree', 'Segoe UI', sans-serif;
            background-color: #ffffff;
            color: #2F3E3C;
            min-height: 100vh;
        }}

        /* Header banner */
        .header-banner {{
            width: 100%;
            display: block;
        }}
        .header-banner img {{
            width: 100%;
            display: block;
        }}

        /* Contenido */
        .main {{ max-width: 1100px; margin: 0 auto; padding: 60px 30px 60px; }}

        /* Grid */
        .services-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 72px 36px;
            max-width: 1080px;
            margin: 0 auto;
            padding: 40px 0 40px;
        }}

        /* Tarjetas - flex column, logo sobresale por abajo (mitad dentro / mitad fuera) */
        .service-card {{
            background: rgba(255,255,255,0.75);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 20px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.04);
            padding: 24px 24px 14px;
            text-align: center;
            text-decoration: none;
            color: inherit;
            transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
            border: 2px solid rgba(0,0,0,0.04);
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            min-height: 150px;
            overflow: visible;
        }}
        .service-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 16px 40px rgba(0,0,0,0.1);
            border-color: var(--accent, #663A93);
        }}

        /* Descripci&oacute;n del servicio */
        .service-desc {{
            font-size: 0.88rem;
            color: #555;
            line-height: 1.5;
            text-align: center;
            margin: 0 auto;
            max-width: 340px;
        }}

        /* Logo — sobresale por el borde inferior (mitad dentro, mitad fuera) */
        .service-logo {{
            height: 56px;
            margin: 14px auto -28px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s;
            position: relative;
            z-index: 2;
        }}
        .service-logo img {{ height: 100%; object-fit: contain; }}
        .service-card:hover .service-logo {{ transform: scale(1.08); }}

        /* Bot&oacute;n de ayuda */
        .help-btn {{
            position: fixed; bottom: 80px; right: 28px; z-index: 100;
            width: 48px; height: 48px; border-radius: 50%;
            background: #2F3E3C; color: #F8F4E1; border: none;
            font-size: 1.4rem; font-weight: 700; cursor: pointer;
            box-shadow: 0 4px 16px rgba(0,0,0,0.18);
            transition: transform 0.2s, box-shadow 0.2s;
            display: flex; align-items: center; justify-content: center;
        }}
        .help-btn:hover {{ transform: scale(1.1); box-shadow: 0 6px 24px rgba(0,0,0,0.25); }}

        /* Modal */
        .modal-overlay {{
            display: none; position: fixed; inset: 0; z-index: 200;
            background: rgba(0,0,0,0.45); align-items: center; justify-content: center;
        }}
        .modal-overlay.show {{ display: flex; }}
        .modal-box {{
            background: #2F3E3C; color: #F8F4E1; border-radius: 14px;
            max-width: 560px; width: 90%; padding: 32px 36px 28px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.35); position: relative;
        }}
        .modal-box h2 {{ font-size: 1.35rem; font-weight: 700; margin-bottom: 6px; }}
        .modal-box .modal-sub {{ font-size: 0.85rem; opacity: 0.75; margin-bottom: 18px; }}
        .modal-box p {{ font-size: 0.92rem; line-height: 1.7; opacity: 0.9; margin-bottom: 12px; }}
        .modal-close {{
            position: absolute; top: 14px; right: 18px;
            background: none; border: none; color: #F8F4E1; font-size: 1.5rem;
            cursor: pointer; opacity: 0.6; transition: opacity 0.2s;
        }}
        .modal-close:hover {{ opacity: 1; }}

        @media (max-width: 700px) {{
            .services-grid {{ grid-template-columns: 1fr; gap: 40px; padding: 30px 0 30px; }}
            .main {{ padding: 35px 20px 40px; }}
            .service-desc {{ font-size: 0.9rem; }}
            .service-logo {{ height: 46px; }}
        }}
    </style>
</head>
<body>
    <div class="header-banner">
        <img src="imagenes/Header - gestor.jpeg" alt="Gestor de conocimiento - SDIS Juventud">
    </div>
    <main class="main">
        <div class="services-grid">
{tarjetas}
        </div>
    </main>
    <button class="help-btn" onclick="document.getElementById('modal-info').classList.add('show')" title="&iquest;Qu&eacute; es esto?">?</button>

    <div class="modal-overlay" id="modal-info" onclick="if(event.target===this)this.classList.remove('show')">
        <div class="modal-box">
            <button class="modal-close" onclick="document.getElementById('modal-info').classList.remove('show')">&times;</button>
            <h2>Gestor de conocimiento</h2>
            <div class="modal-sub">Subdirecci&oacute;n para la Juventud | SDIS</div>
            <p>Herramienta interna que documenta los procesos, datos, metodolog&iacute;as y aprendizajes de cada servicio de la Subdirecci&oacute;n para la Juventud.</p>
            <p>El objetivo es que cualquier persona del equipo pueda consultar c&oacute;mo funciona cada servicio, qu&eacute; datos se gestionan y cu&aacute;les son los procedimientos vigentes.</p>
        </div>
    </div>

    <footer style="background:#3a3a3a; padding:18px 30px; display:flex; justify-content:space-between; align-items:center;">
        <img src="imagenes/Footer1.png" alt="Distrito Joven" style="height:40px; object-fit:contain;">
        <img src="imagenes/Footer2.png" alt="Secretar&iacute;a de Integraci&oacute;n Social" style="height:40px; object-fit:contain;">
    </footer>
</body>
</html>"""

    ruta = os.path.join(BASE, "index.html")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Generado: index.html ({len(html):,} caracteres)".replace(",", "."))


# =====================================================================
# Ejecutar todo
# =====================================================================
if __name__ == "__main__":
    # Este script solo genera el index (home).
    # Los gestores de cada servicio se generan desde sus scripts individuales:
    # generar_juventud.py, generar_gc_forjar.py, generar_gc_jco.py, generar_gc_alertas.py.
    print("Generando pagina home del gestor de conocimiento...\n")
    generar_index()
    print("\nListo. Index generado.")
