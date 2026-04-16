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
                    <div class="sidebar-item" onclick="showContent('linea_tiempo')">L&iacute;nea de tiempo</div>
                    <div class="sidebar-item" onclick="showContent('a_tener_en_cuenta')">A tener en cuenta</div>
                    <div class="sidebar-item" onclick="showContent('equipo')">Equipo</div>
                    <div class="sidebar-item" onclick="showContent('pilares')">Pilares del programa</div>
                    <div class="sidebar-item" onclick="showContent('modulos_proyecto_vida')">M&oacute;dulos de Proyecto de Vida</div>
                    <div class="sidebar-item" onclick="showContent('triage_psicosocial')">Triage psicosocial</div>
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

# --- A tener en cuenta ---
SECCION_A_TENER_EN_CUENTA = """\
            <div class="content-section" id="a_tener_en_cuenta">
                <div class="card">
                    <h2 class="card-title">A tener en cuenta</h2>

                    <h3 class="card-subtitle">Los montos var&iacute;an seg&uacute;n la ruta de formaci&oacute;n</h3>
                    <p style="line-height:1.7;">Parceros entregaba una cuota fija de <strong>$500.000 mensuales durante 6 meses</strong>. En J&oacute;venes con Oportunidades el apoyo econ&oacute;mico depende de la ruta elegida: hasta <strong>$1.200.000 en cursos cortos</strong>, hasta <strong>$3.200.000</strong> en la ruta de educaci&oacute;n flexible para terminar el bachillerato (j&oacute;venes y adultos), y topes m&aacute;ximos que van desde <strong>$2.700.000</strong> (para nivel t&eacute;cnico y tecn&oacute;logo) hasta <strong>$4.300.000</strong> en educaci&oacute;n universitaria de ciclo largo.</p>

                    <h3 class="card-subtitle">Focalizaci&oacute;n y requisitos de ingreso</h3>
                    <p style="line-height:1.7;">Los criterios de selecci&oacute;n var&iacute;an entre ambos modelos. Parceros por Bogot&aacute; se enfocaba en j&oacute;venes &ldquo;Ninis&rdquo; (que ni estudian ni trabajan) de <strong>18 a 28 a&ntilde;os</strong>, identificados directamente en barrios vulnerables mediante una encuesta de 23 preguntas que calculaba su &Iacute;ndice de Vulnerabilidad Juvenil. Por su parte, el nuevo programa J&oacute;venes con Oportunidades atiende a j&oacute;venes de <strong>14 a 28 a&ntilde;os</strong> en situaci&oacute;n de pobreza extrema, moderada o vulnerabilidad por inseguridad alimentaria. Su focalizaci&oacute;n es distinta, ya que exige que los beneficiarios residan en Bogot&aacute; y est&eacute;n registrados oficialmente en el Sisb&eacute;n dentro de las categor&iacute;as <strong>A, B o hasta C09</strong>.</p>

                    <h3 class="card-subtitle">Financiaci&oacute;n de los programas</h3>
                    <p style="line-height:1.7;">Una caracter&iacute;stica clave de Parceros por Bogot&aacute; es que se sustentaba, en gran parte, gracias a la uni&oacute;n institucional con los <strong>Fondos de Desarrollo Local (FDL)</strong>. Esto permiti&oacute; una inversi&oacute;n territorializada, donde los alcaldes locales y ediles destinaban recursos para apoyar directamente a los j&oacute;venes de sus respectivas localidades. Por su parte, la nueva estrategia J&oacute;venes con Oportunidades cuenta con una inversi&oacute;n distrital proyectada de <strong>$324.053 millones</strong>, uniendo los esfuerzos sectoriales de las Secretar&iacute;as de Integraci&oacute;n Social, Educaci&oacute;n, Desarrollo Econ&oacute;mico y la Agencia Atenea.</p>

                    <h3 class="card-subtitle">El cambio de paradigma en la condicionalidad</h3>
                    <p style="line-height:1.7;">En Parceros por Bogot&aacute;, la transferencia monetaria estaba condicionada a la participaci&oacute;n en actividades pedag&oacute;gicas y labores pr&aacute;cticas de servicio a la ciudad, tales como proyectos de embellecimiento, limpieza, huertas urbanas y &ldquo;Nuestras Zonas Seguras&rdquo;. Adem&aacute;s, los participantes se formaban y certificaban como Agentes Comunitarios de Prevenci&oacute;n en temas de salud mental, violencias y consumo de sustancias. Con J&oacute;venes con Oportunidades, la condicionalidad depende directamente del cumplimiento de actividades en tres componentes clave: el acompa&ntilde;amiento psicosocial transversal, el avance en la ruta de formaci&oacute;n elegida, y el proceso de orientaci&oacute;n e intermediaci&oacute;n laboral.</p>

                    <h3 class="card-subtitle">Intermediaci&oacute;n laboral y conexi&oacute;n con el empleo</h3>
                    <p style="line-height:1.7;">En Parceros por Bogot&aacute;, la conexi&oacute;n con el mercado laboral se daba principalmente al culminar el programa, mediante ferias de empleo organizadas exclusivamente para los egresados y la gesti&oacute;n de alianzas con empresas del sector privado. En el nuevo modelo de J&oacute;venes con Oportunidades, la intermediaci&oacute;n se consolida como una etapa formal y estructural, siendo el tercer componente de la ruta. El objetivo es garantizar la integralidad y que el joven &ldquo;salga por el &uacute;ltimo eslab&oacute;n&rdquo; con el resultado esperado. Por ello, al finalizar su formaci&oacute;n, la Secretar&iacute;a Distrital de Desarrollo Econ&oacute;mico asume el liderazgo directo para garantizar la orientaci&oacute;n y el registro en el Servicio P&uacute;blico de Empleo o en las plataformas de la estrategia &ldquo;Talento Capital&rdquo;.</p>
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
                            <div class="timeline-year">2023 (diciembre)</div>
                            <div class="timeline-text"><strong>Cierre del ciclo Parceros por Bogot&aacute;.</strong> Al finalizar el programa se reportan <strong>m&aacute;s de 28.000 j&oacute;venes atendidos</strong> y m&aacute;s de <strong>64 alianzas</strong> con sector p&uacute;blico y privado. <strong>4 de cada 10 egresados</strong> obtuvieron empleo formal, apoyo para emprendimiento o acceso a educaci&oacute;n superior.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2024</div>
                            <div class="timeline-text"><strong>Se lanza oficialmente el programa J&oacute;venes con Oportunidades.</strong> Este nuevo modelo, enmarcado t&eacute;cnica y presupuestalmente dentro del Proyecto de Inversi&oacute;n 7940 &ldquo;Implementaci&oacute;n de estrategias de inclusi&oacute;n social y productiva para la poblaci&oacute;n joven en situaci&oacute;n de pobreza y vulnerabilidad en Bogot&aacute;&rdquo;, mantiene el acompa&ntilde;amiento psicosocial y las transferencias monetarias condicionadas, pero ahora articula el esfuerzo de las Secretar&iacute;as de Integraci&oacute;n Social, Educaci&oacute;n y Desarrollo Econ&oacute;mico junto con la Agencia Atenea. Vincula el apoyo econ&oacute;mico directamente a tres rutas de formaci&oacute;n espec&iacute;fica.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2024 &ndash; 2027</div>
                            <div class="timeline-text"><strong>Meta del cuatrienio.</strong> J&oacute;venes con Oportunidades tiene el reto de beneficiar a <strong>40.000 j&oacute;venes</strong> con una inversi&oacute;n distrital proyectada de <strong>$324.053 millones</strong>, garantizando que el origen socioecon&oacute;mico no sea un impedimento para el desarrollo del potencial de la juventud bogotana.</div>
                        </div>
                    </div>
                </div>
            </div>"""

# --- Equipo ---
SECCION_EQUIPO = """\
            <div class="content-section" id="equipo">
                <div class="card">
                    <h2 class="card-title">Equipo y gesti&oacute;n de J&oacute;venes con Oportunidades</h2>
                    <p style="line-height:1.7;">El servicio J&oacute;venes con Oportunidades es un esfuerzo articulado entre la <strong>Secretar&iacute;a Distrital de Integraci&oacute;n Social (SDIS)</strong>, la <strong>Secretar&iacute;a de Educaci&oacute;n</strong>, la <strong>Secretar&iacute;a de Desarrollo Econ&oacute;mico</strong> y la <strong>Agencia Atenea</strong>. Su seguimiento y articulaci&oacute;n intersectorial se lidera a trav&eacute;s de tres instancias: el <strong>Comit&eacute; T&eacute;cnico</strong>, el <strong>Comit&eacute; Estrat&eacute;gico</strong> y el <strong>Comit&eacute; Directivo</strong>.</p>
                    <p style="line-height:1.7;">La gesti&oacute;n operativa recae principalmente en la Subdirecci&oacute;n para la Juventud de la SDIS, cuyo equipo se organiza bajo roles espec&iacute;ficos para garantizar la atenci&oacute;n integral:</p>

                    <div style="display:grid; grid-template-columns:repeat(2, 1fr); gap:22px; margin-bottom:32px;">
                        <div style="background:#2B2F3A; border-radius:12px; padding:20px; box-shadow:7px 7px 0 #b8a9d4; color:#fff;">
                            <h4 style="font-size:0.95rem; color:#d4c6f0; margin:0 0 12px; font-weight:700;">Equipo Psicosocial</h4>
                            <p style="font-size:0.85rem; color:rgba(255,255,255,0.8); margin:0; line-height:1.6;">Acompa&ntilde;amiento directo a los j&oacute;venes, guiar la aplicaci&oacute;n del Triage psicosocial y liderar la Formaci&oacute;n en Proyecto de Vida.</p>
                        </div>
                        <div style="background:#2B2F3A; border-radius:12px; padding:20px; box-shadow:7px 7px 0 #b8a9d4; color:#fff;">
                            <h4 style="font-size:0.95rem; color:#d4c6f0; margin:0 0 12px; font-weight:700;">Equipo de Alertas</h4>
                            <p style="font-size:0.85rem; color:rgba(255,255,255,0.8); margin:0; line-height:1.6;">Sistematizar el Triage, gestionar las alertas de vulneraci&oacute;n de derechos inmediatas (alto riesgo) y referenciar a los j&oacute;venes a la oferta interinstitucional.</p>
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
                </div>
            </div>"""

# --- Pilares ---
SECCION_PILARES = """\
            <div class="content-section" id="pilares">
                <div class="card">
                    <h2 class="card-title">Pilares del programa J&oacute;venes con Oportunidades</h2>

                    <h3 class="card-subtitle">1. Acompa&ntilde;amiento psicosocial</h3>
                    <p style="line-height:1.7;">Orientaci&oacute;n y seguimiento transversal a cargo de la Secretar&iacute;a Distrital de Integraci&oacute;n Social, para ayudar a los j&oacute;venes en la construcci&oacute;n de su proyecto de vida y gestionar alertas de vulneraci&oacute;n de derechos.</p>

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
                                <p style="font-size:0.85rem; line-height:1.55; color:#555; margin:0;">Acceso a Educaci&oacute;n Superior y Educaci&oacute;n para el Trabajo y Desarrollo Humano, articul&aacute;ndose con iniciativas como J&oacute;venes a la E.</p>
                            </div>
                        </div>
                    </div>

                    <h3 class="card-subtitle">3. Acompa&ntilde;amiento y orientaci&oacute;n laboral</h3>
                    <p style="line-height:1.7;">Una vez finalizada la formaci&oacute;n, la Secretar&iacute;a de Desarrollo Econ&oacute;mico lidera el acceso a servicios de registro de empleo, orientaci&oacute;n e intermediaci&oacute;n laboral a trav&eacute;s de plataformas como Talento Capital.</p>

                    <h3 class="card-subtitle">4. Transferencias monetarias condicionadas</h3>
                    <p style="line-height:1.7;">Apoyos econ&oacute;micos que dependen del cumplimiento de las actividades de cada ruta. Los topes m&aacute;ximos son: hasta <strong>$1.200.000</strong> para cursos cortos, hasta <strong>$3.200.000</strong> para educaci&oacute;n flexible, y montos desde <strong>$2.700.000</strong> hasta <strong>$4.300.000</strong> en educaci&oacute;n posmedia y universitaria.</p>
                </div>
            </div>"""


# --- Módulos de Proyecto de Vida ---
SECCION_MODULOS_PROYECTO_VIDA = """\
            <div class="content-section" id="modulos_proyecto_vida">
                <div class="card">
                    <h2 class="card-title">Los 7 m&oacute;dulos de formaci&oacute;n en Proyecto de Vida</h2>
                    <p style="line-height:1.7;">Como parte del proceso de fortalecimiento de capacidades, todos los participantes cursan <strong>siete m&oacute;dulos pedag&oacute;gicos</strong> bajo una metodolog&iacute;a de <strong>talleres presenciales y vivenciales</strong>, estructurados en tres momentos: motivaci&oacute;n, teor&iacute;a y ejercicios pr&aacute;cticos.</p>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#5f9ea0; color:#fff; min-width:72px; padding:14px 24px 14px 18px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.6rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">1</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">
                            <strong style="font-size:0.98rem;">Sentido de vida y bienestar.</strong> Desarrollo del autoconocimiento y proyecci&oacute;n de metas personales mediante herramientas como el Ikigai. <em style="opacity:0.85;">Talleres de introspecci&oacute;n y mapeo de sue&ntilde;os.</em>
                        </div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#e07850; color:#fff; min-width:72px; padding:14px 24px 14px 18px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.6rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">2</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">
                            <strong style="font-size:0.98rem;">Coaching en finanzas.</strong> Fortalecimiento de la cultura del ahorro y pautas para la gesti&oacute;n econ&oacute;mica del hogar y el negocio. <em style="opacity:0.85;">Ejercicios de presupuesto y planeaci&oacute;n financiera.</em>
                        </div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#7b6b99; color:#fff; min-width:72px; padding:14px 24px 14px 18px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.6rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">3</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">
                            <strong style="font-size:0.98rem;">Manejo del estr&eacute;s y ansiedad.</strong> Identificaci&oacute;n de s&iacute;ntomas emocionales y aprendizaje de t&eacute;cnicas para regular el bienestar mental. <em style="opacity:0.85;">Din&aacute;micas de relajaci&oacute;n y reconocimiento emocional.</em>
                        </div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#d4a84b; color:#fff; min-width:72px; padding:14px 24px 14px 18px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.6rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">4</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">
                            <strong style="font-size:0.98rem;">Acoso y resoluci&oacute;n de conflictos.</strong> Herramientas para detectar el <em>bullying</em> y estrategias de di&aacute;logo para la convivencia pac&iacute;fica. <em style="opacity:0.85;">Juegos de rol y simulaci&oacute;n de casos de conflicto.</em>
                        </div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#6b8e7f; color:#fff; min-width:72px; padding:14px 24px 14px 18px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.6rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">5</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">
                            <strong style="font-size:0.98rem;">Relaciones saludables y cuidadosas.</strong> Fomento de v&iacute;nculos basados en el respeto, el cuidado mutuo y la prevenci&oacute;n de violencias. <em style="opacity:0.85;">Actividades grupales de empat&iacute;a y comunicaci&oacute;n.</em>
                        </div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#c86464; color:#fff; min-width:72px; padding:14px 24px 14px 18px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.6rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">6</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">
                            <strong style="font-size:0.98rem;">Promoci&oacute;n de derechos y habilidades.</strong> Reconocimiento del joven como sujeto de derechos y fortalecimiento de habilidades socioemocionales. <em style="opacity:0.85;">Debates y an&aacute;lisis de derechos ciudadanos.</em>
                        </div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#4a7ba7; color:#fff; min-width:72px; padding:14px 24px 14px 18px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.6rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">7</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">
                            <strong style="font-size:0.98rem;">Activa tu potencial.</strong> Conexi&oacute;n de las capacidades individuales con las rutas de inclusi&oacute;n social y productiva. <em style="opacity:0.85;">Mapeo de habilidades y perfiles de oportunidad.</em>
                        </div>
                    </div>
                </div>
            </div>"""

# --- Triage psicosocial ---
SECCION_TRIAGE_PSICOSOCIAL = """\
            <div class="content-section" id="triage_psicosocial">
                <div class="card">
                    <h2 class="card-title">Componente psicosocial y el instrumento de Triage</h2>
                    <p style="line-height:1.7;">El <strong>acompa&ntilde;amiento psicosocial</strong> es un componente transversal durante toda la permanencia del joven en el servicio. Posterior a la formalizaci&oacute;n del ingreso, el equipo profesional acompa&ntilde;a la aplicaci&oacute;n del <strong>Triage psicosocial</strong>, un instrumento de auto-reporte que permite caracterizar social, econ&oacute;mica y territorialmente a las y los participantes.</p>

                    <h3 class="card-subtitle">&iquest;Para qu&eacute; sirve el Triage?</h3>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px; margin-top:15px;">
                        <div style="background:#5f9ea0; color:#fff; min-width:180px; padding:14px 24px 14px 18px; display:flex; align-items:center; font-weight:700; font-size:0.9rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">Identificar y clasificar alertas</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">Detecta situaciones de vulneraci&oacute;n de derechos y las clasifica. Identifica alertas inmediatas con alto riesgo (como <strong>prevenci&oacute;n del suicidio</strong> y <strong>violencia intrafamiliar</strong>) y alertas mediatas (como <strong>salud mental</strong> o <strong>prevenci&oacute;n del consumo de sustancias psicoactivas</strong>).</div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#e07850; color:#fff; min-width:180px; padding:14px 24px 14px 18px; display:flex; align-items:center; font-weight:700; font-size:0.9rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">Definir el nivel de acompa&ntilde;amiento</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">Los resultados no definen la ruta acad&eacute;mica, sino que canalizan al joven hacia la atenci&oacute;n psicosocial adecuada: <strong>Salas de Escucha Especializadas</strong> (para riesgos inmediatos), <strong>Salas de Escucha Psicosocial</strong> (para riesgos mediatos) o <strong>Actividades Colectivas de Prevenci&oacute;n y Promoci&oacute;n</strong> (para j&oacute;venes sin alertas).</div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#7b6b99; color:#fff; min-width:180px; padding:14px 24px 14px 18px; display:flex; align-items:center; font-weight:700; font-size:0.9rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">Referenciaci&oacute;n institucional</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">Facilita la conexi&oacute;n y referenciaci&oacute;n del joven hacia otros servicios que brindan la Secretar&iacute;a Distrital de Integraci&oacute;n Social y el Distrito Capital.</div>
                    </div>

                    <h3 class="card-subtitle">Tipos de alertas</h3>
                    <p style="line-height:1.7;"><strong>Alertas inmediatas:</strong> Corresponden a situaciones con un alto riesgo de vulneraci&oacute;n de derechos. Los j&oacute;venes identificados con este tipo de alertas son canalizados a las <strong>Salas de Escucha Especializadas</strong>, las cuales son desarrolladas directamente por el equipo de alertas del servicio e intervienen tem&aacute;ticas urgentes como la prevenci&oacute;n del suicidio y la prevenci&oacute;n de la violencia intrafamiliar.</p>
                    <p style="line-height:1.7;"><strong>Alertas mediatas:</strong> Son aquellas situaciones de riesgo que requieren intervenci&oacute;n, pero no representan una emergencia inminente. Los participantes con estas alertas son dirigidos a las <strong>Salas de Escucha Psicosocial</strong>, desarrolladas por el equipo psicosocial, para abordar temas como la salud mental, la crianza, el amor rom&aacute;ntico y la prevenci&oacute;n del consumo de sustancias psicoactivas.</p>
                    <p style="line-height:1.7;">Adicionalmente, el manual contempla una tercera categor&iacute;a:</p>
                    <p style="line-height:1.7;"><strong>Sin alertas:</strong> Si el joven no presenta alertas de vulneraci&oacute;n de derechos, es dirigido a <strong>Actividades Colectivas de Prevenci&oacute;n y Promoci&oacute;n</strong>. Estas acciones tienen un car&aacute;cter netamente preventivo.</p>

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
        SECCION_LINEA_TIEMPO,
        SECCION_A_TENER_EN_CUENTA,
        SECCION_EQUIPO,
        SECCION_PILARES,
        SECCION_MODULOS_PROYECTO_VIDA,
        SECCION_TRIAGE_PSICOSOCIAL,
        SECCION_GESTION_DATOS,
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
