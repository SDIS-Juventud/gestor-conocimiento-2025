# -*- coding: utf-8 -*-
"""
Genera el archivo gestion_conocimiento_jco_2025.html
para el gestor de conocimiento de Jóvenes con Oportunidades.

Cada sección del HTML se almacena como variable de Python
para facilitar la edición de contenido sin tocar HTML crudo.
"""

import os
import sys

# CSS y datos compartidos con los demás generadores
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _comun.estilos import css_para
from _comun.aliados import seccion_jco as seccion_aliados_jco
# ============================================================
# 1. CSS — estilos del gestor
# ============================================================

# Las reglas para .modulo-acordeon viven en _comun/estilos.py porque
# ahora se comparten con el generador de Forjar.
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
                    <div class="sidebar-item" onclick="showContent('linea_tiempo')">L&iacute;nea de tiempo</div>
                    <div class="sidebar-item" onclick="showContent('a_tener_en_cuenta')">A tener en cuenta</div>
                    <div class="sidebar-item" onclick="showContent('equipo')">Equipo</div>
                    <div class="sidebar-item" onclick="showContent('pilares')">Pilares del programa</div>
                    <div class="sidebar-item" onclick="showContent('modulos_proyecto_vida')">M&oacute;dulos de Proyecto de Vida</div>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-title" onclick="toggleSection(this)">
                    <span>Gesti&oacute;n de datos</span><span class="arrow">&#9654;</span>
                </div>
                <div class="sidebar-items">
                    <div class="sidebar-item" onclick="showContent('flujo_datos')">Flujo de gesti&oacute;n de la informaci&oacute;n</div>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-title" onclick="showContent('aliados')" style="cursor:pointer;">
                    <span>Aliados</span>
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
                    <div style="font-family:'Anton','Figtree',sans-serif; font-weight:400; font-size:1.9rem; line-height:1.05; letter-spacing:1px; text-transform:uppercase; background:#2d2a28; color:#f4f5de; padding:14px 24px 11px; margin:0 auto 28px; display:block; width:fit-content; max-width:100%; text-align:center;">J&oacute;venes con Oportunidades</div>
                    <p>Ruta de inclusi&oacute;n social y productiva de la Alcald&iacute;a de Bogot&aacute; para empoderar a j&oacute;venes de 14 a 28 a&ntilde;os en situaci&oacute;n de pobreza extrema, moderada o vulnerabilidad, especialmente aquellos que no estudian ni trabajan.</p>
                    <p>Iniciativa conjunta entre la Secretar&iacute;a de Integraci&oacute;n Social, la Secretar&iacute;a de Desarrollo Econ&oacute;mico, la Secretar&iacute;a de Educaci&oacute;n y la Agencia Atenea.</p>
                    <div style="margin:30px auto 0; max-width:450px;">
                        <img src="imagenes/Jovenes con oportunidades.png" alt="J&oacute;venes con Oportunidades" style="width:100%; border-radius:12px; box-shadow:0 4px 15px rgba(0,0,0,0.1);">
                    </div>
                </div>
            </div>"""

# --- A tener en cuenta ---
SECCION_A_TENER_EN_CUENTA = """\
            <div class="content-section" id="a_tener_en_cuenta">
                <div class="card">
                    <h2 class="card-title">A tener en cuenta</h2>

                    <h3 class="card-subtitle">Los montos var&iacute;an seg&uacute;n la ruta de formaci&oacute;n</h3>
                    <p style="line-height:1.7;">Parceros entregaba una cuota fija de <strong>$500.000 mensuales durante 6 meses</strong>. En J&oacute;venes con Oportunidades el apoyo econ&oacute;mico depende de la ruta elegida: hasta <strong>$1.200.000 en cursos cortos</strong>, hasta <strong>$3.200.000</strong> en la ruta de educaci&oacute;n flexible para terminar el bachillerato (j&oacute;venes y adultos), y topes m&aacute;ximos que van desde <strong>$2.700.000</strong> (para nivel t&eacute;cnico y tecn&oacute;logo) hasta <strong>$4.300.000</strong> en educaci&oacute;n universitaria de ciclo largo.</p>
                    <p style="line-height:1.7;">En la ruta de <strong>EFT</strong> en particular, los recursos que pone la SDIS pueden llegar hasta <strong>3 salarios m&iacute;nimos</strong>, m&aacute;s <strong>3 pagos de $400.000</strong> y <strong>$300.000 por intermediaci&oacute;n</strong>.</p>

                    <h3 class="card-subtitle">Focalizaci&oacute;n y requisitos de ingreso</h3>
                    <p style="line-height:1.7;">Los criterios de selecci&oacute;n var&iacute;an entre ambos modelos. Parceros por Bogot&aacute; se enfocaba en j&oacute;venes &ldquo;Ninis&rdquo; (que ni estudian ni trabajan) de <strong>18 a 28 a&ntilde;os</strong>, identificados directamente en barrios vulnerables mediante una encuesta de 23 preguntas que calculaba su &Iacute;ndice de Vulnerabilidad Juvenil. Por su parte, el nuevo programa J&oacute;venes con Oportunidades atiende a j&oacute;venes de <strong>14 a 28 a&ntilde;os</strong> en situaci&oacute;n de pobreza extrema, moderada o vulnerabilidad por inseguridad alimentaria. Su focalizaci&oacute;n es distinta, ya que exige que los beneficiarios residan en Bogot&aacute; y est&eacute;n registrados oficialmente en el Sisb&eacute;n dentro de las categor&iacute;as <strong>A, B o hasta C09</strong>.</p>

                    <h3 class="card-subtitle">Financiaci&oacute;n de los programas</h3>
                    <p style="line-height:1.7;">Una caracter&iacute;stica clave de Parceros por Bogot&aacute; fue que se sustent&oacute;, en gran parte, gracias a la uni&oacute;n institucional con los <strong>Fondos de Desarrollo Local (FDL)</strong>. Esto permiti&oacute; una inversi&oacute;n territorializada, donde los alcaldes locales y ediles destinaban recursos para apoyar directamente a los j&oacute;venes de sus respectivas localidades. En J&oacute;venes con Oportunidades, los FDL tambi&eacute;n han venido aportando recursos: con un rol inicial <strong>desde 2025</strong> y una <strong>presencia muy fuerte en 2026</strong>. A estos aportes se suma la inversi&oacute;n distrital proyectada de <strong>$324.053 millones</strong>, que une los esfuerzos sectoriales de las Secretar&iacute;as de Integraci&oacute;n Social, Educaci&oacute;n, Desarrollo Econ&oacute;mico y la Agencia Atenea.</p>

                    <h3 class="card-subtitle">El cambio de paradigma en la condicionalidad</h3>
                    <p style="line-height:1.7;">En Parceros por Bogot&aacute;, la transferencia monetaria estaba condicionada a la participaci&oacute;n en actividades pedag&oacute;gicas y labores pr&aacute;cticas de servicio a la ciudad, tales como proyectos de embellecimiento, limpieza, huertas urbanas y &ldquo;Nuestras Zonas Seguras&rdquo;. Adem&aacute;s, los participantes se formaban y certificaban como Agentes Comunitarios de Prevenci&oacute;n en temas de salud mental, violencias y consumo de sustancias. Con J&oacute;venes con Oportunidades, la condicionalidad depende directamente del cumplimiento de actividades en tres componentes clave: el acompa&ntilde;amiento psicosocial transversal, el avance en la ruta de formaci&oacute;n elegida, y el proceso de intermediaci&oacute;n laboral.</p>

                    <h3 class="card-subtitle">Intermediaci&oacute;n laboral y conexi&oacute;n con el empleo</h3>
                    <p style="line-height:1.7;">En Parceros por Bogot&aacute; exist&iacute;a un componente de <strong>formaci&oacute;n educativa e inclusi&oacute;n laboral</strong> que se establec&iacute;a <strong>desde el inicio de la atenci&oacute;n</strong>, ofertando oportunidades a los participantes y permitiendo el cumplimiento de actividades condicionadas. En el nuevo modelo de J&oacute;venes con Oportunidades, la intermediaci&oacute;n se consolida como un <strong>tercer componente de la ruta</strong>, una etapa formal y estructural. El objetivo es garantizar la integralidad y que el joven &ldquo;salga por el &uacute;ltimo eslab&oacute;n&rdquo; con el resultado esperado. Por ello, al finalizar su formaci&oacute;n, la Secretar&iacute;a Distrital de Desarrollo Econ&oacute;mico asume el liderazgo directo de la intermediaci&oacute;n laboral, gestionando el registro en el Servicio P&uacute;blico de Empleo y en las plataformas de la estrategia &ldquo;Talento Capital&rdquo;.</p>
                </div>
            </div>"""

# --- Línea de tiempo ---
SECCION_LINEA_TIEMPO = """\
            <div class="content-section" id="linea_tiempo">
                <div class="card">
                    <h2 class="card-title">L&iacute;nea de tiempo</h2>
                    <p style="line-height:1.7; margin-bottom:20px;">Evoluci&oacute;n de las pol&iacute;ticas de inclusi&oacute;n social juvenil y transferencias monetarias en Bogot&aacute;: del modelo de emergencia <strong>Parceros por Bogot&aacute;</strong> hacia la estrategia integral <strong>J&oacute;venes con Oportunidades</strong>.</p>
                    <div class="timeline">
                        <div class="timeline-item">
                            <div class="timeline-year">2020</div>
                            <div class="timeline-text"><strong>Estrategia RETO.</strong> La SDIS lanza la Estrategia Retorno de las Oportunidades Juveniles &ndash; RETO, estructurada institucionalmente bajo el Proyecto de Inversi&oacute;n 7740 &ldquo;Generaci&oacute;n J&oacute;venes con Derechos en Bogot&aacute;&rdquo;, para reducir el riesgo social en poblaci&oacute;n joven vulnerable.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2021</div>
                            <div class="timeline-text"><strong>Lanzamiento de Parceros por Bogot&aacute;.</strong> El programa nace como respuesta a las demandas escuchadas en las mesas de di&aacute;logo y concertaci&oacute;n durante el estallido social y el Paro Nacional. Como parte de la Estrategia RETO, entrega a j&oacute;venes vulnerables transferencias de <strong>$500.000 mensuales durante seis meses</strong>. Este apoyo econ&oacute;mico est&aacute; condicionado a su participaci&oacute;n en actividades pedag&oacute;gicas, labores de servicio a la ciudad y acompa&ntilde;amiento psicosocial para apoyar su proyecto de vida.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2023 (septiembre)</div>
                            <div class="timeline-text"><strong>Cierre del ciclo Parceros por Bogot&aacute;.</strong> Al finalizar el programa se reportan <strong>m&aacute;s de 28.000 j&oacute;venes atendidos</strong>. <strong>4 de cada 10 egresados</strong> obtuvieron empleo formal, apoyo para emprendimiento o acceso a educaci&oacute;n superior.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2024</div>
                            <div class="timeline-text"><strong>Se lanza oficialmente el programa J&oacute;venes con Oportunidades.</strong> Este nuevo modelo, enmarcado t&eacute;cnica y presupuestalmente dentro del Proyecto de Inversi&oacute;n 7940 &ldquo;Implementaci&oacute;n de estrategias de inclusi&oacute;n social y productiva para la poblaci&oacute;n joven en situaci&oacute;n de pobreza y vulnerabilidad en Bogot&aacute;&rdquo;, mantiene el acompa&ntilde;amiento psicosocial y las transferencias monetarias condicionadas, pero ahora articula el esfuerzo de las Secretar&iacute;as de Integraci&oacute;n Social, Educaci&oacute;n y Desarrollo Econ&oacute;mico junto con la Agencia Atenea. Vincula el apoyo econ&oacute;mico directamente a tres rutas de formaci&oacute;n espec&iacute;fica.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2024 &ndash; 2027</div>
                            <div class="timeline-text"><strong>Meta del cuatrienio.</strong> J&oacute;venes con Oportunidades tiene el reto de beneficiar a <strong>40.000 j&oacute;venes</strong> con una inversi&oacute;n distrital proyectada de <strong>$324.053 millones</strong>.</div>
                        </div>
                    </div>
                </div>
            </div>"""

# --- Equipo ---
SECCION_EQUIPO = """\
            <div class="content-section" id="equipo">
                <div class="card">
                    <h2 class="card-title">Equipo y gesti&oacute;n de J&oacute;venes con Oportunidades</h2>
                    <p style="line-height:1.7;">El servicio J&oacute;venes con Oportunidades es un esfuerzo articulado entre la <strong>Secretar&iacute;a Distrital de Integraci&oacute;n Social (SDIS)</strong>, la <strong>Secretar&iacute;a de Educaci&oacute;n</strong>, la <strong>Secretar&iacute;a de Desarrollo Econ&oacute;mico</strong> y la <strong>Agencia Atenea</strong>.</p>
                    <p style="line-height:1.7;">La gesti&oacute;n operativa recae principalmente en la Subdirecci&oacute;n para la Juventud de la SDIS, cuyo equipo se organiza bajo roles espec&iacute;ficos para garantizar la atenci&oacute;n integral:</p>

                    <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:22px; margin-bottom:32px;">
                        <div style="background:#2B2F3A; border-radius:12px; padding:20px; box-shadow:7px 7px 0 #b8a9d4; color:#fff;">
                            <h4 style="font-size:0.95rem; color:#d4c6f0; margin:0 0 12px; font-weight:700;">Equipo Psicosocial</h4>
                            <p style="font-size:0.85rem; color:rgba(255,255,255,0.8); margin:0; line-height:1.6;">Acompa&ntilde;amiento directo a los j&oacute;venes y liderar la Formaci&oacute;n en Proyecto de Vida.</p>
                        </div>
                        <div style="background:#2B2F3A; border-radius:12px; padding:20px; box-shadow:7px 7px 0 #b8a9d4; color:#fff;">
                            <h4 style="font-size:0.95rem; color:#d4c6f0; margin:0 0 12px; font-weight:700;">Equipo Territorial</h4>
                            <p style="font-size:0.85rem; color:rgba(255,255,255,0.8); margin:0; line-height:1.6;">Apoya el contacto, la formalizaci&oacute;n de los ingresos y el seguimiento en las localidades.</p>
                        </div>
                        <div style="background:#2B2F3A; border-radius:12px; padding:20px; box-shadow:7px 7px 0 #b8a9d4; color:#fff;">
                            <h4 style="font-size:0.95rem; color:#d4c6f0; margin:0 0 12px; font-weight:700;">Equipos Transversales</h4>
                            <p style="font-size:0.85rem; color:rgba(255,255,255,0.8); margin:0; line-height:1.6;">Anal&iacute;tica, gesti&oacute;n documental, administrativo y financiero: validan requisitos de ingreso, administran bases de datos y consolidan el cumplimiento de actividades para gestionar las transferencias monetarias.</p>
                        </div>
                    </div>

                    <h3 class="card-subtitle">Organigrama del equipo</h3>
                    <p style="line-height:1.7;">El equipo completo del servicio, con nombres y roles, se organiza seg&uacute;n el siguiente organigrama:</p>
                    <div style="margin:18px 0 10px; text-align:center;">
                        <img src="imagenes/Organigrama JcO.jpeg" alt="Organigrama del equipo de J&oacute;venes con Oportunidades" style="max-width:100%; height:auto; border-radius:8px; box-shadow:0 2px 10px rgba(0,0,0,0.08);">
                    </div>
                </div>
            </div>"""

# --- Pilares ---
SECCION_PILARES = """\
            <div class="content-section" id="pilares">
                <div class="card">
                    <h2 class="card-title">Pilares del programa J&oacute;venes con Oportunidades</h2>

                    <h3 class="card-subtitle">1. Acompa&ntilde;amiento psicosocial</h3>
                    <p style="line-height:1.7;">Orientaci&oacute;n y seguimiento transversal a cargo de la Secretar&iacute;a Distrital de Integraci&oacute;n Social, para ayudar a los j&oacute;venes en la construcci&oacute;n de su proyecto de vida.</p>

                    <h3 class="card-subtitle">2. Rutas de formaci&oacute;n</h3>
                    <p style="line-height:1.7;">Los participantes eligen entre tres opciones:</p>
                    <div class="rutas-formacion-grid" style="display:grid; grid-template-columns:repeat(3, 1fr); gap:16px; margin-top:18px;">
                        <div style="display:flex; flex-direction:column;">
                            <div style="background:#5f9ea0; color:#fff; padding:10px 16px 10px 14px; font-weight:800; font-size:0.8rem; letter-spacing:0.5px; text-transform:uppercase; clip-path:polygon(0 0, calc(100% - 14px) 0, 100% 50%, calc(100% - 14px) 100%, 0 100%);">Ruta 1</div>
                            <div style="padding:14px 4px 0; border-top:1px dashed #ccc; margin-top:-1px;">
                                <h4 style="color:#253C5C; font-size:0.98rem; font-weight:700; margin:0 0 8px 0;">Educaci&oacute;n flexible</h4>
                                <p style="font-size:0.85rem; line-height:1.55; color:#555; margin:0;">Para personas j&oacute;venes y adultas que buscan completar su educaci&oacute;n media.</p>
                            </div>
                        </div>
                        <div style="display:flex; flex-direction:column;">
                            <div style="background:#e07850; color:#fff; padding:10px 16px 10px 14px; font-weight:800; font-size:0.8rem; letter-spacing:0.5px; text-transform:uppercase; clip-path:polygon(0 0, calc(100% - 14px) 0, 100% 50%, calc(100% - 14px) 100%, 0 100%);">Ruta 2</div>
                            <div style="padding:14px 4px 0; border-top:1px dashed #ccc; margin-top:-1px;">
                                <h4 style="color:#253C5C; font-size:0.98rem; font-weight:700; margin:0 0 8px 0;">Cursos cortos certificados</h4>
                                <p style="font-size:0.85rem; line-height:1.55; color:#555; margin:0;">Formaci&oacute;n de hasta 160 horas para adquirir competencias que aumenten las oportunidades de empleo.</p>
                            </div>
                        </div>
                        <div style="display:flex; flex-direction:column;">
                            <div style="background:#7b6b99; color:#fff; padding:10px 16px 10px 14px; font-weight:800; font-size:0.8rem; letter-spacing:0.5px; text-transform:uppercase; clip-path:polygon(0 0, calc(100% - 14px) 0, 100% 50%, calc(100% - 14px) 100%, 0 100%);">Ruta 3</div>
                            <div style="padding:14px 4px 0; border-top:1px dashed #ccc; margin-top:-1px;">
                                <h4 style="color:#253C5C; font-size:0.98rem; font-weight:700; margin:0 0 8px 0;">Educaci&oacute;n posmedia de ciclo largo</h4>
                                <p style="font-size:0.85rem; line-height:1.55; color:#555; margin:0;">Acceso a Educaci&oacute;n Superior y Educaci&oacute;n para el Trabajo y Desarrollo Humano, en articulaci&oacute;n con iniciativas como J&oacute;venes a la E.</p>
                            </div>
                        </div>
                    </div>

                    <h3 class="card-subtitle">3. Intermediaci&oacute;n laboral</h3>
                    <p style="line-height:1.7;">Una vez finalizada la formaci&oacute;n, la Secretar&iacute;a de Desarrollo Econ&oacute;mico lidera la intermediaci&oacute;n laboral, con acceso a servicios de registro de empleo a trav&eacute;s de plataformas como Talento Capital.</p>

                    <h3 class="card-subtitle">4. Transferencias monetarias condicionadas</h3>
                    <p style="line-height:1.7;">Apoyos econ&oacute;micos que dependen del cumplimiento de las actividades de cada ruta. Los topes m&aacute;ximos son: hasta <strong>$1.200.000</strong> para cursos cortos, hasta <strong>$3.200.000</strong> para educaci&oacute;n flexible, y montos desde <strong>$2.700.000</strong> hasta <strong>$4.300.000</strong> en educaci&oacute;n posmedia y universitaria.</p>
                </div>
            </div>"""


# --- Módulos de Proyecto de Vida ---
# Texto literal redactado por David (equipo psicosocial JCO).
# Diseño: cabecera oscura con número de color en flecha y cuerpo crema con
# el párrafo completo. El número del módulo va en la flecha lateral, así que
# el título solo lleva el nombre del módulo (sin "MÓDULO N:").
SECCION_MODULOS_PROYECTO_VIDA = """\
            <div class="content-section" id="modulos_proyecto_vida">
                <div class="card">
                    <h2 class="card-title">Los 7 m&oacute;dulos de formaci&oacute;n en Proyecto de Vida</h2>
                    <p style="line-height:1.7;">Como parte del proceso de fortalecimiento de capacidades, todos los participantes cursan <strong>siete m&oacute;dulos pedag&oacute;gicos</strong> bajo una metodolog&iacute;a de <strong>talleres presenciales y vivenciales</strong>, estructurados en tres momentos: motivaci&oacute;n, teor&iacute;a y ejercicios pr&aacute;cticos.</p>

                    <div class="modulo-acordeon">
                        <div class="modulo-header">
                            <span class="modulo-header-num" style="background:#5f9ea0;">1</span>
                            <span class="modulo-header-titulo">Sentido de vida</span>
                        </div>
                        <div class="modulo-body">
                            <p>El primer m&oacute;dulo tiene como objetivo aportar al desarrollo del sentido de vida y la visualizaci&oacute;n de metas, con miras al bienestar integral, mediante herramientas de autoconocimiento y proyecci&oacute;n socio-ocupacional. Lo anterior se logra mediante acuerdos previos con los j&oacute;venes para promover espacios seguros para las actividades, donde se recalca que no existen respuestas correctas o incorrectas. Con actividades como el &ldquo;diagrama del Ikigai&rdquo; y &ldquo;Conejos a sus madrigueras&rdquo; se promueve una reflexi&oacute;n sobre la importancia del cuidado propio y cuidado hacia los otros.</p>
                        </div>
                    </div>

                    <div class="modulo-acordeon">
                        <div class="modulo-header">
                            <span class="modulo-header-num" style="background:#e07850;">2</span>
                            <span class="modulo-header-titulo">Coaching en finanzas</span>
                        </div>
                        <div class="modulo-body">
                            <p>El segundo m&oacute;dulo busca generar estrategias pr&aacute;cticas que permitan fortalecer habilidades para el entorno financiero y, asimismo, potenciar h&aacute;bitos para un manejo adecuado de las finanzas. A trav&eacute;s del desarrollo de habilidades blandas impartidas durante el m&oacute;dulo, se busca fomentar la asertiva toma de decisiones por medio de h&aacute;bitos financieros saludables. Para lograr este objetivo, el m&oacute;dulo se divide en 2 partes: 1) ense&ntilde;anza de conceptos b&aacute;sicos sobre finanzas personales y 2) la importancia del ahorro.</p>
                        </div>
                    </div>

                    <div class="modulo-acordeon">
                        <div class="modulo-header">
                            <span class="modulo-header-num" style="background:#7b6b99;">3</span>
                            <span class="modulo-header-titulo">Manejo del estr&eacute;s y la ansiedad</span>
                        </div>
                        <div class="modulo-body">
                            <p>El tercer m&oacute;dulo se plantea entender la diferencia entre estr&eacute;s y ansiedad, identificar sus causas y s&iacute;ntomas, y aprender estrategias efectivas para manejarlos. A trav&eacute;s de t&eacute;cnicas de relajaci&oacute;n, ejercicio f&iacute;sico, planificaci&oacute;n y organizaci&oacute;n para gestionar el tiempo y las cargas de trabajo se busca fortalecer las habilidades para manejar estas emociones de forma asertiva. Por medio de actividades como el &ldquo;medidor emocional&rdquo; y el &ldquo;teatro de la mente&rdquo; se ense&ntilde;a sobre los conceptos b&aacute;sicos necesarios para identificar la ansiedad y el estr&eacute;s, adem&aacute;s de diferenciar sus s&iacute;ntomas e identificar c&oacute;mo manejarlos, ya sea por medio de estrategias de autorregulaci&oacute;n o acudiendo a profesionales cuando los s&iacute;ntomas as&iacute; lo requieran.</p>
                        </div>
                    </div>

                    <div class="modulo-acordeon">
                        <div class="modulo-header">
                            <span class="modulo-header-num" style="background:#d4a84b;">4</span>
                            <span class="modulo-header-titulo">Acoso en el &aacute;mbito educativo, mobbing y resoluci&oacute;n de conflictos</span>
                        </div>
                        <div class="modulo-body">
                            <p>El cuarto m&oacute;dulo se plantea identificar el acoso (Bullying) como una problem&aacute;tica social actual y brindar informaci&oacute;n acerca de los escenarios en los que se presenta, las herramientas existentes para prevenir o afrontar situaciones de acoso, rutas de apoyo y estrategias para la resoluci&oacute;n de conflictos. Por medio de actividades como &ldquo;en tus zapatos&rdquo; y &ldquo;representaciones del acoso&rdquo; se ense&ntilde;an conceptos relevantes sobre el acoso, adem&aacute;s de rutas de atenci&oacute;n para abordar esta problem&aacute;tica cuando se presenta.</p>
                        </div>
                    </div>

                    <div class="modulo-acordeon">
                        <div class="modulo-header">
                            <span class="modulo-header-num" style="background:#6b8e7f;">5</span>
                            <span class="modulo-header-titulo">Relaciones saludables y cuidadosas</span>
                        </div>
                        <div class="modulo-body">
                            <p>El quinto m&oacute;dulo tiene como objetivo fortalecer habilidades blandas para la construcci&oacute;n de relaciones saludables y cuidadosas mediante la implementaci&oacute;n de acciones de informaci&oacute;n y formaci&oacute;n. En este m&oacute;dulo se aborda el desarrollo de un &ldquo;botiqu&iacute;n de gesti&oacute;n emocional&rdquo; y &ldquo;la receta de las relaciones sanas y cuidadosas&rdquo;, las cuales buscan ense&ntilde;ar y recopilar las herramientas trabajadas durante la sesi&oacute;n para mejorar el trato de las relaciones saludables en el &aacute;mbito familiar, social, de pareja, laboral, entre otros. Adem&aacute;s, se ense&ntilde;a sobre &ldquo;red flags&rdquo; (banderas rojas), lo cual permite identificar y establecer l&iacute;mites en las relaciones.</p>
                        </div>
                    </div>

                    <div class="modulo-acordeon">
                        <div class="modulo-header">
                            <span class="modulo-header-num" style="background:#c86464;">6</span>
                            <span class="modulo-header-titulo">Promoci&oacute;n de derechos y habilidades para la vida</span>
                        </div>
                        <div class="modulo-body">
                            <p>El sexto m&oacute;dulo busca incentivar la promoci&oacute;n y protecci&oacute;n de los derechos mediante diferentes estrategias que contribuyan en su conocimiento, difusi&oacute;n y respeto, e identificar las habilidades sociales de cada joven para que estas puedan aportar de manera significativa su desarrollo e interacci&oacute;n con la sociedad en diferentes contextos. Para lograr este objetivo, el m&oacute;dulo aborda tem&aacute;ticas relacionadas con la promoci&oacute;n y la protecci&oacute;n de los derechos, enfocados principalmente en el derecho a la vida, a la salud, al trabajo, a la educaci&oacute;n y los derechos sexuales y reproductivos.</p>
                        </div>
                    </div>

                    <div class="modulo-acordeon">
                        <div class="modulo-header">
                            <span class="modulo-header-num" style="background:#4a7ba7;">7</span>
                            <span class="modulo-header-titulo">Activa tu potencial</span>
                        </div>
                        <div class="modulo-body">
                            <p>El &uacute;ltimo m&oacute;dulo tiene como objetivo orientar e incentivar la apropiaci&oacute;n de elementos relevantes que faciliten la participaci&oacute;n en la ruta de formaci&oacute;n corta e intermediaci&oacute;n laboral. En este m&oacute;dulo se ense&ntilde;a en qu&eacute; consiste la ruta de formaci&oacute;n e intermediaci&oacute;n laboral, adem&aacute;s de ense&ntilde;ar los beneficios de participar en la ruta. En este m&oacute;dulo final, los participantes identifican, con base en sus intereses, los procesos para avanzar en las rutas, adem&aacute;s de los canales de comunicaci&oacute;n en caso de requerir apoyo.</p>
                        </div>
                    </div>
                </div>
            </div>"""

# --- Flujo de gestión de la información ---
SECCION_GESTION_DATOS = """\
            <div class="content-section" id="flujo_datos">
                <div class="card">
                    <h2 class="card-title">Flujo de gesti&oacute;n de la informaci&oacute;n</h2>
                    <p style="color:#666; margin-bottom:20px;">La gesti&oacute;n de la informaci&oacute;n de JCO est&aacute; dise&ntilde;ada para operar con cohortes de <strong>m&aacute;s de 5.000 j&oacute;venes</strong> que el servicio administra internamente y luego carga en SIRBE, en lugar de registrar cada joven uno por uno.</p>

                    <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:25px;">
                        <span style="display:inline-block; padding:4px 12px; border-radius:15px; background:var(--accent-bg); color:var(--accent); font-size:0.8rem; font-weight:600;">DADE</span>
                        <span style="display:inline-block; padding:4px 12px; border-radius:15px; background:#e8ecf1; color:#3A3A3A; font-size:0.8rem; font-weight:600;">Equipo psicosocial</span>
                        <span style="display:inline-block; padding:4px 12px; border-radius:15px; background:var(--accent-border); color:var(--accent); font-size:0.8rem; font-weight:600;">Equipo de anal&iacute;tica</span>
                    </div>

                    <div style="position:relative; padding-left:30px;">
                        <div style="position:absolute; left:12px; top:0; bottom:0; width:3px; background:linear-gradient(to bottom, var(--accent), #2F3E3C); border-radius:2px;"></div>

                        <div style="position:relative; margin-bottom:25px;">
                            <div style="position:absolute; left:-24px; top:4px; width:14px; height:14px; background:var(--accent); border-radius:50%; border:3px solid var(--accent-bg);"></div>
                            <h3 style="font-size:1rem; color:var(--accent); margin:0 0 6px;">1. Ingreso masivo por cohortes</h3>
                            <span style="display:inline-block; padding:2px 8px; border-radius:10px; font-size:0.7rem; background:var(--accent-bg); color:var(--accent); margin-bottom:6px; font-weight:600;">DADE</span>
                            <p style="font-size:0.88rem; color:#555; line-height:1.6; margin:0;">En JCO no se llena una ficha SIRBE individual como en Casas de Juventud o Forjar. El ingreso se realiza mediante el <strong>cargue masivo de una base de datos</strong>, porque el servicio opera con cohortes grandes de miles de j&oacute;venes focalizados previamente por la <strong>Direcci&oacute;n de An&aacute;lisis y Dise&ntilde;o Estrat&eacute;gico (DADE)</strong>.</p>
                        </div>

                        <div style="position:relative; margin-bottom:25px;">
                            <div style="position:absolute; left:-24px; top:4px; width:14px; height:14px; background:var(--accent); border-radius:50%; border:3px solid var(--accent-bg);"></div>
                            <h3 style="font-size:1rem; color:var(--accent); margin:0 0 6px;">2. Estructura en SIRBE: servicios sociales con modalidades</h3>
                            <span style="display:inline-block; padding:2px 8px; border-radius:10px; font-size:0.7rem; background:#e8ecf1; color:#3A3A3A; margin-bottom:6px; font-weight:600;">Equipo psicosocial</span>
                            <p style="font-size:0.88rem; color:#555; line-height:1.6; margin:0;">JCO est&aacute; parametrizado en SIRBE como <strong>&ldquo;servicio social&rdquo;</strong> (no como curso) y tiene configuradas <strong>modalidades que reflejan las rutas del servicio</strong>. Todos los j&oacute;venes inician su proceso por la modalidad de <strong>Proyecto de Vida</strong> y lo finalizan saliendo por <strong>Intermediaci&oacute;n laboral</strong>. La parametrizaci&oacute;n es estricta: no hay campos de texto abierto, los profesionales seleccionan siempre de listas preestablecidas.</p>
                        </div>

                        <div style="position:relative; margin-bottom:25px;">
                            <div style="position:absolute; left:-24px; top:4px; width:14px; height:14px; background:var(--accent); border-radius:50%; border:3px solid var(--accent-bg);"></div>
                            <h3 style="font-size:1rem; color:var(--accent); margin:0 0 6px;">3. Tres tipos de actuaciones</h3>
                            <span style="display:inline-block; padding:2px 8px; border-radius:10px; font-size:0.7rem; background:#e8ecf1; color:#3A3A3A; margin-bottom:6px; font-weight:600;">Equipo psicosocial</span>
                            <p style="font-size:0.88rem; color:#555; line-height:1.6; margin:0 0 6px;">El seguimiento a los j&oacute;venes se registra en SIRBE con tres tipos de actuaci&oacute;n:</p>
                            <ul style="font-size:0.88rem; color:#555; line-height:1.7; margin:0 0 0 18px;">
                                <li><strong>Estado:</strong> situaci&oacute;n actual del joven (en atenci&oacute;n, suspendido, transferido o retirado).</li>
                                <li><strong>Intervenci&oacute;n:</strong> registra si el joven cumpli&oacute; o incumpli&oacute; las condiciones para autorizar el pago de la transferencia monetaria.</li>
                                <li><strong>Seguimiento:</strong> registra el paso del joven entre modalidades dentro de su ruta.</li>
                            </ul>
                        </div>

                        <div style="position:relative; margin-bottom:10px;">
                            <div style="position:absolute; left:-24px; top:4px; width:14px; height:14px; background:var(--accent); border-radius:50%; border:3px solid var(--accent-bg);"></div>
                            <h3 style="font-size:1rem; color:var(--accent); margin:0 0 6px;">4. Anal&iacute;tica propia del servicio</h3>
                            <span style="display:inline-block; padding:2px 8px; border-radius:10px; font-size:0.7rem; background:var(--accent-border); color:var(--accent); margin-bottom:6px; font-weight:600;">Equipo de anal&iacute;tica</span>
                            <p style="font-size:0.88rem; color:#555; line-height:1.6; margin:0;">La informaci&oacute;n oficial del servicio es gestionada directamente por el <strong>equipo de anal&iacute;tica</strong> de JCO mediante bases de datos propias.</p>
                        </div>
                    </div>

                    <h3 class="card-subtitle" style="margin-top:30px;">Diagrama de flujo del proceso</h3>
                    <p style="color:#666; font-size:0.85rem; margin-bottom:12px;">Representaci&oacute;n visual del ciclo de recolecci&oacute;n y digitaci&oacute;n en SIRBE para J&oacute;venes con Oportunidades.</p>
                    <img src="imagenes/diagrama_flujo_jco.png" alt="Diagrama de flujo del proceso del ciclo J&oacute;venes con Oportunidades" style="width:100%; border:1px solid #e0e0e0; border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.05);">
                </div>
            </div>"""

# --- Estadísticas ---
SECCION_ESTADISTICAS = """\
            <div class="content-section" id="estadisticas">
                <div class="card">
                    <h2 class="card-title">Estad&iacute;sticas</h2>
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
        SECCION_LINEA_TIEMPO,
        SECCION_A_TENER_EN_CUENTA,
        SECCION_EQUIPO,
        SECCION_PILARES,
        SECCION_MODULOS_PROYECTO_VIDA,
        SECCION_GESTION_DATOS,
        seccion_aliados_jco(),
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
