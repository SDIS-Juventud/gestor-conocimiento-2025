# Genera el home (index.html) y las páginas placeholder de cada servicio
# de la Subdirección para la Juventud.
# Todos comparten el mismo CSS base y estructura de navegación.

import os

BASE = os.path.dirname(os.path.abspath(__file__))

# --- Iframe de Power BI (mismo para todos los servicios) ---
POWERBI_SRC = "https://app.powerbi.com/view?r=eyJrIjoiMzRiNWRkMDQtNThmNC00Yzk5LThjNTItOWI4MzZkYzYwM2EzIiwidCI6ImIzZTMwODA4LWU5YTgtNGYyYS05YmMxLWE3NjBhZTkxMGNmNSIsImMiOjR9"

# =====================================================================
# CSS compartido (mismo estilo que Casas de Juventud)
# =====================================================================
CSS_BASE = """
@import url('https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&display=swap');
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Figtree', 'Segoe UI', sans-serif; background-color: #ffffff; color: #2F3E3C; }
.header { background: #2F3E3C; color: #F8F4E1; padding: 20px 30px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.15); }
.header h1 { font-size: 1.5rem; font-weight: 700; } .header .subtitle { font-size: 0.9rem; opacity: 0.85; }
.header-btns { display: flex; align-items: center; gap: 15px; }
.home-btn { font-size: 1.5rem; cursor: pointer; padding: 5px 12px; border-radius: 8px; transition: background 0.2s; text-decoration: none; color: #F8F4E1; }
.home-btn:hover { background: rgba(255,255,255,0.15); }
.container { display: flex; min-height: calc(100vh - 80px); }
.sidebar { width: 280px; background: #fff; border-right: 1px solid #e0e0e0; padding: 20px 0; overflow-y: auto; }
.sidebar-section { margin-bottom: 10px; }
.sidebar-title { padding: 12px 20px; font-weight: 600; color: #663A93; cursor: pointer; display: flex; justify-content: space-between; align-items: center; transition: background 0.2s; }
.sidebar-title:hover { background: #f5f0fa; }
.sidebar-title .arrow { transition: transform 0.2s; }
.sidebar-title.active .arrow { transform: rotate(90deg); }
.sidebar-items { display: none; padding-left: 20px; }
.sidebar-items.show { display: block; }
.sidebar-item { padding: 10px 20px; cursor: pointer; font-size: 0.9rem; color: #3A3A3A; border-left: 3px solid transparent; transition: all 0.2s; }
.sidebar-item:hover { background: #f5f0fa; border-left-color: #663A93; }
.sidebar-item.active { background: #ede7f6; border-left-color: #663A93; color: #663A93; font-weight: 600; }
.sidebar-link { display: block; padding: 12px 20px; font-weight: 600; color: #663A93; text-decoration: none; transition: background 0.2s; }
.sidebar-link:hover { background: #f5f0fa; }
.main-content { flex: 1; padding: 30px; overflow-y: auto; }
.content-section { display: none; }
.content-section.active { display: block; }
.card { background: white; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); padding: 25px; margin-bottom: 20px; }
.card-title { font-size: 1.4rem; color: #663A93; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 2px solid #ede7f6; }
.card-subtitle { font-size: 1.15rem; color: #6B4FA0; font-weight: 500; margin: 25px 0 10px 0; }
.card p { margin-bottom: 15px; }
.badge { display: inline-block; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 500; margin-right: 8px; margin-bottom: 8px; }
.badge-primary { background: #ede7f6; color: #663A93; }
.badge-warning { background: #FFF3E0; color: #F58B53; }
.badge-info { background: #e0f4f5; color: #1E9DA3; }
.welcome-section { text-align: center; padding: 60px 20px; }
.welcome-section h2 { font-size: 2rem; color: #663A93; margin-bottom: 20px; }
.welcome-section p { font-size: 1.1rem; color: #666; max-width: 700px; margin: 0 auto 20px; line-height: 1.7; }
.methodology-box { background: #f5f0fa; border-left: 4px solid #663A93; padding: 15px 20px; margin: 15px 0; border-radius: 0 8px 8px 0; }
.pending-box { background: #FFF3E0; border-left: 4px solid #F58B53; padding: 15px 20px; margin: 15px 0; border-radius: 0 8px 8px 0; color: #8B5E3C; }
/* Línea de tiempo */
.timeline { position: relative; padding-left: 30px; margin: 20px 0; }
.timeline::before { content: ''; position: absolute; left: 8px; top: 0; bottom: 0; width: 3px; background: #ede7f6; }
.timeline-item { position: relative; margin-bottom: 25px; }
.timeline-item::before { content: ''; position: absolute; left: -26px; top: 4px; width: 12px; height: 12px; border-radius: 50%; background: #663A93; border: 3px solid #ede7f6; }
.timeline-year { font-weight: 700; color: #663A93; font-size: 1rem; }
.timeline-text { color: #555; font-size: 0.9rem; margin-top: 4px; line-height: 1.5; }
@media (max-width: 768px) { .container { flex-direction: column; } .sidebar { width: 100%; border-right: none; border-bottom: 1px solid #e0e0e0; } }
"""

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
def generar_pagina_servicio(titulo, subtitulo, sidebar_html, contenido_html, archivo, logo_img=""):
    """Genera un HTML con la estructura estándar del gestor."""
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestor de conocimiento - {titulo}</title>
    <style>{CSS_BASE}</style>
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
            "nombre": "Alertas",
            "archivo": "gestion_conocimiento_alertas_2025.html",
            "imagen": "imagenes/servicios/alertas.png",
            "desc": "Sistema de identificaci&oacute;n y seguimiento de alertas tempranas para la protecci&oacute;n integral de la poblaci&oacute;n joven.",
            "badge": "soon",
        },
    ]

    # Colores de acento por servicio (borde hover)
    # Azul rey, lila, azul claro (forjar), rojo claro (alertas)
    colores = ["#1a237e", "#663A93", "#80cbc4", "#e57373"]

    tarjetas = ""
    for i, s in enumerate(servicios):
        badge_class = "badge-active" if s["badge"] == "active" else "badge-soon"
        badge_text = "Activo" if s["badge"] == "active" else "Pr&oacute;ximamente"
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
            background: #FFF3E0; color: #E07850;
        }}
        .badge-active {{
            display: inline-block; margin-top: 14px; padding: 5px 16px;
            border-radius: 20px; font-size: 0.72rem; font-weight: 600;
            background: #e6f9f0; color: #1EAE76;
        }}

        /* Footer */
        .footer {{ text-align: center; padding: 35px 30px; color: #bbb; font-size: 0.82rem; }}

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
            <h2>Servicios</h2>
            <p>Documentaci&oacute;n de procesos, datos y gesti&oacute;n del conocimiento de cada servicio de la Subdirecci&oacute;n para la Juventud.</p>
        </div>
        <div class="services-grid">
{tarjetas}
        </div>
    </main>
    <footer class="footer">
        Subdirecci&oacute;n para la Juventud &middot; Secretar&iacute;a Distrital de Integraci&oacute;n Social &middot; Bogot&aacute; D.C.
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
                    <div class="sidebar-item" onclick="showContent('estructura')">Estructura del programa</div>
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
                    <p>Programa de la Subdirecci&oacute;n para la Juventud que ofrece formaci&oacute;n, apoyo psicosocial, transferencias monetarias condicionadas y acompa&ntilde;amiento laboral para j&oacute;venes de 14 a 28 a&ntilde;os en condici&oacute;n de vulnerabilidad.</p>
                    <p>Opera a trav&eacute;s de tres componentes: acompa&ntilde;amiento psicosocial, rutas de formaci&oacute;n y orientaci&oacute;n laboral.</p>
                </div>
            </div>

            <div class="content-section" id="antecedentes">
                <div class="card">
                    <h2 class="card-title">Antecedentes y transformaci&oacute;n</h2>
                    <p>El programa actual <strong>J&oacute;venes con Oportunidades</strong> es la evoluci&oacute;n de lo que anteriormente se conoc&iacute;a como <strong>&ldquo;Parceros por Bogot&aacute;&rdquo;</strong>.</p>

                    <h3 class="card-subtitle">Antes: Parceros por Bogot&aacute;</h3>
                    <p>El programa exig&iacute;a a los j&oacute;venes realizar <strong>servicio social</strong> como contraprestaci&oacute;n: actividades como limpieza de parques, apoyo log&iacute;stico en eventos y labores comunitarias. Los j&oacute;venes recib&iacute;an transferencias monetarias condicionadas de $500.000 por 6 meses.</p>

                    <h3 class="card-subtitle">Hoy: J&oacute;venes con Oportunidades</h3>
                    <p>El servicio social ya no existe. El programa actual se centra en <strong>intermediaci&oacute;n laboral</strong> y opera bajo <strong>tres rutas</strong>:</p>
                    <ul style="margin:10px 0 15px 20px; line-height:1.8;">
                        <li><strong>Acompa&ntilde;amiento psicosocial:</strong> formaci&oacute;n en proyecto de vida e identificaci&oacute;n de alertas</li>
                        <li><strong>Rutas de formaci&oacute;n:</strong> educaci&oacute;n media, cursos cortos (hasta 160 horas), educaci&oacute;n posmedia</li>
                        <li><strong>Orientaci&oacute;n laboral:</strong> registro en servicio p&uacute;blico de empleo, plataforma Talento Capital, intermediaci&oacute;n</li>
                    </ul>
                </div>
            </div>

            <div class="content-section" id="estructura">
                <div class="card">
                    <h2 class="card-title">Estructura del programa</h2>
                    <p>El servicio se divide en dos grandes bloques:</p>
                    <div class="methodology-box">
                        <strong>Proyecto de vida:</strong> 7 m&oacute;dulos espec&iacute;ficos que trabajan el desarrollo personal y las capacidades de los j&oacute;venes.
                    </div>
                    <div class="methodology-box">
                        <strong>Componente psicosocial:</strong> triage psicosocial para clasificar el nivel de riesgo de cada joven y activar rutas de atenci&oacute;n.
                    </div>
                    <div class="pending-box">
                        Pendiente: completar detalle de los componentes con informaci&oacute;n del equipo operativo.
                    </div>
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
                    <div class="pending-box">
                        Pendiente: confirmar nombres de los m&oacute;dulos 4 a 7 y agregar descripciones y enlaces a manuales.
                    </div>
                </div>
            </div>

            <div class="content-section" id="triage">
                <div class="card">
                    <h2 class="card-title">Triage psicosocial</h2>
                    <p>El componente psicosocial realiza un <strong>triage</strong> al ingreso de cada joven al programa. El equipo profesional clasifica el nivel de riesgo y activa las rutas de atenci&oacute;n correspondientes.</p>
                    <div class="pending-box">
                        Pendiente: describir el proceso de triage, niveles de riesgo y rutas de activaci&oacute;n.
                    </div>
                </div>
            </div>

            <div class="content-section" id="enlaces">
                <div class="card">
                    <h2 class="card-title">Manuales y gu&iacute;as oficiales</h2>
                    <p>Enlaces directos a los documentos de consulta para cada m&oacute;dulo del programa.</p>
                    <div class="pending-box">
                        Pendiente: agregar links a manuales, anexos y gu&iacute;as oficiales de cada m&oacute;dulo.
                    </div>
                </div>
            </div>"""

    generar_pagina_servicio(
        titulo="J&oacute;venes con Oportunidades",
        subtitulo="Subdirecci&oacute;n para la Juventud | J&oacute;venes con Oportunidades | 2025",
        sidebar_html=sidebar,
        contenido_html=contenido,
        archivo="gestion_conocimiento_jco_2025.html",
        logo_img="imagenes/servicios/jovenes-con-oportunidades.png",
    )


# =====================================================================
# 3. SERVICIO FORJAR RESTAURATIVO
# =====================================================================
def generar_forjar():
    sidebar = """
            <div class="sidebar-section">
                <div class="sidebar-title active" onclick="toggleSection(this)">
                    <span>Contexto</span><span class="arrow">&#9654;</span>
                </div>
                <div class="sidebar-items show">
                    <div class="sidebar-item" onclick="showContent('linea_tiempo')">L&iacute;nea de tiempo</div>
                    <div class="sidebar-item" onclick="showContent('cambio_discursivo')">Cambio discursivo</div>
                    <div class="sidebar-item" onclick="showContent('modalidades')">Modalidades de atenci&oacute;n</div>
                </div>
            </div>"""

    contenido = f"""
            <div class="content-section active" id="welcome">
                <div class="welcome-section">
                    <h2>Servicio Forjar Restaurativo</h2>
                    <p>Servicio de la Subdirecci&oacute;n para la Juventud dirigido a adolescentes y j&oacute;venes de 14 a 28 a&ntilde;os vinculados al Sistema de Responsabilidad Penal para Adolescentes (SRPA). Ofrece acompa&ntilde;amiento integral con enfoque restaurativo, priorizando sanciones no privativas de libertad y el acompa&ntilde;amiento en el medio sociofamiliar.</p>
                    <p>Opera en tres unidades operativas ubicadas en las localidades de Suba, Ciudad Bol&iacute;var y Rafael Uribe Uribe.</p>
                </div>
            </div>

            <div class="content-section" id="linea_tiempo">
                <div class="card">
                    <h2 class="card-title">L&iacute;nea de tiempo</h2>
                    <div class="timeline">
                        <div class="timeline-item">
                            <div class="timeline-year">~2012</div>
                            <div class="timeline-text">Nace el servicio como <strong>&ldquo;Centros Forjar&rdquo;</strong>. Originalmente no pertenec&iacute;a a la Subdirecci&oacute;n para la Juventud sino a otra dependencia de la SDIS.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">Administraci&oacute;n anterior</div>
                            <div class="timeline-text">Forjar es incorporado a la Subdirecci&oacute;n para la Juventud, consolidando la atenci&oacute;n a j&oacute;venes del SRPA dentro de la oferta de servicios de juventud.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">Administraci&oacute;n actual</div>
                            <div class="timeline-text">Se adopta el nombre <strong>&ldquo;Servicio Forjar Restaurativo&rdquo;</strong>, eliminando la palabra &ldquo;centro&rdquo;. Se fortalece el enfoque restaurativo y el acompa&ntilde;amiento sociofamiliar.</div>
                        </div>
                    </div>
                    <div class="pending-box">
                        Pendiente: completar hitos intermedios y fechas espec&iacute;ficas con el equipo de Forjar.
                    </div>
                </div>
            </div>

            <div class="content-section" id="cambio_discursivo">
                <div class="card">
                    <h2 class="card-title">Cambio discursivo</h2>
                    <p>El servicio antes se conoc&iacute;a como <strong>&ldquo;Centros Forjar&rdquo;</strong>. La palabra <strong>&ldquo;centro&rdquo;</strong> fue eliminada porque los j&oacute;venes la asociaban con <strong>centros de reclusi&oacute;n</strong>, generando una connotaci&oacute;n negativa que iba en contra del enfoque restaurativo del programa.</p>
                    <div class="methodology-box">
                        <strong>Referencia correcta:</strong> usar siempre <strong>&ldquo;servicio Forjar&rdquo;</strong> o <strong>&ldquo;servicio Forjar Restaurativo&rdquo;</strong>. Nunca &ldquo;Centro Forjar&rdquo;.
                    </div>
                </div>
            </div>

            <div class="content-section" id="modalidades">
                <div class="card">
                    <h2 class="card-title">Modalidades de atenci&oacute;n</h2>
                    <p>El servicio ofrece acompa&ntilde;amiento en las siguientes modalidades:</p>
                    <ul style="margin:10px 0 15px 20px; line-height:2;">
                        <li><span class="badge badge-primary">Libertad asistida y/o vigilada</span></li>
                        <li><span class="badge badge-primary">Prestaci&oacute;n de servicios a la comunidad</span></li>
                        <li><span class="badge badge-info">IARAJ</span> Intervenci&oacute;n de apoyo al restablecimiento en administraci&oacute;n de justicia</li>
                        <li><span class="badge badge-info">RIAJ</span> Ruta integral de atenci&oacute;n para j&oacute;venes</li>
                        <li><span class="badge badge-warning">Post-egreso</span> Estrategia voluntaria de acompa&ntilde;amiento</li>
                    </ul>
                    <div class="pending-box">
                        Pendiente: describir en detalle cada modalidad con el equipo de Forjar.
                    </div>
                </div>
            </div>"""

    generar_pagina_servicio(
        titulo="Servicio Forjar Restaurativo",
        subtitulo="Subdirecci&oacute;n para la Juventud | Servicio Forjar Restaurativo | 2025",
        sidebar_html=sidebar,
        contenido_html=contenido,
        archivo="gestion_conocimiento_forjar_2025.html",
        logo_img="imagenes/servicios/forjar.png",
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
                    <h2>Estrategia de Alertas</h2>
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
                    <div class="pending-box">
                        Pendiente: completar descripci&oacute;n del flujo de trabajo con la referente Paula.
                    </div>
                </div>
            </div>

            <div class="content-section" id="protocolos">
                <div class="card">
                    <h2 class="card-title">Protocolos de atenci&oacute;n</h2>
                    <p>La estrategia cuenta con <strong>m&aacute;s de 10 protocolos</strong> de atenci&oacute;n, cada uno con un procedimiento espec&iacute;fico. Referente: <strong>Paula</strong>.</p>
                    <p>Para cada protocolo se incluye: t&iacute;tulo, rese&ntilde;a corta y enlace al documento completo.</p>
                    <div class="pending-box">
                        Pendiente: Paula debe proveer la lista de protocolos con sus documentos para completar esta secci&oacute;n.
                    </div>
                </div>
            </div>"""

    generar_pagina_servicio(
        titulo="Alertas",
        subtitulo="Subdirecci&oacute;n para la Juventud | Estrategia de Alertas | 2025",
        sidebar_html=sidebar,
        contenido_html=contenido,
        archivo="gestion_conocimiento_alertas_2025.html",
        logo_img="imagenes/servicios/alertas.png",
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
