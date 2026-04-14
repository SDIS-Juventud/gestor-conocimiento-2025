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
                    <p style="line-height:1.7;">Parceros entregaba una cuota fija de <strong>$500.000 mensuales durante 6 meses</strong>. En J&oacute;venes con Oportunidades el apoyo econ&oacute;mico depende de la ruta elegida: hasta <strong>$1.200.000 en cursos cortos</strong>, <strong>$1.000.000 por ciclo acad&eacute;mico</strong> m&aacute;s $300.000 por intermediaci&oacute;n laboral para quienes terminan bachillerato, o <strong>transferencias semestrales de sostenimiento</strong> para educaci&oacute;n superior. Las transferencias se gestionan a trav&eacute;s del sistema <strong>Ingreso M&iacute;nimo Garantizado (IMG)</strong>.</p>

                    <h3 class="card-subtitle">Focalizaci&oacute;n por Sisb&eacute;n A hasta C09</h3>
                    <p style="line-height:1.7;">El servicio est&aacute; dirigido a j&oacute;venes de <strong>14 a 28 a&ntilde;os</strong> en situaci&oacute;n de pobreza extrema, moderada o vulnerabilidad por inseguridad alimentaria, con puntaje Sisb&eacute;n entre A y C09. Ambos programas (Parceros y JCO) comparten esta base de focalizaci&oacute;n.</p>

                    <h3 class="card-subtitle">Parceros se financiaba en parte con Fondos de Desarrollo Local</h3>
                    <p style="line-height:1.7;">Una caracter&iacute;stica clave de la financiaci&oacute;n de Parceros por Bogot&aacute; es que se sustentaba, en gran parte, con recursos de los <strong>Fondos de Desarrollo Local (FDL)</strong> de las alcald&iacute;as. Esto permiti&oacute; una inversi&oacute;n territorializada pero condicionada a la disponibilidad de cada localidad. J&oacute;venes con Oportunidades se articula con presupuesto sectorial y sistema de pagos centralizado.</p>

                    <h3 class="card-subtitle">El cambio de paradigma en la condicionalidad</h3>
                    <p style="line-height:1.7;">En Parceros, los j&oacute;venes deb&iacute;an cumplir <strong>48 horas mensuales de servicio a la ciudad</strong> para recibir la transferencia, participando en programas distritales como <strong>Juntos Cuidamos Bogot&aacute;, Escuadrones de Limpieza y Zonas Seguras</strong>. Adem&aacute;s se formaban durante 100 horas como Agentes Comunitarios de Prevenci&oacute;n en salud mental, violencias y consumo. En J&oacute;venes con Oportunidades <strong>este servicio social ya no existe</strong>: la condicionalidad se centra exclusivamente en el avance dentro de las rutas de formaci&oacute;n y en la b&uacute;squeda efectiva de empleo.</p>

                    <h3 class="card-subtitle">Intermediaci&oacute;n laboral como etapa formal</h3>
                    <p style="line-height:1.7;">La intermediaci&oacute;n laboral es una etapa formal y estructural del dise&ntilde;o operativo de JCO. El programa busca que el joven <em>&ldquo;salga por el &uacute;ltimo eslab&oacute;n&rdquo;</em> con empleo o autonom&iacute;a econ&oacute;mica real, por eso la conexi&oacute;n con el mercado laboral es un componente t&eacute;cnico obligatorio y secuencial, no una actividad opcional o paralela.</p>
                    <ul style="line-height:1.7; margin-left:20px;">
                        <li>La <strong>Secretar&iacute;a Distrital de Desarrollo Econ&oacute;mico (SDDE)</strong> lidera el componente de acompa&ntilde;amiento y orientaci&oacute;n laboral una vez el joven finaliza su formaci&oacute;n.</li>
                        <li>Los participantes acceden al <strong>Servicio P&uacute;blico de Empleo</strong> y a las plataformas de prestadores socios de la estrategia <strong>&ldquo;Talento Capital&rdquo;</strong>, con orientaci&oacute;n ocupacional y fortalecimiento de habilidades blandas (socioemocionales y del siglo XXI) para mejorar el perfil competitivo en el mercado formal.</li>
                        <li>Incluye una transferencia monetaria &uacute;nica de <strong>$300.000</strong> por el logro de la intermediaci&oacute;n laboral al finalizar los ciclos acad&eacute;micos.</li>
                    </ul>
                </div>
            </div>"""

# --- Línea de tiempo ---
SECCION_LINEA_TIEMPO = """\
            <div class="content-section" id="linea_tiempo">
                <div class="card">
                    <h2 class="card-title">L&iacute;nea de tiempo</h2>
                    <p style="line-height:1.7; margin-bottom:20px;">Trayectoria institucional y evoluci&oacute;n de las pol&iacute;ticas de inclusi&oacute;n social juvenil en Bogot&aacute;: del modelo de emergencia <strong>Parceros por Bogot&aacute;</strong> hacia la estrategia integral <strong>J&oacute;venes con Oportunidades</strong>.</p>
                    <div class="timeline">
                        <div class="timeline-item">
                            <div class="timeline-year">2020</div>
                            <div class="timeline-text"><strong>Estrategia RETO y pilotaje t&eacute;cnico.</strong> La SDIS lanza la &ldquo;Estrategia RETO: Retorno de las Oportunidades Juveniles&rdquo; para reducir el riesgo social en poblaci&oacute;n joven vulnerable. Se realiza un programa piloto con <strong>152 j&oacute;venes</strong> en las ocho localidades con mayor vulnerabilidad, validando los instrumentos de focalizaci&oacute;n y caracterizaci&oacute;n que luego ser&iacute;an base de la operaci&oacute;n masiva.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2021</div>
                            <div class="timeline-text"><strong>Lanzamiento de Parceros por Bogot&aacute;.</strong> Tras el estallido social y las demandas del Paro Nacional, se formula el &ldquo;Plan de Rescate Social y Econ&oacute;mico&rdquo; y nace Parceros por Bogot&aacute; como el programa principal de la Estrategia RETO. Entrega transferencias monetarias de <strong>$500.000 mensuales durante 6 meses</strong>, con 48 horas mensuales de servicio a la ciudad y acompa&ntilde;amiento psicosocial. La <strong>Resoluci&oacute;n 509 del 20 de abril de 2021</strong> define las reglas de los servicios sociales y la focalizaci&oacute;n en la SDIS.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2021</div>
                            <div class="timeline-text"><strong>&Iacute;ndice de Vulnerabilidad Juvenil (IVJ).</strong> La Subdirecci&oacute;n para la Juventud desarrolla el IVJ como instrumento de priorizaci&oacute;n que eval&uacute;a cinco dimensiones con peso igualitario del 20%: educaci&oacute;n y trabajo, enfoque familiar, enfoque diferencial y de g&eacute;nero, salud, y maternidad o paternidad temprana. Garantiza que el programa atienda a j&oacute;venes v&iacute;ctimas del conflicto, personas con discapacidad y cuidadores.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2023 (diciembre)</div>
                            <div class="timeline-text"><strong>Cierre del ciclo Parceros por Bogot&aacute;.</strong> Al finalizar el programa se reportan <strong>cerca de 27.000 j&oacute;venes atendidos</strong>, una inversi&oacute;n acumulada de <strong>$109.000 millones</strong> y m&aacute;s de <strong>64 alianzas</strong> con sector p&uacute;blico y privado. <strong>4 de cada 10 egresados</strong> obtuvieron empleo formal, apoyo para emprendimiento o acceso a educaci&oacute;n superior.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2024 (septiembre)</div>
                            <div class="timeline-text"><strong>Transici&oacute;n normativa hacia J&oacute;venes con Oportunidades.</strong> La <strong>Resoluci&oacute;n 2007 de septiembre de 2024</strong> oficializa la transici&oacute;n y establece el Plan Especial para la Implementaci&oacute;n del nuevo servicio. Las actividades condicionadas del programa Parceros se mantienen v&aacute;lidas hasta el 30 de septiembre de 2024, cuando inicia el nuevo esquema de beneficios.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2024 (octubre)</div>
                            <div class="timeline-text"><strong>Lanzamiento de J&oacute;venes con Oportunidades.</strong> Bajo el Plan de Desarrollo 2024&ndash;2027 &ldquo;Bogot&aacute; Camina Segura&rdquo; (Acuerdo 927 de 2024), el nuevo servicio amp&iacute;a el rango de edad de <strong>18&ndash;28 a&ntilde;os a 14&ndash;28 a&ntilde;os</strong>, reconociendo que la exclusi&oacute;n educativa empieza antes de la mayor&iacute;a de edad. Pasa de un enfoque asistencialista a uno de inclusi&oacute;n productiva y formaci&oacute;n posmedia, con transferencias variables seg&uacute;n la ruta elegida (hasta $4.300.000 acumulados).</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-year">2025</div>
                            <div class="timeline-text"><strong>Articulaci&oacute;n interinstitucional y consolidaci&oacute;n.</strong> El <strong>Convenio Interadministrativo No. 1285 de 2025</strong> formaliza la alianza entre la Secretar&iacute;a de Integraci&oacute;n Social, la Secretar&iacute;a de Educaci&oacute;n, la Secretar&iacute;a de Desarrollo Econ&oacute;mico y la Agencia Atenea. Se ofrecen <strong>30.000 cupos de formaci&oacute;n</strong> (10.000 de ciclo largo y 20.000 de ciclos cortos Talento Capital). El sistema de transferencias se integra con <strong>Ingreso M&iacute;nimo Garantizado (IMG)</strong>.</div>
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
                    <h2 class="card-title">Equipo</h2>
                    <p style="line-height:1.7;">El servicio J&oacute;venes con Oportunidades es liderado por un <strong>comit&eacute; intersectorial</strong> compuesto por la Secretar&iacute;a Distrital de Integraci&oacute;n Social, la Secretar&iacute;a de Educaci&oacute;n, la Secretar&iacute;a de Desarrollo Econ&oacute;mico y la Agencia Atenea. La gesti&oacute;n operativa recae en la Subdirecci&oacute;n para la Juventud de la SDIS.</p>

                    <h3 class="card-subtitle">Composici&oacute;n del equipo operativo</h3>
                    <p style="line-height:1.7;">El equipo operativo de JCO se organiza en tres grandes componentes que trabajan de manera articulada:</p>

                    <table style="width:100%; border-collapse:collapse; font-size:0.85rem;">
                        <thead>
                            <tr style="background:#f8f9fa;">
                                <th style="padding:10px; border-bottom:2px solid var(--accent); text-align:left;">Componente</th>
                                <th style="padding:10px; border-bottom:2px solid var(--accent); text-align:left;">Funci&oacute;n</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="background:#fff;">
                                <td style="padding:8px 10px; border-bottom:1px solid #eee; width:200px;"><strong>Psicosocial</strong></td>
                                <td style="padding:8px 10px; border-bottom:1px solid #eee;">Acompa&ntilde;amiento directo a los j&oacute;venes, aplicaci&oacute;n del triage y seguimiento al proyecto de vida.</td>
                            </tr>
                            <tr style="background:#f8f9fa;">
                                <td style="padding:8px 10px; border-bottom:1px solid #eee;"><strong>Ofertas y alertas</strong></td>
                                <td style="padding:8px 10px; border-bottom:1px solid #eee;">Gesti&oacute;n de oportunidades educativas y laborales; seguimiento a vulneraciones de derechos.</td>
                            </tr>
                            <tr style="background:#fff;">
                                <td style="padding:8px 10px; border-bottom:1px solid #eee;"><strong>Apoyo transversal</strong></td>
                                <td style="padding:8px 10px; border-bottom:1px solid #eee;">Unidades de anal&iacute;tica, referentes metodol&oacute;gicos, gesti&oacute;n documental y equipo jur&iacute;dico.</td>
                            </tr>
                        </tbody>
                    </table>
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
                    <div class="rutas-formacion-grid" style="display:grid; grid-template-columns:repeat(3, 1fr); gap:16px; margin-top:18px;">
                        <div style="display:flex; flex-direction:column;">
                            <div style="background:#5f9ea0; color:#fff; padding:10px 16px 10px 14px; font-weight:800; font-size:0.8rem; letter-spacing:0.5px; text-transform:uppercase; clip-path:polygon(0 0, calc(100% - 14px) 0, 100% 50%, calc(100% - 14px) 100%, 0 100%);">Ruta 1</div>
                            <div style="padding:14px 4px 0; border-top:1px dashed #ccc; margin-top:-1px;">
                                <h4 style="color:#253C5C; font-size:0.98rem; font-weight:700; margin:0 0 8px 0;">Educaci&oacute;n para j&oacute;venes y adultos</h4>
                                <p style="font-size:0.85rem; line-height:1.55; color:#555; margin:0;">Para terminar el bachillerato (grados 10&deg; y 11&deg;) en jornadas nocturnas o fines de semana.</p>
                            </div>
                        </div>
                        <div style="display:flex; flex-direction:column;">
                            <div style="background:#e07850; color:#fff; padding:10px 16px 10px 14px; font-weight:800; font-size:0.8rem; letter-spacing:0.5px; text-transform:uppercase; clip-path:polygon(0 0, calc(100% - 14px) 0, 100% 50%, calc(100% - 14px) 100%, 0 100%);">Ruta 2</div>
                            <div style="padding:14px 4px 0; border-top:1px dashed #ccc; margin-top:-1px;">
                                <h4 style="color:#253C5C; font-size:0.98rem; font-weight:700; margin:0 0 8px 0;">Cursos cortos certificados</h4>
                                <p style="font-size:0.85rem; line-height:1.55; color:#555; margin:0;">Formaciones de 40 a 160 horas para adquirir conocimientos t&eacute;cnicos y habilidades pr&aacute;cticas para el empleo.</p>
                            </div>
                        </div>
                        <div style="display:flex; flex-direction:column;">
                            <div style="background:#7b6b99; color:#fff; padding:10px 16px 10px 14px; font-weight:800; font-size:0.8rem; letter-spacing:0.5px; text-transform:uppercase; clip-path:polygon(0 0, calc(100% - 14px) 0, 100% 50%, calc(100% - 14px) 100%, 0 100%);">Ruta 3</div>
                            <div style="padding:14px 4px 0; border-top:1px dashed #ccc; margin-top:-1px;">
                                <h4 style="color:#253C5C; font-size:0.98rem; font-weight:700; margin:0 0 8px 0;">Educaci&oacute;n posmedia de ciclo largo</h4>
                                <p style="font-size:0.85rem; line-height:1.55; color:#555; margin:0;">Acceso a Educaci&oacute;n y Formaci&oacute;n para el Trabajo (EFT) o educaci&oacute;n superior, articul&aacute;ndose con iniciativas como J&oacute;venes a la E.</p>
                            </div>
                        </div>
                    </div>

                    <h3 class="card-subtitle">3. Acompa&ntilde;amiento a la empleabilidad</h3>
                    <p style="line-height:1.7;">Orientaci&oacute;n ocupacional y formaci&oacute;n en habilidades blandas para conectar a los j&oacute;venes con oportunidades laborales (intermediaci&oacute;n laboral).</p>

                    <h3 class="card-subtitle">4. Transferencias monetarias condicionadas</h3>
                    <p style="line-height:1.7;">Apoyos econ&oacute;micos de <strong>$200.000 a $1.200.000</strong> dependiendo de la ruta de formaci&oacute;n elegida. El dinero se entrega por partes a medida que el joven avanza y cumple con sus actividades, a trav&eacute;s de operadores financieros o billeteras digitales (Daviplata, Nequi, Movii, Efecty, Dale).</p>
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
                    <h2 class="card-title">Componente psicosocial y el instrumento de triage</h2>
                    <p style="line-height:1.7;">El <strong>acompa&ntilde;amiento psicosocial</strong> es el eje transversal del servicio. Para iniciar la atenci&oacute;n, el equipo profesional aplica un <strong>instrumento de triage psicosocial</strong> que funciona como herramienta de diagn&oacute;stico inicial del joven.</p>

                    <h3 class="card-subtitle">&iquest;Para qu&eacute; sirve el triage?</h3>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px; margin-top:15px;">
                        <div style="background:#5f9ea0; color:#fff; min-width:180px; padding:14px 24px 14px 18px; display:flex; align-items:center; font-weight:700; font-size:0.9rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">Clasificar el riesgo</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">Eval&uacute;a la vulnerabilidad socioecon&oacute;mica y multidimensional del joven, ubic&aacute;ndolo en un nivel de riesgo (alta, moderada o baja) que determina la intensidad del acompa&ntilde;amiento.</div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#e07850; color:#fff; min-width:180px; padding:14px 24px 14px 18px; display:flex; align-items:center; font-weight:700; font-size:0.9rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">Identificar alertas</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">Detecta situaciones cr&iacute;ticas que requieren intervenci&oacute;n inmediata: <strong>riesgo de reclutamiento</strong>, <strong>consumo de sustancias psicoactivas</strong>, <strong>violencia intrafamiliar</strong> o <strong>barreras en salud mental</strong>.</div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#7b6b99; color:#fff; min-width:180px; padding:14px 24px 14px 18px; display:flex; align-items:center; font-weight:700; font-size:0.9rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">Priorizar</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">Los resultados del triage permiten canalizar a cada joven hacia las ofertas m&aacute;s adecuadas seg&uacute;n su perfil de necesidad, garantizando que las rutas de formaci&oacute;n e intermediaci&oacute;n laboral se ajusten a su realidad.</div>
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
