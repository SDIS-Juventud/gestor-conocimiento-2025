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
                    <h2 class="card-title">Estad&iacute;sticas 2025</h2>
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
# 1. INDEX.HTML — Home de todos los servicios
# =====================================================================
def generar_index():
    servicios = [
        {
            "nombre": "Casas de Juventud",
            "archivo": "gestion_conocimiento_juventud_2025.html",
            "imagen": "imagenes/servicios/casas-de-juventud.png",
            "desc": "Espacios distritales para j&oacute;venes entre 14 y 28 a&ntilde;os. Oferta integral a trav&eacute;s de 5 ejes: bienestar, cultura, inclusi&oacute;n, liderazgo y SIDICU.",
            "badge": "active",
        },
        {
            "nombre": "J&oacute;venes con Oportunidades",
            "archivo": "gestion_conocimiento_jco_2025.html",
            "imagen": "imagenes/servicios/jovenes-con-oportunidades.png",
            "desc": "Formaci&oacute;n, apoyo psicosocial, transferencias monetarias condicionadas y acompa&ntilde;amiento laboral para j&oacute;venes de 14 a 28 a&ntilde;os en condici&oacute;n de vulnerabilidad.",
            "badge": "soon",
        },
        {
            "nombre": "Servicio Forjar Restaurativo",
            "archivo": "gestion_conocimiento_forjar_2025.html",
            "imagen": "imagenes/servicios/forjar.png",
            "desc": "Servicio restaurativo de atenci&oacute;n integral a adolescentes y j&oacute;venes vinculados al SRPA, con enfoque en sanciones no privativas de libertad y acompa&ntilde;amiento sociofamiliar.",
            "badge": "soon",
        },
        {
            "nombre": "Parche seguro",
            "archivo": "gestion_conocimiento_alertas_2025.html",
            "imagen": "imagenes/servicios/alertas.png",
            "desc": "Sistema de identificaci&oacute;n y seguimiento de alertas tempranas para la protecci&oacute;n integral de la poblaci&oacute;n joven.",
            "badge": "soon",
        },
    ]

    # Colores de acento por servicio (borde hover)
    # Azul rey, lila, azul claro (forjar), naranja (Parche seguro)
    colores = ["#1a237e", "#663A93", "#80cbc4", "#e67e22"]

    tarjetas = ""
    for i, s in enumerate(servicios):
        badge_class = "badge-active" if s["badge"] == "active" else "badge-soon"
        badge_text = "Estado: por completar" if s["badge"] == "active" else "Estado: inicial"
        color = colores[i]
        tarjetas += f"""
            <a class="service-card" href="{s['archivo']}" style="--accent:{color};">
                <div class="service-logo">
                    <img src="{s['imagen']}" alt="{s['nombre']}">
                </div>
                <div class="service-desc">{s['desc']}</div>
                <span class="{badge_class}">{badge_text}</span>
            </a>
"""

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestor de conocimiento - Subdirecci&oacute;n para la Juventud</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&display=swap');
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
        .intro {{ text-align: center; max-width: 700px; margin: 0 auto 55px; }}
        .intro h2 {{ font-size: 1.9rem; color: #2F3E3C; margin-bottom: 14px; font-weight: 800; }}
        .intro p {{ font-size: 1rem; line-height: 1.7; color: #666; }}

        /* Grid */
        .services-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 28px;
            max-width: 880px;
            margin: 0 auto;
        }}

        /* Tarjetas */
        .service-card {{
            background: rgba(255,255,255,0.75);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 20px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.04);
            padding: 36px 28px 30px;
            text-align: center;
            text-decoration: none;
            color: inherit;
            transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
            border: 2px solid rgba(0,0,0,0.04);
            position: relative;
        }}
        .service-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 16px 40px rgba(0,0,0,0.1);
            border-color: var(--accent, #663A93);
        }}

        /* Logo */
        .service-logo {{
            height: 52px;
            margin: 0 auto 22px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s;
        }}
        .service-logo img {{ height: 100%; border-radius: 30px; object-fit: contain; }}
        .service-card:hover .service-logo {{ transform: scale(1.08); }}

        .service-title {{ font-size: 1.15rem; font-weight: 700; margin-bottom: 10px; }}
        .service-desc {{ font-size: 0.88rem; color: #888; line-height: 1.65; }}

        /* Badges */
        .badge-soon {{
            display: inline-block; margin-top: 14px; padding: 5px 16px;
            border-radius: 20px; font-size: 0.72rem; font-weight: 600;
            background: #e8760a; color: #ffffff;
        }}
        .badge-active {{
            display: inline-block; margin-top: 14px; padding: 5px 16px;
            border-radius: 20px; font-size: 0.72rem; font-weight: 600;
            background: #2e7d52; color: #ffffff;
        }}

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
            .services-grid {{ grid-template-columns: 1fr; gap: 20px; }}
            .main {{ padding: 35px 20px 40px; }}
            .intro h2 {{ font-size: 1.4rem; }}
        }}
    </style>
</head>
<body>
    <div class="header-banner">
        <img src="imagenes/Header - gestor.jpeg" alt="Gestor de conocimiento - SDIS Juventud">
    </div>
    <main class="main">
        <div class="intro">
            <p>Documentaci&oacute;n de procesos, datos y gesti&oacute;n del conocimiento de cada servicio de la Subdirecci&oacute;n para la Juventud.</p>
        </div>
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
# 2. JÓVENES CON OPORTUNIDADES
# =====================================================================
def generar_jco():
    sidebar = """
            <div class="sidebar-section">
                <div class="sidebar-title active" onclick="toggleSection(this)">
                    <span>Contexto</span><span class="arrow">&#9654;</span>
                </div>
                <div class="sidebar-items show">
                    <div class="sidebar-item" onclick="showContent('antecedentes')">Antecedentes y transformaci&oacute;n</div>
                    <div class="sidebar-item" onclick="showContent('pilares')">Pilares del programa</div>
                    <div class="sidebar-item" onclick="showContent('requisitos')">Requisitos y selecci&oacute;n</div>
                    <div class="sidebar-item" onclick="showContent('impacto')">Impacto y alcance</div>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-title" onclick="toggleSection(this)">
                    <span>Proyecto de vida</span><span class="arrow">&#9654;</span>
                </div>
                <div class="sidebar-items">
                    <div class="sidebar-item" onclick="showContent('modulos')">M&oacute;dulos</div>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-title" onclick="toggleSection(this)">
                    <span>Componente psicosocial</span><span class="arrow">&#9654;</span>
                </div>
                <div class="sidebar-items">
                    <div class="sidebar-item" onclick="showContent('triage')">Triage psicosocial</div>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-title" onclick="toggleSection(this)">
                    <span>Enlaces oficiales</span><span class="arrow">&#9654;</span>
                </div>
                <div class="sidebar-items">
                    <div class="sidebar-item" onclick="showContent('enlaces')">Manuales y gu&iacute;as</div>
                </div>
            </div>"""

    contenido = f"""
            <div class="content-section active" id="welcome">
                <div class="welcome-section">
                    <h2>J&oacute;venes con Oportunidades</h2>
                    <p>Ruta de inclusi&oacute;n social y productiva de la Alcald&iacute;a de Bogot&aacute; para empoderar a j&oacute;venes de 14 a 28 a&ntilde;os en situaci&oacute;n de pobreza extrema, moderada o vulnerabilidad, especialmente aquellos que no estudian ni trabajan.</p>
                    <p>Iniciativa conjunta entre la Secretar&iacute;a de Integraci&oacute;n Social, la Secretar&iacute;a de Desarrollo Econ&oacute;mico, la Secretar&iacute;a de Educaci&oacute;n y la Agencia Atenea.</p>
                    <div style="margin:30px auto 0; max-width:450px;">
                        <img src="imagenes/Jovenes con oportunidades.png" alt="J&oacute;venes con Oportunidades" style="width:100%; border-radius:12px; box-shadow:0 4px 15px rgba(0,0,0,0.1);">
                    </div>
                </div>
            </div>

            <div class="content-section" id="antecedentes">
                <div class="card">
                    <h2 class="card-title">Antecedentes y transformaci&oacute;n</h2>
                    <p style="line-height:1.7;">El programa de transferencias monetarias para la juventud en Bogot&aacute; pas&oacute; del modelo conocido como <strong>&ldquo;Parceros por Bogot&aacute;&rdquo;</strong> (administraci&oacute;n anterior) al actual <strong>&ldquo;J&oacute;venes con Oportunidades&rdquo;</strong>, lanzado a finales de 2024. Ambos programas comparten la misma esencia: est&aacute;n dirigidos a j&oacute;venes vulnerables o en condici&oacute;n de pobreza (Sisb&eacute;n A hasta C09) de 14 a 28 a&ntilde;os, y mantienen el acompa&ntilde;amiento psicosocial permanente como base para fortalecer el proyecto de vida.</p>

                    <h3 class="card-subtitle">Cambios en el monto y estructura de la transferencia</h3>
                    <p style="line-height:1.7;">En Parceros por Bogot&aacute;, los j&oacute;venes recib&iacute;an una cuota fija de <strong>$500.000 mensuales durante 6 meses</strong>. En J&oacute;venes con Oportunidades, el apoyo econ&oacute;mico depende de la ruta de formaci&oacute;n elegida: hasta $1.200.000 en cursos cortos, $1.000.000 por ciclo acad&eacute;mico m&aacute;s $300.000 por intermediaci&oacute;n laboral para quienes terminan bachillerato, o transferencias semestrales de sostenimiento para educaci&oacute;n superior.</p>

                    <h3 class="card-subtitle">Cambios en las actividades</h3>
                    <p style="line-height:1.7;">Parceros por Bogot&aacute; ten&iacute;a un componente de trabajo social comunitario: los j&oacute;venes se formaban durante 100 horas como Agentes Comunitarios de Prevenci&oacute;n (salud mental, violencias, consumo) y realizaban actividades de apoyo a servicios de la ciudad. J&oacute;venes con Oportunidades reemplaza este componente por una ruta de inclusi&oacute;n social y productiva con tres trayectorias: terminar el colegio, hacer cursos cortos t&eacute;cnicos o entrar a educaci&oacute;n superior.</p>

                    <h3 class="card-subtitle">Apuesta por la empleabilidad</h3>
                    <p style="line-height:1.7;">El programa actual consolida una etapa formal de <strong>intermediaci&oacute;n laboral</strong> con orientaci&oacute;n ocupacional y formaci&oacute;n en habilidades blandas, integrando los esfuerzos de la Secretar&iacute;a de Desarrollo Econ&oacute;mico para conectar a los j&oacute;venes con ofertas de empleo.</p>

                    <h3 class="card-subtitle">Articulaci&oacute;n y cobertura</h3>
                    <p style="line-height:1.7;">Parceros logr&oacute; beneficiar a cerca de <strong>28.000 j&oacute;venes</strong> al cierre de su ciclo. J&oacute;venes con Oportunidades es un esfuerzo articulado entre las Secretar&iacute;as de Integraci&oacute;n Social, Desarrollo Econ&oacute;mico, Educaci&oacute;n y la Agencia Atenea, con meta de llegar a <strong>40.000 j&oacute;venes</strong> en el cuatrienio.</p>
                </div>
            </div>

            <div class="content-section" id="pilares">
                <div class="card">
                    <h2 class="card-title">Pilares del programa</h2>

                    <h3 class="card-subtitle">1. Acompa&ntilde;amiento psicosocial</h3>
                    <p style="line-height:1.7;">Orientaci&oacute;n y seguimiento durante todo el tiempo de permanencia en el programa para ayudar a los j&oacute;venes a fortalecer su proyecto de vida y superar retos personales.</p>

                    <h3 class="card-subtitle">2. Rutas de formaci&oacute;n</h3>
                    <p style="line-height:1.7;">Los participantes eligen entre tres opciones:</p>
                    <table style="width:100%; border-collapse:collapse; font-size:0.85rem;">
                        <thead>
                            <tr style="background:#f8f9fa;">
                                <th style="padding:10px; border-bottom:2px solid var(--accent); text-align:left;">Ruta</th>
                                <th style="padding:10px; border-bottom:2px solid var(--accent); text-align:left;">Descripci&oacute;n</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="background:#fff;"><td style="padding:8px 10px; border-bottom:1px solid #eee;"><strong>Educaci&oacute;n para j&oacute;venes y adultos</strong></td><td style="padding:8px 10px; border-bottom:1px solid #eee;">Para terminar el bachillerato (grados 10&deg; y 11&deg;) en jornadas nocturnas o fines de semana</td></tr>
                            <tr style="background:#f8f9fa;"><td style="padding:8px 10px; border-bottom:1px solid #eee;"><strong>Cursos cortos certificados</strong></td><td style="padding:8px 10px; border-bottom:1px solid #eee;">Formaciones de 40 a 160 horas para adquirir conocimientos t&eacute;cnicos y habilidades pr&aacute;cticas para el empleo</td></tr>
                            <tr style="background:#fff;"><td style="padding:8px 10px; border-bottom:1px solid #eee;"><strong>Educaci&oacute;n posmedia de ciclo largo</strong></td><td style="padding:8px 10px; border-bottom:1px solid #eee;">Acceso a Educaci&oacute;n y Formaci&oacute;n para el Trabajo (EFT) o educaci&oacute;n superior, articul&aacute;ndose con iniciativas como J&oacute;venes a la E</td></tr>
                        </tbody>
                    </table>

                    <h3 class="card-subtitle">3. Acompa&ntilde;amiento a la empleabilidad</h3>
                    <p style="line-height:1.7;">Orientaci&oacute;n ocupacional y formaci&oacute;n en habilidades blandas para conectar a los j&oacute;venes con oportunidades laborales (intermediaci&oacute;n laboral).</p>

                    <h3 class="card-subtitle">4. Transferencias monetarias condicionadas</h3>
                    <p style="line-height:1.7;">Apoyos econ&oacute;micos de <strong>$200.000 a $1.200.000</strong> dependiendo de la ruta de formaci&oacute;n elegida. El dinero se entrega por partes a medida que el joven avanza y cumple con sus actividades, a trav&eacute;s de operadores financieros o billeteras digitales (Daviplata, Nequi, Movii, Efecty, Dale).</p>
                </div>
            </div>

            <div class="content-section" id="requisitos">
                <div class="card">
                    <h2 class="card-title">Requisitos y criterios de selecci&oacute;n</h2>

                    <h3 class="card-subtitle">Requisitos obligatorios</h3>
                    <ul style="margin:10px 0 15px 20px; line-height:2;">
                        <li>Tener entre <strong>14 y 28 a&ntilde;os</strong></li>
                        <li>Residir en <strong>Bogot&aacute;</strong></li>
                        <li>Estar clasificado en <strong>Sisb&eacute;n IV</strong> (grupos A a C09) o en listados oficiales de grupos &eacute;tnicos</li>
                        <li>Poblaci&oacute;n migrante: contar con C&eacute;dula de Extranjer&iacute;a o Permiso de Protecci&oacute;n Temporal (PPT)</li>
                    </ul>

                    <h3 class="card-subtitle">Criterios de priorizaci&oacute;n</h3>
                    <p style="line-height:1.7;">Debido a cupos limitados, se da mayor puntaje a poblaciones vulnerables:</p>
                    <ul style="margin:10px 0 15px 20px; line-height:2;">
                        <li>Mujeres</li>
                        <li>V&iacute;ctimas del conflicto armado</li>
                        <li>Personas con discapacidad</li>
                        <li>Grupos &eacute;tnicos</li>
                        <li>Habitantes rurales</li>
                        <li>Cuidadores</li>
                        <li>Personas sin seguridad social en salud o sin empleo</li>
                        <li>Pagadiarios</li>
                    </ul>
                    <p style="line-height:1.7;">Estar en este programa <strong>no impide recibir otros subsidios</strong> a nivel distrital o nacional.</p>
                </div>
            </div>

            <div class="content-section" id="impacto">
                <div class="card">
                    <h2 class="card-title">Impacto y alcance</h2>
                    <p style="line-height:1.7;">La meta del programa es beneficiar a <strong>40.000 j&oacute;venes</strong> a lo largo del cuatrienio de la actual administraci&oacute;n.</p>
                    <p style="line-height:1.7;">Para 2025, el Distrito abri&oacute; una convocatoria inicial de 17.000 cupos, que fue ampliada a 25.000 tras la alta demanda, logrando m&aacute;s de <strong>70.000 j&oacute;venes preinscritos</strong>.</p>
                </div>
            </div>

            <div class="content-section" id="modulos">
                <div class="card">
                    <h2 class="card-title">M&oacute;dulos de proyecto de vida</h2>
                    <p>El componente de proyecto de vida se estructura en <strong>7 m&oacute;dulos</strong>:</p>
                    <ul style="margin:10px 0 15px 20px; line-height:2;">
                        <li><span class="badge badge-primary">M&oacute;dulo 1</span> Sentido de la vida</li>
                        <li><span class="badge badge-primary">M&oacute;dulo 2</span> Coaching en finanzas</li>
                        <li><span class="badge badge-primary">M&oacute;dulo 3</span> Manejo del estr&eacute;s</li>
                        <li><span class="badge badge-primary">M&oacute;dulo 4</span> <em>Pendiente</em></li>
                        <li><span class="badge badge-primary">M&oacute;dulo 5</span> <em>Pendiente</em></li>
                        <li><span class="badge badge-primary">M&oacute;dulo 6</span> <em>Pendiente</em></li>
                        <li><span class="badge badge-primary">M&oacute;dulo 7</span> <em>Pendiente</em></li>
                    </ul>
                </div>
            </div>

            <div class="content-section" id="triage">
                <div class="card">
                    <h2 class="card-title">Triage psicosocial</h2>
                    <p>El componente psicosocial realiza un <strong>triage</strong> al ingreso de cada joven al programa. El equipo profesional clasifica el nivel de riesgo y activa las rutas de atenci&oacute;n correspondientes.</p>
                </div>
            </div>

            <div class="content-section" id="enlaces">
                <div class="card">
                    <h2 class="card-title">Manuales y gu&iacute;as oficiales</h2>
                    <p>Enlaces directos a los documentos de consulta para cada m&oacute;dulo del programa.</p>
                </div>
            </div>"""

    generar_pagina_servicio(
        titulo="J&oacute;venes con Oportunidades",
        subtitulo="Subdirecci&oacute;n para la Juventud | SDIS",
        sidebar_html=sidebar,
        contenido_html=contenido,
        archivo="gestion_conocimiento_jco_2025.html",
        logo_img="imagenes/servicios/jovenes-con-oportunidades.png",
        color_key="jco",
    )


# =====================================================================
# 3. SERVICIO FORJAR RESTAURATIVO
# =====================================================================
def generar_forjar():
    import json as _json
    import unicodedata, re

    def normalizar(texto):
        texto = unicodedata.normalize('NFC', texto).upper().strip()
        texto = texto.replace('Ñ', 'N').replace('ñ', 'n')
        texto = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
        texto = re.sub(r'^(LA |LOS |EL )', '', texto)
        return texto

    # Leer directorio de unidades operativas desde Excel
    excel_forjar = os.path.join(DATOS, "directorio_forjar.xlsx")
    df_forjar = pd.read_excel(excel_forjar)

    # Generar tabla HTML con el mismo estilo que Casas de Juventud
    tabla_forjar = '<div style="margin-top:25px;">\n'
    tabla_forjar += '                <h3 class="card-subtitle">Directorio</h3>\n'
    tabla_forjar += '                <table style="width:100%; border-collapse:collapse; font-size:0.85rem;">\n'
    tabla_forjar += '                    <thead>\n'
    tabla_forjar += '                        <tr style="background:#f8f9fa;">\n'
    tabla_forjar += '                            <th style="padding:10px; border-bottom:2px solid var(--accent); text-align:left;">Unidad operativa</th>\n'
    tabla_forjar += '                            <th style="padding:10px; border-bottom:2px solid var(--accent); text-align:left;">Localidad</th>\n'
    tabla_forjar += '                            <th style="padding:10px; border-bottom:2px solid var(--accent); text-align:left;">Direcci&oacute;n</th>\n'
    tabla_forjar += '                        </tr>\n'
    tabla_forjar += '                    </thead>\n'
    tabla_forjar += '                    <tbody>\n'
    for idx, row in df_forjar.iterrows():
        bg = '#fff' if idx % 2 == 0 else '#f8f9fa'
        nombre = row["Nombre unidad operativa"]
        localidad = row["Localidad"]
        direccion = row["Dirección"]
        link = row.get("Link Google Maps", "")
        if pd.notna(link) and link:
            dir_html = f'<a href="{link}" target="_blank" style="color:var(--accent);">{direccion}</a>'
        else:
            dir_html = direccion
        tabla_forjar += f'                        <tr style="background:{bg};">\n'
        tabla_forjar += f'                            <td style="padding:8px 10px; border-bottom:1px solid #eee;"><strong>{nombre}</strong></td>\n'
        tabla_forjar += f'                            <td style="padding:8px 10px; border-bottom:1px solid #eee;">{localidad}</td>\n'
        tabla_forjar += f'                            <td style="padding:8px 10px; border-bottom:1px solid #eee;">{dir_html}</td>\n'
        tabla_forjar += '                        </tr>\n'
    tabla_forjar += '                    </tbody>\n'
    tabla_forjar += '                </table>\n'
    tabla_forjar += '            </div>'

    # Generar mapa con Folium (mismo estilo que Casas de Juventud)
    geojson_path = os.path.join(DATOS, "localidades_bogota.geojson")
    m = folium.Map(location=[4.624, -74.105], zoom_start=11, tiles="CartoDB positron", width="100%", height="100%")

    # Capa de localidades si existe el geojson
    if os.path.exists(geojson_path):
        with open(geojson_path, encoding="utf-8") as f:
            localidades_gj = _json.load(f)
        locs_forjar = set(normalizar(l) for l in df_forjar["Localidad"].unique())

        def style_loc(feature):
            nombre = normalizar(feature["properties"]["nombre"])
            if nombre in locs_forjar:
                return {"fillColor": "#d5e8e8", "color": "#5f9ea0", "weight": 2, "fillOpacity": 0.4}
            else:
                return {"fillColor": "#f0f0f0", "color": "#999", "weight": 1.5, "fillOpacity": 0.2}

        folium.GeoJson(localidades_gj, name="Localidades", style_function=style_loc,
            tooltip=folium.GeoJsonTooltip(fields=["nombre"], aliases=["Localidad:"])).add_to(m)

    # Marcadores circulares
    for _, row in df_forjar.iterrows():
        lat, lon = row["Latitud"], row["Longitud"]
        if pd.notna(lat) and pd.notna(lon):
            popup_html = f'<div style="font-family:Arial; min-width:200px;"><strong style="color:#5f9ea0; font-size:14px;">{row["Nombre unidad operativa"]}</strong><br><span style="color:#666; font-size:12px;">{row["Localidad"]}</span><br><span style="font-size:11px;">{row["Dirección"]}</span></div>'
            folium.CircleMarker(
                location=[lat, lon], radius=8, color="#5f9ea0",
                fill=True, fill_color="#5f9ea0", fill_opacity=0.9, weight=2,
                popup=folium.Popup(popup_html, max_width=250),
                tooltip=row["Nombre unidad operativa"]
            ).add_to(m)

    m.save(os.path.join(BASE, "mapa_forjar.html"))

    sidebar = """
            <div class="sidebar-section">
                <div class="sidebar-title active" onclick="toggleSection(this)">
                    <span>Contexto</span><span class="arrow">&#9654;</span>
                </div>
                <div class="sidebar-items show">
                    <div class="sidebar-item" onclick="showContent('linea_tiempo')">L&iacute;nea de tiempo</div>
                    <div class="sidebar-item" onclick="showContent('a_tener_en_cuenta')">A tener en cuenta</div>
                    <div class="sidebar-item" onclick="showContent('equipo')">Equipo</div>
                    <div class="sidebar-item" onclick="showContent('ubicacion')">Ubicaci&oacute;n</div>
                    <div class="sidebar-item" onclick="showContent('modalidades')">Modalidades de atenci&oacute;n</div>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-title" onclick="toggleSection(this)">
                    <span>Gesti&oacute;n de datos</span><span class="arrow">&#9654;</span>
                </div>
                <div class="sidebar-items">
                    <div class="sidebar-item" onclick="showContent('flujo_datos')">Flujo de gesti&oacute;n de la informaci&oacute;n</div>
                    <div class="sidebar-item" onclick="showContent('datos_sirbe')">Datos SIRBE</div>
                </div>
            </div>"""

    contenido = f"""
            <div class="content-section active" id="welcome">
                <div class="welcome-section">
                    <h2>Servicio Forjar Restaurativo</h2>
                    <p>Servicio de la Subdirecci&oacute;n para la Juventud dirigido a adolescentes y j&oacute;venes de 14 a 28 a&ntilde;os vinculados al Sistema de Responsabilidad Penal para Adolescentes (SRPA). Ofrece acompa&ntilde;amiento integral con enfoque restaurativo, priorizando sanciones no privativas de libertad y el acompa&ntilde;amiento en el medio sociofamiliar.</p>
                    <p>Opera en tres unidades operativas ubicadas en las localidades de Suba, Ciudad Bol&iacute;var y Rafael Uribe Uribe.</p>
                    <div style="margin:30px auto 0; max-width:450px;">
                        <img src="imagenes/Forjar.jpg" alt="Servicio Forjar Restaurativo" style="width:100%; border-radius:12px; box-shadow:0 4px 15px rgba(0,0,0,0.1);">
                    </div>
                </div>
            </div>

            <div class="content-section" id="linea_tiempo">
                <div class="card">
                    <h2 class="card-title">L&iacute;nea de tiempo</h2>
                    <div class="timeline">
                        <div class="timeline-item">
                            <div class="timeline-year">2010</div>
                            <div class="timeline-text"><strong>Creaci&oacute;n como proyecto de inversi&oacute;n.</strong> El servicio nace en la localidad de Ciudad Bol&iacute;var como respuesta a la &ldquo;delincuencia juvenil&rdquo; identificada en las zonas de calor. Funcion&oacute; a trav&eacute;s de un convenio de la Alcald&iacute;a local y cooperaci&oacute;n internacional (una ONG y Artesan&iacute;as de Colombia), con enfoque en formaci&oacute;n en artes y oficios.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2012 &ndash; 2013</div>
                            <div class="timeline-text"><strong>Consolidaci&oacute;n e institucionalizaci&oacute;n en la SDIS.</strong> Se determina que la SDIS debe asumir la operaci&oacute;n desde un enfoque de inclusi&oacute;n y pol&iacute;tica p&uacute;blica. A partir de 2013 se consolida como servicio especializado de atenci&oacute;n integral, operado directamente por la SDIS (inicialmente bajo la Subdirecci&oacute;n para la Infancia), dirigido a sanciones no privativas de libertad y restablecimiento de derechos. Se abren las unidades operativas de <strong>Suba</strong> y <strong>Rafael Uribe Uribe</strong> para cubrir el 100% del distrito.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2020 (septiembre)</div>
                            <div class="timeline-text"><strong>Transici&oacute;n a la Subdirecci&oacute;n para la Juventud.</strong> El servicio es trasladado de la Subdirecci&oacute;n para la Infancia a la Subdirecci&oacute;n para la Juventud, enmarcado bajo el proyecto de inversi&oacute;n 7740 &ldquo;Generaci&oacute;n J&oacute;venes con Derechos en Bogot&aacute;&rdquo;.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2021</div>
                            <div class="timeline-text"><strong>Creaci&oacute;n de nuevas rutas de atenci&oacute;n.</strong> Se dise&ntilde;a la <strong>Ruta de Oportunidades Juveniles</strong> para ampliar opciones en educaci&oacute;n, inclusi&oacute;n productiva, cultura y recreaci&oacute;n. Tambi&eacute;n surge la <strong>Ruta Integral de Atenci&oacute;n para J&oacute;venes (RIAJ)</strong>, estrategia propia de la SDIS para orientar a quienes est&aacute;n vinculados al SRPA y esperan la resoluci&oacute;n de su situaci&oacute;n socio-jur&iacute;dica.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2023</div>
                            <div class="timeline-text"><strong>Actualizaci&oacute;n normativa y metodol&oacute;gica.</strong> Se expide un marco normativo robusto: adopci&oacute;n del Anexo T&eacute;cnico de Est&aacute;ndares de Calidad (Resoluci&oacute;n 0824, abril 2023) y publicaci&oacute;n del Documento Metodol&oacute;gico (septiembre 2023). Se armonizan los postulados de justicia restaurativa y juvenil con las din&aacute;micas sociales actuales y las pol&iacute;ticas p&uacute;blicas distritales.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2025</div>
                            <div class="timeline-text"><strong>Fortalecimiento del acompa&ntilde;amiento al pos-egreso.</strong> Se ampl&iacute;a la Estrategia de Acompa&ntilde;amiento al Egreso para brindar continuidad voluntaria por 6 meses a 1 a&ntilde;o tras cumplir la sanci&oacute;n, consolidando la inclusi&oacute;n social y productiva a trav&eacute;s de la Ruta de Oportunidades Juveniles.</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section" id="a_tener_en_cuenta">
                <div class="card">
                    <h2 class="card-title">A tener en cuenta</h2>

                    <h3 class="card-subtitle">El nombre refleja un cambio de paradigma</h3>
                    <p style="line-height:1.7;">El servicio antes se conoc&iacute;a como &ldquo;Centros Forjar&rdquo;. La palabra &ldquo;centro&rdquo; fue eliminada porque los j&oacute;venes la asociaban con centros de reclusi&oacute;n, lo que iba en contra del enfoque restaurativo del programa. La referencia correcta es &ldquo;servicio Forjar&rdquo; o &ldquo;servicio Forjar Restaurativo&rdquo;. Nunca &ldquo;Centro Forjar&rdquo;.</p>

                    <h3 class="card-subtitle">Justicia restaurativa, no retributiva</h3>
                    <p style="line-height:1.7;">El servicio se fundamenta en tres pilares: la responsabilizaci&oacute;n, la reparaci&oacute;n del da&ntilde;o y la inclusi&oacute;n social (reintegraci&oacute;n). Se distancia del modelo de justicia retributiva centrado en el castigo.</p>

                    <h3 class="card-subtitle">Atenci&oacute;n a j&oacute;venes mayores de edad</h3>
                    <p style="line-height:1.7;">Aunque el SRPA atiende a quienes cometieron un delito siendo menores de 18 a&ntilde;os, Forjar atiende a j&oacute;venes hasta los 28 a&ntilde;os (11 meses y 29 d&iacute;as). Debido a los tiempos de los procesos judiciales, m&aacute;s de la mitad de la poblaci&oacute;n atendida actualmente es mayor de edad, lo que lleva al servicio a enfocarse en necesidades de juventud como empleabilidad y emprendimiento.</p>

                    <h3 class="card-subtitle">Cobertura distrital desde tres puntos estrat&eacute;gicos</h3>
                    <p style="line-height:1.7;">Aunque opera f&iacute;sicamente en tres unidades operativas (Suba, Ciudad Bol&iacute;var y Rafael Uribe Uribe), ubicadas en localidades con alta incidencia, Forjar atiende al 100% de la poblaci&oacute;n objetivo del Distrito Capital, recibiendo j&oacute;venes de cualquier localidad.</p>

                    <h3 class="card-subtitle">Continuidad voluntaria despu&eacute;s de la sanci&oacute;n</h3>
                    <p style="line-height:1.7;">El acompa&ntilde;amiento no termina cuando se cumple la orden del juez. La estrategia de acompa&ntilde;amiento al pos-egreso permite a los j&oacute;venes continuar de manera 100% voluntaria por 6 meses a 1 a&ntilde;o, buscando consolidar su proyecto de vida y evitar el retorno a entornos vulnerables sin apoyo institucional.</p>

                    <h3 class="card-subtitle">Cumplimiento de mandatos judiciales</h3>
                    <p style="line-height:1.7;">A diferencia de otros servicios de la Subdirecci&oacute;n, Forjar no es voluntario: da cumplimiento a sanciones y medidas impuestas por autoridades judiciales. Esto significa que la atenci&oacute;n no puede interrumpirse ni postergarse, ya que cualquier falla en la prestaci&oacute;n del servicio puede generar consecuencias legales y disciplinarias para la entidad, adem&aacute;s de afectar directamente el proceso de los j&oacute;venes.</p>
                </div>
            </div>

            <div class="content-section" id="equipo">
                <div class="card">
                    <h2 class="card-title">Equipo</h2>

                    <h3 class="card-subtitle">Liderazgo</h3>
                    <p style="line-height:1.7;"><strong>Aura Vanessa Le&oacute;n</strong> &mdash; L&iacute;der del Servicio Forjar Restaurativo, Subdirecci&oacute;n para la Juventud, SDIS.</p>
                    <p style="line-height:1.7;">Coordina la atenci&oacute;n especializada, formaci&oacute;n para el trabajo y oportunidades juveniles. El servicio hace parte de la estructura territorial de la SDIS, reportando al Subdirector para la Juventud.</p>

                    <h3 class="card-subtitle">Componentes profesionales</h3>

                    <table style="width:100%; border-collapse:collapse; font-size:0.85rem;">
                        <thead>
                            <tr style="background:#f8f9fa;">
                                <th style="padding:10px; border-bottom:2px solid var(--accent); text-align:left;">Componente</th>
                                <th style="padding:10px; border-bottom:2px solid var(--accent); text-align:left;">Profesionales</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="background:#fff;"><td style="padding:8px 10px; border-bottom:1px solid #eee;"><strong>Psicosocial</strong></td><td style="padding:8px 10px; border-bottom:1px solid #eee;">Trabajo social y psicolog&iacute;a</td></tr>
                            <tr style="background:#f8f9fa;"><td style="padding:8px 10px; border-bottom:1px solid #eee;"><strong>Pedag&oacute;gico</strong></td><td style="padding:8px 10px; border-bottom:1px solid #eee;">Pedagog&iacute;a y terapia ocupacional</td></tr>
                            <tr style="background:#fff;"><td style="padding:8px 10px; border-bottom:1px solid #eee;"><strong>Estilos de vida saludable</strong></td><td style="padding:8px 10px; border-bottom:1px solid #eee;">Nutrici&oacute;n y enfermer&iacute;a</td></tr>
                            <tr style="background:#f8f9fa;"><td style="padding:8px 10px; border-bottom:1px solid #eee;"><strong>Ruta de oportunidades juveniles</strong></td><td style="padding:8px 10px; border-bottom:1px solid #eee;">Enlace social</td></tr>
                            <tr style="background:#fff;"><td style="padding:8px 10px; border-bottom:1px solid #eee;"><strong>Socio-jur&iacute;dico</strong></td><td style="padding:8px 10px; border-bottom:1px solid #eee;">Abogados</td></tr>
                            <tr style="background:#f8f9fa;"><td style="padding:8px 10px; border-bottom:1px solid #eee;"><strong>Administrativo y t&eacute;cnico</strong></td><td style="padding:8px 10px; border-bottom:1px solid #eee;">Administrativo, coordinaci&oacute;n y enlace CESPA (Centro de Servicios Judiciales para Adolescentes)</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="content-section" id="ubicacion">
                <div class="card">
                    <h2 class="card-title">Ubicaci&oacute;n</h2>
                    <p style="line-height:1.7;">El servicio Forjar Restaurativo opera en <strong>{len(df_forjar)} unidades operativas</strong> ubicadas en localidades con alta incidencia, con cobertura para el 100% del Distrito Capital.</p>
                    <p style="line-height:1.7;">Aunque opera desde estos puntos, el servicio recibe j&oacute;venes de <strong>cualquier localidad</strong> de Bogot&aacute;.</p>

                    <div style="margin:20px 0;">
                        <iframe src="mapa_forjar.html" width="100%" height="450" style="border:1px solid #e0e0e0; border-radius:8px;" loading="lazy"></iframe>
                    </div>

                    {tabla_forjar}
                </div>
            </div>

            <div class="content-section" id="modalidades">
                <div class="card">
                    <h2 class="card-title">Modalidades de atenci&oacute;n</h2>
                    <div class="methodology-box" style="margin-bottom:20px;">
                        <strong>El servicio Forjar Restaurativo est&aacute; dise&ntilde;ado espec&iacute;ficamente para dar cumplimiento a sanciones no privativas de la libertad en medio abierto y comunitario.</strong> Las principales sanciones no privativas que atiende son la <strong>Prestaci&oacute;n de Servicios a la Comunidad</strong> y la <strong>Libertad Asistida y/o Vigilada</strong>. Adem&aacute;s, recibe j&oacute;venes para medidas de restablecimiento de derechos (IARAJ y RIAJ) y atiende a quienes han terminado sus sanciones y deciden continuar de forma voluntaria en la estrategia de acompa&ntilde;amiento al pos-egreso.
                    </div>
                    <p>En el marco del SRPA, las modalidades se clasifican seg&uacute;n el tipo de medida, sanci&oacute;n o estrategia impuesta por la autoridad competente.</p>

                    <h3 class="card-subtitle">1. No privativas de la libertad (sanciones)</h3>
                    <p>Se cumplen en medio abierto, sociofamiliar o comunitario. Buscan la responsabilizaci&oacute;n, reparaci&oacute;n del da&ntilde;o e inclusi&oacute;n social.</p>

                    <div class="methodology-box">
                        <strong>Libertad asistida y/o vigilada</strong><br>
                        Concesi&oacute;n de libertad otorgada por la autoridad judicial con la condici&oacute;n de que el adolescente o joven se someta a supervisi&oacute;n, asistencia y orientaci&oacute;n de un programa especializado. Busca fortalecer la autonom&iacute;a, la capacidad de reconocer la responsabilidad y la reparaci&oacute;n a trav&eacute;s de espacios pedag&oacute;gicos y pr&aacute;cticas restaurativas. M&iacute;nimo 10 actividades mensuales (individuales, familiares, grupales y en contexto).
                    </div>
                    <div class="methodology-box">
                        <strong>Prestaci&oacute;n de servicios a la comunidad</strong><br>
                        Ejecuci&oacute;n de acciones no remuneradas para restaurar los lazos afectados, posibilitando la reparaci&oacute;n (directa, indirecta o simb&oacute;lica) a la v&iacute;ctima, la familia o la comunidad. M&iacute;nimo 32 horas mensuales: 24 horas de trabajo comunitario y 8 horas de acompa&ntilde;amiento psicosocial.
                    </div>
                    <div class="methodology-box">
                        <strong>Internaci&oacute;n en medio semicerrado</strong><br>
                        Vinculaci&oacute;n a un programa de atenci&oacute;n especializada que se cumple durante el horario no escolar o no laboral.
                    </div>

                    <h3 class="card-subtitle">2. Apoyo y restablecimiento de derechos</h3>
                    <p>Medidas complementarias frente a vulneraciones de derechos.</p>

                    <div class="methodology-box">
                        <strong>IARAJ &mdash; Intervenci&oacute;n de apoyo al restablecimiento en administraci&oacute;n de justicia</strong><br>
                        Modalidad cuyo objetivo principal es el restablecimiento y la garant&iacute;a de los derechos de los adolescentes y j&oacute;venes, acompa&ntilde;ada de orientaci&oacute;n familiar. Ofrece apoyo pedag&oacute;gico, psicosocial y psicol&oacute;gico especializado para que el joven participe en escenarios de socializaci&oacute;n, comprenda y se responsabilice de los hechos en los que se involucr&oacute;, sea o no responsable a nivel jur&iacute;dico. M&iacute;nimo 10 actividades mensuales.
                    </div>
                    <div class="methodology-box">
                        <strong>RIAJ &mdash; Ruta integral de atenci&oacute;n para j&oacute;venes</strong><br>
                        Estrategia garantizada por la SDIS dirigida a j&oacute;venes (especialmente mayores de edad) que presentan alg&uacute;n conflicto con la ley y cuya situaci&oacute;n jur&iacute;dica a&uacute;n no ha sido definida. Busca favorecer el acceso a la oferta institucional y a oportunidades en educaci&oacute;n, empleo, emprendimiento, aprovechamiento del tiempo libre, arte, cultura y deporte.
                    </div>

                    <h3 class="card-subtitle">3. Estrategias transversales de continuidad</h3>

                    <div class="methodology-box">
                        <strong>Estrategia de acompa&ntilde;amiento al egreso (pos-egreso)</strong><br>
                        Dirigida a quienes culminaron el cumplimiento de diversas modalidades del SRPA y deciden dar continuidad voluntaria a su proceso. Acompa&ntilde;amiento por 6 meses a 1 a&ntilde;o para consolidar la inclusi&oacute;n social y productiva mediante la Ruta de Oportunidades Juveniles.
                    </div>

                </div>
            </div>

            <div class="content-section" id="flujo_datos">
                <div class="card">
                    <h2 class="card-title">Flujo de gesti&oacute;n de la informaci&oacute;n</h2>
                    <p style="color:#666; margin-bottom:20px;">Proceso de recolecci&oacute;n, registro y reporte de datos en el servicio Forjar Restaurativo.</p>

                    <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:25px;">
                        <span style="display:inline-block; padding:4px 12px; border-radius:15px; background:var(--accent-bg); color:var(--accent); font-size:0.8rem; font-weight:600;">Equipo psicosocial</span>
                        <span style="display:inline-block; padding:4px 12px; border-radius:15px; background:#e8ecf1; color:#3A3A3A; font-size:0.8rem; font-weight:600;">Enlace CESPA</span>
                        <span style="display:inline-block; padding:4px 12px; border-radius:15px; background:var(--accent-border); color:var(--accent); font-size:0.8rem; font-weight:600;">Referente t&eacute;cnico</span>
                    </div>

                    <div style="position:relative; padding-left:30px;">
                        <div style="position:absolute; left:12px; top:0; bottom:0; width:3px; background:linear-gradient(to bottom, var(--accent), #2F3E3C); border-radius:2px;"></div>

                        <div style="position:relative; margin-bottom:25px;">
                            <div style="position:absolute; left:-24px; top:4px; width:14px; height:14px; background:var(--accent); border-radius:50%; border:3px solid var(--accent-bg);"></div>
                            <h3 style="font-size:1rem; color:var(--accent); margin:0 0 6px;">1. Ingreso y acogida</h3>
                            <span style="display:inline-block; padding:2px 8px; border-radius:10px; font-size:0.7rem; background:var(--accent-bg); color:var(--accent); margin-bottom:6px;">Equipo psicosocial</span>
                            <p style="font-size:0.88rem; color:#555; line-height:1.6; margin:0;">Durante el ingreso, la equipo psicosocial (psicolog&iacute;a y trabajo social) realiza la acogida mediante entrevista. Se generan dos registros: el diligenciamiento de la <strong>ficha SIRBE</strong> y la toma de datos en la <strong>Valija Estandarizada</strong>. Se capturan variables b&aacute;sicas (edad, sexo, educaci&oacute;n), transversales (pertenencia &eacute;tnica, discapacidad), de ubicaci&oacute;n geogr&aacute;fica, din&aacute;micas familiares y variables espec&iacute;ficas sobre la remisi&oacute;n judicial y el delito.</p>
                        </div>

                        <div style="position:relative; margin-bottom:25px;">
                            <div style="position:absolute; left:-24px; top:4px; width:14px; height:14px; background:var(--accent); border-radius:50%; border:3px solid var(--accent-bg);"></div>
                            <h3 style="font-size:1rem; color:var(--accent); margin:0 0 6px;">2. Instrumentos de captura</h3>
                            <span style="display:inline-block; padding:2px 8px; border-radius:10px; font-size:0.7rem; background:var(--accent-bg); color:var(--accent); margin-bottom:6px;">Equipo psicosocial</span>
                            <p style="font-size:0.88rem; color:#555; line-height:1.6; margin:0 0 8px;"><strong>Fichas SIRBE:</strong> la informaci&oacute;n se consigna en dos formatos estandarizados de la SDIS: el formato de informaci&oacute;n b&aacute;sica y transversal (FOR-PSS-321) y el formato de variables espec&iacute;ficas del servicio Forjar (FOR-PSS-694).</p>
                            <p style="font-size:0.88rem; color:#555; line-height:1.6; margin:0;"><strong>Valija Estandarizada:</strong> base de datos en Excel utilizada internamente por cada unidad operativa. Recopila datos b&aacute;sicos y transversales, asigna un n&uacute;mero de &ldquo;Historia Social&rdquo; para el archivo f&iacute;sico e incluye variables de contraste para verificar la consistencia y calidad de la informaci&oacute;n antes de subirla al sistema oficial.</p>
                        </div>

                        <div style="position:relative; margin-bottom:25px;">
                            <div style="position:absolute; left:-24px; top:4px; width:14px; height:14px; background:var(--accent); border-radius:50%; border:3px solid var(--accent-bg);"></div>
                            <h3 style="font-size:1rem; color:var(--accent); margin:0 0 6px;">3. Digitalizaci&oacute;n en SIRBE WEB</h3>
                            <span style="display:inline-block; padding:2px 8px; border-radius:10px; font-size:0.7rem; background:#e8ecf1; color:#3A3A3A; margin-bottom:6px;">Enlace CESPA / Equipo psicosocial</span>
                            <p style="font-size:0.88rem; color:#555; line-height:1.6; margin:0;">Una vez consolidada la informaci&oacute;n en fichas f&iacute;sicas y Valija Estandarizada, se realiza el cargue al aplicativo <strong>SIRBE WEB</strong> (Sistema de Informaci&oacute;n Misional). All&iacute; queda el estado actualizado de cada usuario: ingresos, seguimientos, incumplimientos de sanci&oacute;n y egresos.</p>
                        </div>

                        <div style="position:relative; margin-bottom:10px;">
                            <div style="position:absolute; left:-24px; top:4px; width:14px; height:14px; background:var(--accent); border-radius:50%; border:3px solid var(--accent-bg);"></div>
                            <h3 style="font-size:1rem; color:var(--accent); margin:0 0 6px;">4. Controles de calidad y reportes</h3>
                            <span style="display:inline-block; padding:2px 8px; border-radius:10px; font-size:0.7rem; background:var(--accent-border); color:var(--accent); margin-bottom:6px;">Referente t&eacute;cnico</span>
                            <p style="font-size:0.88rem; color:#555; line-height:1.6; margin:0 0 8px;">El proceso est&aacute; regulado por manuales que definen los roles de &ldquo;recolector&rdquo;, &ldquo;cr&iacute;tico&rdquo; y &ldquo;digitador&rdquo;. Los referentes t&eacute;cnicos revisan mensualmente los datos para ajustes previos a los reportes.</p>
                            <p style="font-size:0.88rem; color:#555; line-height:1.6; margin:0 0 8px;">El tratamiento de datos personales es estrictamente confidencial y se rige por la Ley Estatutaria 1581 de 2012.</p>
                            <p style="font-size:0.88rem; color:#555; line-height:1.6; margin:0;">La informaci&oacute;n depurada sirve como insumo para preparar mensualmente el <strong>Informe Cualitativo y Cuantitativo del Servicio Forjar Restaurativo</strong>, que visibiliza el volumen de atenciones, cumplimiento de metas y avance del modelo.</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section" id="datos_sirbe">
                <div class="card">
                    <h2 class="card-title">Datos SIRBE</h2>
                    <p style="color:#666; margin-bottom:20px;">C&oacute;mo se estructura el servicio Forjar Restaurativo dentro del sistema de informaci&oacute;n misional SIRBE.</p>

                    <h3 class="card-subtitle">Tipolog&iacute;a y entrada al servicio</h3>
                    <p style="line-height:1.7;">Forjar funciona en SIRBE bajo la tipolog&iacute;a de <strong>&ldquo;servicio social&rdquo;</strong>. Los j&oacute;venes ingresan remitidos por juzgados o por el ICBF, llegan con una historia social, y el primer paso siempre es diligenciar la ficha SIRBE f&iacute;sica espec&iacute;fica para registrar sus datos transversales.</p>

                    <h3 class="card-subtitle">Seguimiento a largo plazo</h3>
                    <p style="line-height:1.7;">Debido a que los j&oacute;venes ingresan para cumplir una sanci&oacute;n, su permanencia en el servicio toma un tiempo prudente. Las modalidades y actuaciones est&aacute;n dise&ntilde;adas para que los j&oacute;venes sigan una ruta, de modo que SIRBE registra todo su historial de movimientos.</p>

                    <h3 class="card-subtitle">Estados adaptados al sistema penal</h3>
                    <p style="line-height:1.7;">A diferencia de otros servicios, Forjar no maneja actuaciones de &ldquo;intervenci&oacute;n&rdquo;. Maneja tres actuaciones de estado:</p>
                    <ul style="margin:10px 0 15px 20px; line-height:2;">
                        <li><span class="badge badge-primary">En atenci&oacute;n</span> El joven se encuentra cumpliendo su sanci&oacute;n o medida activamente</li>
                        <li><span class="badge badge-primary">Egresado</span> El joven ha finalizado el cumplimiento de su sanci&oacute;n</li>
                        <li><span class="badge badge-primary">En incumplimiento</span> Funciona en la pr&aacute;ctica como un estado &ldquo;suspendido&rdquo;, pero se cre&oacute; con este nombre espec&iacute;fico para no generar confusiones con la terminolog&iacute;a oficial del SRPA</li>
                    </ul>

                    <h3 class="card-subtitle">Uso del estado de seguimiento</h3>
                    <p style="line-height:1.7;">Este estado se utiliza exclusivamente en dos situaciones: cuando hay un <strong>traslado</strong> del joven de una unidad operativa a otra (por cambio de residencia, riesgos de amenazas o por orden de la autoridad competente), o cuando el juez determina un <strong>cambio en la submodalidad</strong> de la sanci&oacute;n.</p>
                </div>
            </div>"""

    generar_pagina_servicio(
        titulo="Servicio Forjar Restaurativo",
        subtitulo="Subdirecci&oacute;n para la Juventud | SDIS",
        sidebar_html=sidebar,
        contenido_html=contenido,
        archivo="gestion_conocimiento_forjar_2025.html",
        logo_img="imagenes/servicios/forjar.png",
        color_key="forjar",
    )


# =====================================================================
# 4. ALERTAS
# =====================================================================
def generar_alertas():
    sidebar = """
            <div class="sidebar-section">
                <div class="sidebar-title active" onclick="toggleSection(this)">
                    <span>Contexto</span><span class="arrow">&#9654;</span>
                </div>
                <div class="sidebar-items show">
                    <div class="sidebar-item" onclick="showContent('descripcion')">Descripci&oacute;n del equipo</div>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-title" onclick="toggleSection(this)">
                    <span>Protocolos</span><span class="arrow">&#9654;</span>
                </div>
                <div class="sidebar-items">
                    <div class="sidebar-item" onclick="showContent('protocolos')">Protocolos de atenci&oacute;n</div>
                </div>
            </div>"""

    contenido = f"""
            <div class="content-section active" id="welcome">
                <div class="welcome-section">
                    <h2>Parche seguro</h2>
                    <p>Sistema de identificaci&oacute;n y seguimiento de alertas tempranas para la protecci&oacute;n integral de la poblaci&oacute;n joven. A partir del triage psicosocial, el equipo identifica situaciones de riesgo y activa los protocolos de atenci&oacute;n correspondientes.</p>
                </div>
            </div>

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
            </div>

            <div class="content-section" id="protocolos">
                <div class="card">
                    <h2 class="card-title">Protocolos de atenci&oacute;n</h2>
                    <p>La estrategia cuenta con <strong>m&aacute;s de 10 protocolos</strong> de atenci&oacute;n, cada uno con un procedimiento espec&iacute;fico. Referente: <strong>Paula</strong>.</p>
                    <p>Para cada protocolo se incluye: t&iacute;tulo, rese&ntilde;a corta y enlace al documento completo.</p>
                </div>
            </div>"""

    generar_pagina_servicio(
        titulo="Parche seguro",
        subtitulo="Subdirecci&oacute;n para la Juventud | SDIS",
        sidebar_html=sidebar,
        contenido_html=contenido,
        archivo="gestion_conocimiento_alertas_2025.html",
        logo_img="imagenes/servicios/alertas.png",
        color_key="alertas",
    )


# =====================================================================
# Ejecutar todo
# =====================================================================
if __name__ == "__main__":
    print("Generando páginas del gestor de conocimiento...\n")
    generar_index()
    generar_jco()
    generar_forjar()
    generar_alertas()
    print("\nListo. Todos los archivos generados.")
