# -*- coding: utf-8 -*-
"""
Genera el archivo gestion_conocimiento_jco_2025.html
para el gestor de conocimiento de Jóvenes con Oportunidades.

Cada sección del HTML se almacena como variable de Python
para facilitar la edición de contenido sin tocar HTML crudo.
"""

import os
import sys

# CSS compartido con los demás generadores
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _comun.estilos import css_para
# ============================================================
# 1. CSS — estilos del gestor
# ============================================================

CSS = css_para("jco")

# ============================================================
# 2. Encabezado (header)
# ============================================================

HEADER = """\
    <header class="header">
        <div>
            <h1>Gestor de conocimiento - J&oacute;venes con Oportunidades</h1>
            <div class="subtitle">Subdirecci&oacute;n para la Juventud | SDIS</div>
        </div>
        <div class="header-btns">
            <a class="home-btn" href="index.html" title="Todos los servicios">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8F4E1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
            </a>
            <div class="home-btn" onclick="showContent('welcome')" title="Inicio J&oacute;venes con Oportunidades">
                <img src="imagenes/servicios/jovenes-con-oportunidades.png" alt="J&oacute;venes con Oportunidades" style="height:32px; border-radius:16px; object-fit:contain; vertical-align:middle;">
            </div>
        </div>
    </header>"""

# ============================================================
# 3. Barra lateral (sidebar)
# ============================================================

SIDEBAR = """\
        <nav class="sidebar">
            <div class="sidebar-title" onclick="showContent('welcome')" style="cursor:pointer;"><span>Inicio</span></div>

            <div class="sidebar-section">
                <div class="sidebar-title active" onclick="toggleSection(this)">
                    <span>Contexto</span><span class="arrow">&#9654;</span>
                </div>
                <div class="sidebar-items show">
                    <div class="sidebar-item" onclick="showContent('antecedentes')">Antecedentes y transformaci&oacute;n</div>
                    <div class="sidebar-item" onclick="showContent('pilares')">Pilares del programa</div>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-title" onclick="showContent('estadisticas')" style="cursor:pointer;">
                    <span>Estad&iacute;sticas</span>
                </div>
            </div>
        </nav>"""

# ============================================================
# 4. Secciones de contenido
#    Cada sección es una variable independiente para editar
#    sin afectar las demás.
# ============================================================

# --- Bienvenida ---
SECCION_WELCOME = """\
            <div class="content-section active" id="welcome">
                <div class="welcome-section">
                    <h2>J&oacute;venes con Oportunidades</h2>
                    <p>Ruta de inclusi&oacute;n social y productiva de la Alcald&iacute;a de Bogot&aacute; para empoderar a j&oacute;venes de 14 a 28 a&ntilde;os en situaci&oacute;n de pobreza extrema, moderada o vulnerabilidad, especialmente aquellos que no estudian ni trabajan.</p>
                    <p>Iniciativa conjunta entre la Secretar&iacute;a de Integraci&oacute;n Social, la Secretar&iacute;a de Desarrollo Econ&oacute;mico, la Secretar&iacute;a de Educaci&oacute;n y la Agencia Atenea.</p>
                    <div style="margin:30px auto 0; max-width:450px;">
                        <img src="imagenes/Jovenes con oportunidades.png" alt="J&oacute;venes con Oportunidades" style="width:100%; border-radius:12px; box-shadow:0 4px 15px rgba(0,0,0,0.1);">
                    </div>
                </div>
            </div>"""

# --- Antecedentes ---
SECCION_ANTECEDENTES = """\
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
            </div>"""

# --- Pilares ---
SECCION_PILARES = """\
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
            </div>"""


# --- Estadísticas ---
SECCION_ESTADISTICAS = """\
            <div class="content-section" id="estadisticas">
                <div class="card">
                    <h2 class="card-title">Estad&iacute;sticas 2025</h2>
                    <iframe title="Seguimiento t&eacute;cnico" width="100%" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiMzRiNWRkMDQtNThmNC00Yzk5LThjNTItOWI4MzZkYzYwM2EzIiwidCI6ImIzZTMwODA4LWU5YTgtNGYyYS05YmMxLWE3NjBhZTkxMGNmNSIsImMiOjR9" frameborder="0" allowFullScreen="true" style="border:1px solid #e0e0e0; border-radius:8px;"></iframe>
                </div>
            </div>"""

# ============================================================
# 5. JavaScript — navegación del sidebar
# ============================================================

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

# ============================================================
# 6. Ensamblaje — une todas las piezas en el HTML final
# ============================================================

def generar_html():
    """Arma el documento HTML completo a partir de las variables."""

    # Se unen todas las secciones de contenido en orden
    secciones = "\n\n".join([
        SECCION_WELCOME,
        SECCION_ANTECEDENTES,
        SECCION_PILARES,
        SECCION_ESTADISTICAS,
    ])

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestor de conocimiento - J&oacute;venes con Oportunidades</title>
    <style>
{CSS}</style>
</head>
<body>
{HEADER}
    <div class="container">
{SIDEBAR}
        <main class="main-content">

{secciones}
        </main>
    </div>
    <script>
{JAVASCRIPT}
</script>
</body>
</html>
"""
    return html


# ============================================================
# 7. Escritura del archivo
# ============================================================

if __name__ == "__main__":
    # Raíz del proyecto (un nivel arriba de scripts/)
    directorio = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    archivo_salida = os.path.join(directorio, "gestion_conocimiento_jco_2025.html")

    html = generar_html()

    with open(archivo_salida, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Archivo generado: {archivo_salida}")
