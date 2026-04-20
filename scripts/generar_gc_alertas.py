# -*- coding: utf-8 -*-
"""
Genera el archivo gestion_conocimiento_alertas_2025.html
a partir de variables estructuradas en Python.

El objetivo es que las ediciones de contenido se hagan aquí
(texto, secciones, sidebar) sin tocar HTML crudo directamente.
"""

import os
import sys

# CSS compartido con los demás generadores
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _comun.estilos import css_para
# ─── Configuración ───────────────────────────────────────────────────────────

NOMBRE_ARCHIVO = "gestion_conocimiento_alertas_2025.html"
TITULO_PAGINA = "Gestor de conocimiento - Parche seguro"
TITULO_HEADER = "Gestor de conocimiento - Parche seguro"
SUBTITULO_HEADER = "Subdirecci&oacute;n para la Juventud | SDIS"

# ─── CSS ─────────────────────────────────────────────────────────────────────

CSS = css_para("alertas")

# ─── Header (barra superior) ────────────────────────────────────────────────

HEADER_HTML = f"""\
    <header class="header">
        <div>
            <h1>{TITULO_HEADER}</h1>
            <div class="subtitle">{SUBTITULO_HEADER}</div>
        </div>
        <div class="header-btns">
            <a class="home-btn" href="index.html" title="Todos los servicios">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8F4E1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
            </a>
            <div class="home-btn" onclick="showContent('welcome')" title="Inicio Parche seguro">
                <img src="imagenes/servicios/alertas.png" alt="Parche seguro" style="height:32px; border-radius:16px; object-fit:contain; vertical-align:middle;">
            </div>
        </div>
    </header>"""

# ─── Sidebar ─────────────────────────────────────────────────────────────────
# Cada sección del menú lateral se define por separado para facilitar edición.

SIDEBAR_CONTEXTO = """\
            <div class="sidebar-section">
                <div class="sidebar-title active" onclick="toggleSection(this)">
                    <span>Contexto</span><span class="arrow">&#9654;</span>
                </div>
                <div class="sidebar-items show">
                    <div class="sidebar-item" onclick="showContent('descripcion')">Descripci&oacute;n del equipo</div>
                </div>
            </div>"""

SIDEBAR_PROTOCOLOS = """\
            <div class="sidebar-section">
                <div class="sidebar-title" onclick="toggleSection(this)">
                    <span>Protocolos</span><span class="arrow">&#9654;</span>
                </div>
                <div class="sidebar-items">
                    <div class="sidebar-item" onclick="showContent('protocolos')">Protocolos de atenci&oacute;n</div>
                </div>
            </div>"""

SIDEBAR_ESTADISTICAS = """\
            <div class="sidebar-section">
                <div class="sidebar-title" onclick="showContent('estadisticas')" style="cursor:pointer;">
                    <span>Estad&iacute;sticas</span>
                </div>
            </div>"""

# Se ensambla el sidebar completo
SIDEBAR_HTML = f"""\
        <nav class="sidebar">
            <div class="sidebar-title" onclick="showContent('welcome')" style="cursor:pointer;"><span>Inicio</span></div>

{SIDEBAR_CONTEXTO}
{SIDEBAR_PROTOCOLOS}
{SIDEBAR_ESTADISTICAS}
        </nav>"""

# ─── Secciones de contenido ─────────────────────────────────────────────────
# Cada sección corresponde a un ítem del sidebar.

SECCION_WELCOME = """\
            <div class="content-section active" id="welcome">
                <div class="welcome-section">
                    <div style="font-family:'Anton','Figtree',sans-serif; font-weight:400; font-size:1.9rem; line-height:1.05; letter-spacing:1px; text-transform:uppercase; background:#2d2a28; color:#f4f5de; padding:14px 24px 11px; margin:0 auto 28px; display:block; width:fit-content; max-width:100%; text-align:center;">Parche seguro</div>
                    <p>Sistema de identificaci&oacute;n y seguimiento de alertas tempranas para la protecci&oacute;n integral de la poblaci&oacute;n joven. A partir del triage psicosocial, el equipo identifica situaciones de riesgo y activa los protocolos de atenci&oacute;n correspondientes.</p>
                </div>
            </div>"""

SECCION_DESCRIPCION = """\
            <div class="content-section" id="descripcion">
                <div class="card">
                    <h2 class="card-title">Descripci&oacute;n del equipo</h2>
                    <p>El equipo de alertas identifica j&oacute;venes con situaciones de riesgo a partir del <strong>triage psicosocial</strong>. Las alertas cubren situaciones como:</p>
                    <ul style="margin:10px 0 15px 20px; line-height:2;">
                        <li>Consumo problem&aacute;tico de sustancias psicoactivas</li>
                        <li>Ideaci&oacute;n suicida y conducta autolesiva</li>
                        <li>Violencia intrafamiliar</li>
                        <li>Explotaci&oacute;n sexual y comercial</li>
                        <li>Reclutamiento forzado</li>
                        <li>Otras vulneraciones de derechos</li>
                    </ul>
                    <p>Cuando se identifica una alerta, el equipo activa el protocolo correspondiente y realiza el seguimiento del caso hasta su cierre.</p>
                </div>
            </div>"""

SECCION_PROTOCOLOS = """\
            <div class="content-section" id="protocolos">
                <div class="card">
                    <h2 class="card-title">Protocolos de atenci&oacute;n</h2>
                    <p>La estrategia cuenta con <strong>m&aacute;s de 10 protocolos</strong> de atenci&oacute;n, cada uno con un procedimiento espec&iacute;fico. Referente: <strong>Paula</strong>.</p>
                    <p>Para cada protocolo se incluye: t&iacute;tulo, rese&ntilde;a corta y enlace al documento completo.</p>
                </div>
            </div>"""

SECCION_ESTADISTICAS = """\
            <div class="content-section" id="estadisticas">
                <div class="card">
                    <h2 class="card-title">Estad&iacute;sticas</h2>
                    <iframe title="Seguimiento t&eacute;cnico" width="100%" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiMzRiNWRkMDQtNThmNC00Yzk5LThjNTItOWI4MzZkYzYwM2EzIiwidCI6ImIzZTMwODA4LWU5YTgtNGYyYS05YmMxLWE3NjBhZTkxMGNmNSIsImMiOjR9" frameborder="0" allowFullScreen="true" style="border:1px solid #e0e0e0; border-radius:8px;"></iframe>
                </div>
            </div>"""

# ─── JavaScript ──────────────────────────────────────────────────────────────

JAVASCRIPT = """\
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
}"""

# ─── Ensamblaje del HTML completo ────────────────────────────────────────────

HTML_COMPLETO = f"""\
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{TITULO_PAGINA}</title>
    <style>
{CSS}</style>
</head>
<body>
{HEADER_HTML}
    <div class="container">
{SIDEBAR_HTML}
        <main class="main-content">

{SECCION_WELCOME}

{SECCION_DESCRIPCION}

{SECCION_PROTOCOLOS}

{SECCION_ESTADISTICAS}
        </main>
    </div>
    <script>
{JAVASCRIPT}
</script>
</body>
</html>
"""

# ─── Escritura del archivo ───────────────────────────────────────────────────

def main():
    """Genera el archivo HTML en la raíz del proyecto."""
    directorio = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_salida = os.path.join(directorio, NOMBRE_ARCHIVO)

    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(HTML_COMPLETO)

    print(f"Archivo generado: {ruta_salida}")


if __name__ == "__main__":
    main()
