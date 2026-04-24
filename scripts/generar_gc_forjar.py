# Genera el archivo gestion_conocimiento_forjar_2025.html
# Servicio Forjar Restaurativo - Subdirección para la Juventud, SDIS.
# Separa CSS, sidebar, secciones de contenido y JavaScript en variables
# para facilitar ediciones futuras desde Python.

import os
import sys
import pandas as pd

# Raíz del proyecto (un nivel arriba de scripts/)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVO_SALIDA = os.path.join(BASE, "gestion_conocimiento_forjar_2025.html")
DATOS = os.path.join(BASE, "datos")

# CSS compartido con los demás generadores
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _comun.estilos import css_para
from _comun.aliados import seccion_forjar as seccion_aliados_forjar

# CSS del servicio (base compartido + color propio de Forjar)
CSS = css_para("forjar")

# =====================================================================
# Header
# =====================================================================
HEADER = """\
    <header class="header">
        <div>
            <h1>Gestor de conocimiento - Servicio Forjar Restaurativo</h1>
            <div class="subtitle">Subdirecci&oacute;n para la Juventud | SDIS</div>
        </div>
        <div class="header-btns">
            <a class="home-btn" href="index.html" title="Todos los servicios">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8F4E1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
            </a>
            <div class="home-btn" onclick="showContent('welcome')" title="Inicio Servicio Forjar Restaurativo">
                <img src="imagenes/servicios/forjar.png" alt="Servicio Forjar Restaurativo" style="height:32px; border-radius:16px; object-fit:contain; vertical-align:middle;">
            </div>
        </div>
    </header>"""

# =====================================================================
# Sidebar - secciones de navegación
# =====================================================================
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

# =====================================================================
# Secciones de contenido - cada una identificada por su id
# =====================================================================

SECCION_WELCOME = """\
            <div class="content-section active" id="welcome">
                <div class="welcome-section">
                    <div style="font-family:'Anton','Figtree',sans-serif; font-weight:400; font-size:1.9rem; line-height:1.05; letter-spacing:1px; text-transform:uppercase; background:#2d2a28; color:#f4f5de; padding:14px 24px 11px; margin:0 auto 28px; display:block; width:fit-content; max-width:100%; text-align:center;">Servicio Forjar Restaurativo</div>
                    <p>Servicio de la Subdirecci&oacute;n para la Juventud dirigido a adolescentes y j&oacute;venes de 14 a 28 a&ntilde;os vinculados al Sistema de Responsabilidad Penal para Adolescentes (SRPA). Ofrece acompa&ntilde;amiento integral con enfoque restaurativo, priorizando sanciones no privativas de libertad y el acompa&ntilde;amiento en el medio sociofamiliar.</p>
                    <div style="margin:30px auto 0; max-width:450px;">
                        <img src="imagenes/Forjar.jpg" alt="Servicio Forjar Restaurativo" style="width:100%; border-radius:12px; box-shadow:0 4px 15px rgba(0,0,0,0.1);">
                    </div>
                </div>
            </div>"""

SECCION_LINEA_TIEMPO = """\
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
            </div>"""

SECCION_A_TENER_EN_CUENTA = """\
            <div class="content-section" id="a_tener_en_cuenta">
                <div class="card">
                    <h2 class="card-title">A tener en cuenta</h2>

                    <h3 class="card-subtitle">El nombre refleja un cambio de paradigma</h3>
                    <p style="line-height:1.7;">El servicio antes se conoc&iacute;a como &ldquo;Centros Forjar&rdquo;. La palabra &ldquo;centro&rdquo; fue eliminada porque los j&oacute;venes la asociaban con centros de reclusi&oacute;n, lo que iba en contra del enfoque restaurativo del programa. La referencia correcta es &ldquo;servicio Forjar&rdquo; o &ldquo;servicio Forjar Restaurativo&rdquo;. Nunca &ldquo;Centro Forjar&rdquo;.</p>

                    <h3 class="card-subtitle">Justicia restaurativa, no retributiva</h3>
                    <p style="line-height:1.7;">El servicio se fundamenta en tres pilares: la responsabilizaci&oacute;n, la reparaci&oacute;n del da&ntilde;o y la inclusi&oacute;n social (reintegraci&oacute;n). Se distancia del modelo de justicia retributiva centrado en el castigo.</p>

                    <h3 class="card-subtitle">Atenci&oacute;n a j&oacute;venes mayores de edad</h3>
                    <p style="line-height:1.7;">El Servicio Forjar Restaurativo atiende a j&oacute;venes hasta los 28 a&ntilde;os (11 meses y 29 d&iacute;as) en dos l&iacute;neas: j&oacute;venes que cumplen sanciones por conductas punibles (SRPA, cuando el ingreso ocurri&oacute; antes de los 18 a&ntilde;os) y j&oacute;venes que requieren medidas de protecci&oacute;n y restablecimiento de derechos. Debido a los tiempos de los procesos judiciales, m&aacute;s de la mitad de la poblaci&oacute;n atendida es mayor de edad, por lo que el servicio enfoca su oferta en necesidades de juventud como empleabilidad y emprendimiento.</p>

                    <h3 class="card-subtitle">Cobertura distrital desde tres puntos estrat&eacute;gicos</h3>
                    <p style="line-height:1.7;">Aunque opera f&iacute;sicamente en tres unidades operativas (Suba, Ciudad Bol&iacute;var y Rafael Uribe Uribe), ubicadas en localidades con alta incidencia, Forjar atiende al 100% de la poblaci&oacute;n objetivo del Distrito Capital, recibiendo j&oacute;venes de cualquier localidad.</p>

                    <h3 class="card-subtitle">Continuidad voluntaria despu&eacute;s de la sanci&oacute;n</h3>
                    <p style="line-height:1.7;">El acompa&ntilde;amiento no termina cuando se cumple la orden del juez. La estrategia de acompa&ntilde;amiento al pos-egreso permite a los j&oacute;venes continuar de manera 100% voluntaria por 6 meses a 1 a&ntilde;o, buscando consolidar su proyecto de vida y evitar el retorno a entornos vulnerables sin apoyo institucional.</p>

                    <h3 class="card-subtitle">Cumplimiento de mandatos judiciales</h3>
                    <p style="line-height:1.7;">A diferencia de otros servicios de la Subdirecci&oacute;n, Forjar no es voluntario: da cumplimiento a sanciones y medidas impuestas por autoridades judiciales. Esto significa que la atenci&oacute;n no puede interrumpirse ni postergarse, ya que cualquier falla en la prestaci&oacute;n del servicio puede generar consecuencias legales y disciplinarias para la entidad, adem&aacute;s de afectar directamente el proceso de los j&oacute;venes.</p>
                </div>
            </div>"""

SECCION_EQUIPO = """\
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
            </div>"""

SECCION_UBICACION = """\
            <div class="content-section" id="ubicacion">
                <div class="card">
                    <h2 class="card-title">Ubicaci&oacute;n</h2>
                    <p style="line-height:1.7;">El servicio Forjar Restaurativo opera en <strong>3 unidades operativas</strong> ubicadas en localidades con alta incidencia, con cobertura para el 100% del Distrito Capital.</p>
                    <p style="line-height:1.7;">Aunque opera desde estos puntos, el servicio recibe j&oacute;venes de <strong>cualquier localidad</strong> de Bogot&aacute;.</p>

                    <div style="margin:20px 0;">
                        <iframe src="mapa_forjar.html" width="100%" height="450" style="border:1px solid #e0e0e0; border-radius:8px;" loading="lazy"></iframe>
                    </div>

                    <div style="margin-top:25px;">
                <h3 class="card-subtitle">Directorio</h3>
                <table style="width:100%; border-collapse:collapse; font-size:0.85rem;">
                    <thead>
                        <tr style="background:#f8f9fa;">
                            <th style="padding:10px; border-bottom:2px solid var(--accent); text-align:left;">Unidad operativa</th>
                            <th style="padding:10px; border-bottom:2px solid var(--accent); text-align:left;">Localidad</th>
                            <th style="padding:10px; border-bottom:2px solid var(--accent); text-align:left;">Direcci&oacute;n</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!--FILAS_DIRECTORIO-->
                    </tbody>
                </table>
            </div>
                </div>
            </div>"""

# Generar filas del directorio leyendo el Excel
directorio_excel = os.path.join(DATOS, "directorio_forjar.xlsx")
if os.path.exists(directorio_excel):
    df_dir = pd.read_excel(directorio_excel)
    filas_html = ""
    for idx, row in df_dir.iterrows():
        bg = '#fff' if idx % 2 == 0 else '#f8f9fa'
        link_maps = row.get("Link Google Maps", "")
        direccion = str(row["Dirección"])
        if pd.notna(link_maps) and str(link_maps).strip():
            direccion_html = f'<a href="{link_maps}" target="_blank" style="color:var(--accent);">{direccion}</a>'
        else:
            direccion_html = direccion
        filas_html += f'                        <tr style="background:{bg};">\n'
        filas_html += f'                            <td style="padding:8px 10px; border-bottom:1px solid #eee;"><strong>{row["Nombre unidad operativa"]}</strong></td>\n'
        filas_html += f'                            <td style="padding:8px 10px; border-bottom:1px solid #eee;">{row["Localidad"]}</td>\n'
        filas_html += f'                            <td style="padding:8px 10px; border-bottom:1px solid #eee;">{direccion_html}</td>\n'
        filas_html += f'                        </tr>\n'
    SECCION_UBICACION = SECCION_UBICACION.replace("<!--FILAS_DIRECTORIO-->", filas_html.rstrip())
    print(f"Directorio Forjar generado desde Excel: {len(df_dir)} unidades")
else:
    print("Excel de directorio Forjar no encontrado")

SECCION_MODALIDADES = """\
            <div class="content-section" id="modalidades">
                <div class="card">
                    <h2 class="card-title">Modalidades de atenci&oacute;n</h2>
                    <p style="margin-bottom:8px;">El servicio Forjar Restaurativo da cumplimiento a sanciones no privativas de la libertad en medio abierto y comunitario. Tambi&eacute;n recibe j&oacute;venes para medidas de restablecimiento de derechos y atiende a quienes contin&uacute;an voluntariamente tras cumplir su sanci&oacute;n.</p>
                    <p style="color:#888; font-size:0.88rem; margin-bottom:28px;">Las modalidades se clasifican seg&uacute;n el tipo de medida, sanci&oacute;n o estrategia impuesta por la autoridad competente.</p>

                    <!-- Categor&iacute;a 1: Sanciones no privativas -->
                    <div style="margin-bottom:14px;">
                        <div style="background:#5f9ea0; color:#fff; padding:10px 18px; border-radius:8px 8px 0 0; font-weight:700; font-size:0.95rem;">1. No privativas de la libertad (sanciones)</div>
                        <div style="background:#edf6f6; padding:8px 18px; border-radius:0 0 8px 8px; font-size:0.85rem; color:#555;">Se cumplen en medio abierto, sociofamiliar o comunitario. Buscan la responsabilizaci&oacute;n, reparaci&oacute;n del da&ntilde;o e inclusi&oacute;n social.</div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:10px; border-radius:8px;">
                        <div style="background:#5f9ea0; color:#fff; min-width:160px; padding:14px 20px 14px 16px; display:flex; align-items:center; font-weight:700; font-size:0.88rem; position:relative; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2; position:relative;">Libertad asistida y/o vigilada</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 18px 14px 28px; font-size:0.85rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">Concesi&oacute;n de libertad otorgada por la autoridad judicial con la condici&oacute;n de que el adolescente o joven se someta a supervisi&oacute;n, asistencia y orientaci&oacute;n de un programa especializado. Busca fortalecer la autonom&iacute;a y la reparaci&oacute;n a trav&eacute;s de espacios pedag&oacute;gicos y pr&aacute;cticas restaurativas. <strong>M&iacute;nimo 10 actividades mensuales.</strong></div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:10px; border-radius:8px;">
                        <div style="background:#5f9ea0; color:#fff; min-width:160px; padding:14px 20px 14px 16px; display:flex; align-items:center; font-weight:700; font-size:0.88rem; position:relative; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2; position:relative;">Prestaci&oacute;n de servicios a la comunidad</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 18px 14px 28px; font-size:0.85rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">Ejecuci&oacute;n de acciones no remuneradas para restaurar los lazos afectados, posibilitando la reparaci&oacute;n (directa, indirecta o simb&oacute;lica) a la v&iacute;ctima, la familia o la comunidad. <strong>M&iacute;nimo 32 horas mensuales:</strong> 24 horas de trabajo comunitario y 8 horas de acompa&ntilde;amiento psicosocial.</div>
                    </div>


                    <!-- Categor&iacute;a 2: Apoyo y restablecimiento -->
                    <div style="margin-top:50px; margin-bottom:14px;">
                        <div style="background:#e07850; color:#fff; padding:10px 18px; border-radius:8px 8px 0 0; font-weight:700; font-size:0.95rem;">2. Apoyo y restablecimiento de derechos</div>
                        <div style="background:#fdf0eb; padding:8px 18px; border-radius:0 0 8px 8px; font-size:0.85rem; color:#555;">Medidas complementarias frente a vulneraciones de derechos.</div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:10px; border-radius:8px;">
                        <div style="background:#e07850; color:#fff; min-width:160px; padding:14px 20px 14px 16px; display:flex; align-items:center; font-weight:700; font-size:0.88rem; position:relative; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2; position:relative;">IARAJ</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 18px 14px 28px; font-size:0.85rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;"><strong>Intervenci&oacute;n de apoyo al restablecimiento en administraci&oacute;n de justicia.</strong> Restablecimiento y garant&iacute;a de derechos con orientaci&oacute;n familiar. Apoyo pedag&oacute;gico, psicosocial y psicol&oacute;gico especializado para que el joven comprenda y se responsabilice de los hechos. <strong>M&iacute;nimo 10 actividades mensuales.</strong></div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:10px; border-radius:8px;">
                        <div style="background:#e07850; color:#fff; min-width:160px; padding:14px 20px 14px 16px; display:flex; align-items:center; font-weight:700; font-size:0.88rem; position:relative; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2; position:relative;">RIAJ</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 18px 14px 28px; font-size:0.85rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;"><strong>Ruta integral de atenci&oacute;n para j&oacute;venes.</strong> Dirigida a j&oacute;venes (especialmente mayores de edad) con conflicto con la ley cuya situaci&oacute;n jur&iacute;dica a&uacute;n no ha sido definida. Favorece el acceso a educaci&oacute;n, empleo, emprendimiento, arte, cultura y deporte.</div>
                    </div>

                    <!-- Categor&iacute;a 3: Estrategias transversales -->
                    <div style="margin-top:50px; margin-bottom:14px;">
                        <div style="background:#7b6b99; color:#fff; padding:10px 18px; border-radius:8px 8px 0 0; font-weight:700; font-size:0.95rem;">3. Estrategias transversales de continuidad</div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:10px; border-radius:8px;">
                        <div style="background:#7b6b99; color:#fff; min-width:160px; padding:14px 20px 14px 16px; display:flex; align-items:center; font-weight:700; font-size:0.88rem; position:relative; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2; position:relative;">Pos-egreso</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 18px 14px 28px; font-size:0.85rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">Dirigida a quienes culminaron el cumplimiento de diversas modalidades del SRPA y deciden dar continuidad voluntaria a su proceso. <strong>Acompa&ntilde;amiento por 6 meses a 1 a&ntilde;o</strong> para consolidar la inclusi&oacute;n social y productiva mediante la Ruta de Oportunidades Juveniles.</div>
                    </div>

                </div>
            </div>"""

SECCION_FLUJO_DATOS = """\
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
                            <p style="font-size:0.88rem; color:#555; line-height:1.6; margin:0 0 8px;">El proceso est&aacute; regulado por manuales que definen los roles. Los referentes t&eacute;cnicos revisan mensualmente los datos para ajustes previos a los reportes.</p>
                            <p style="font-size:0.88rem; color:#555; line-height:1.6; margin:0 0 8px;">El tratamiento de datos personales es estrictamente confidencial y se rige por la Ley Estatutaria 1581 de 2012.</p>
                            <p style="font-size:0.88rem; color:#555; line-height:1.6; margin:0;">La informaci&oacute;n depurada sirve como insumo para preparar mensualmente el <strong>Informe Cualitativo y Cuantitativo del Servicio Forjar Restaurativo</strong>, que visibiliza el volumen de atenciones, cumplimiento de metas y avance del modelo.</p>
                        </div>
                    </div>

                    <h3 class="card-subtitle" style="margin-top:30px;">Diagrama de flujo del proceso</h3>
                    <p style="color:#666; font-size:0.85rem; margin-bottom:12px;">Representaci&oacute;n visual del ciclo de recolecci&oacute;n y digitaci&oacute;n en SIRBE para el servicio Forjar Restaurativo.</p>
                    <img src="imagenes/diagrama_flujo_forjar.png" alt="Diagrama de flujo del proceso del ciclo Forjar Restaurativo" style="width:100%; border:1px solid #e0e0e0; border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.05);">
                </div>
            </div>"""

SECCION_DATOS_SIRBE = """\
            <div class="content-section" id="datos_sirbe">
                <div class="card">
                    <h2 class="card-title">Datos SIRBE
                        <span onclick="document.getElementById('sirbe-tooltip-forjar').style.display=document.getElementById('sirbe-tooltip-forjar').style.display==='block'?'none':'block'" style="display:inline-flex; align-items:center; justify-content:center; width:22px; height:22px; border-radius:50%; background:var(--accent); color:#fff; font-size:0.7rem; font-weight:700; cursor:pointer; margin-left:8px; vertical-align:middle;">?</span>
                    </h2>
                    <div id="sirbe-tooltip-forjar" style="display:none; background:#2F3E3C; color:#F8F4E1; border-radius:10px; padding:18px 22px; margin-bottom:18px; font-size:0.88rem; line-height:1.7; position:relative;">
                        <strong>SIRBE</strong> (Sistema de Informaci&oacute;n para el Registro de Beneficiarios) es el aplicativo de datos de la Secretar&iacute;a Distrital de Integraci&oacute;n Social (SDIS) en Bogot&aacute;. Su funci&oacute;n principal es registrar, sistematizar y hacer seguimiento a la informaci&oacute;n de los ciudadanos que acceden a los servicios sociales, proyectos y ayudas de la entidad. La informaci&oacute;n registrada en las &ldquo;Fichas SIRBE&rdquo; es confidencial y su uso se limita a la gesti&oacute;n interna de servicios sociales.
                        <span onclick="document.getElementById('sirbe-tooltip-forjar').style.display='none'" style="position:absolute; top:8px; right:12px; cursor:pointer; opacity:0.6; font-size:1.1rem;">&times;</span>
                    </div>
                    <p style="color:#666; margin-bottom:20px;">C&oacute;mo se estructura el servicio Forjar Restaurativo dentro del sistema de informaci&oacute;n misional SIRBE.</p>

                    <h3 class="card-subtitle">Tipolog&iacute;a en SIRBE</h3>
                    <p style="line-height:1.7;">Forjar funciona en SIRBE bajo la tipolog&iacute;a de <strong>&ldquo;servicio social&rdquo;</strong>.</p>

                    <h3 class="card-subtitle">Entrada al servicio</h3>
                    <p style="line-height:1.7;">Los j&oacute;venes ingresan remitidos por juzgados o por el ICBF, llegan con una historia social, y el primer paso siempre es diligenciar la ficha SIRBE f&iacute;sica espec&iacute;fica para registrar sus datos transversales.</p>

                    <h3 class="card-subtitle">Seguimiento a largo plazo</h3>
                    <p style="line-height:1.7;">Debido a que los j&oacute;venes ingresan para cumplir una sanci&oacute;n, su permanencia en el servicio toma un tiempo prudente. Las modalidades y actuaciones est&aacute;n dise&ntilde;adas para que los j&oacute;venes sigan una ruta, de modo que SIRBE registra todo su historial de movimientos.</p>

                    <h3 class="card-subtitle">Estados adaptados al sistema penal</h3>
                    <p style="line-height:1.7;">A diferencia de otros servicios, Forjar no maneja actuaciones de &ldquo;intervenci&oacute;n&rdquo;. Maneja tres actuaciones de estado:</p>
                    <ul style="margin:10px 0 15px 20px; line-height:2;">
                        <li><span class="badge badge-primary">En atenci&oacute;n</span> El joven se encuentra cumpliendo su sanci&oacute;n o medida activamente</li>
                        <li><span class="badge badge-primary">Egresado</span> El joven ha finalizado el cumplimiento de su sanci&oacute;n</li>
                        <li><span class="badge badge-primary">En incumplimiento</span> Funciona en la pr&aacute;ctica como un estado &ldquo;suspendido&rdquo;, pero se cre&oacute; con este nombre espec&iacute;fico para no generar confusiones con la terminolog&iacute;a oficial del SRPA</li>
                    </ul>
                </div>
            </div>"""

# Iframe de Power BI para estadísticas
POWERBI_SRC = "https://app.powerbi.com/view?r=eyJrIjoiMzRiNWRkMDQtNThmNC00Yzk5LThjNTItOWI4MzZkYzYwM2EzIiwidCI6ImIzZTMwODA4LWU5YTgtNGYyYS05YmMxLWE3NjBhZTkxMGNmNSIsImMiOjR9"

SECCION_ESTADISTICAS = f"""\
            <div class="content-section" id="estadisticas">
                <div class="card">
                    <h2 class="card-title">Estad&iacute;sticas</h2>
                    <iframe title="Seguimiento t&eacute;cnico" width="100%" height="600" src="{POWERBI_SRC}" frameborder="0" allowFullScreen="true" style="border:1px solid #e0e0e0; border-radius:8px;"></iframe>
                </div>
            </div>"""

# =====================================================================
# JavaScript - navegación del sidebar
# =====================================================================
JS_NAVEGACION = """\
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


# =====================================================================
# Ensamblaje del HTML final
# =====================================================================
def ensamblar_html():
    """Combina todas las partes y devuelve el HTML completo."""
    # Secciones de contenido en orden de aparición
    secciones = "\n\n".join([
        SECCION_WELCOME,
        SECCION_LINEA_TIEMPO,
        SECCION_A_TENER_EN_CUENTA,
        SECCION_EQUIPO,
        SECCION_UBICACION,
        SECCION_MODALIDADES,
        SECCION_FLUJO_DATOS,
        SECCION_DATOS_SIRBE,
        seccion_aliados_forjar(),
        SECCION_ESTADISTICAS,
    ])

    html = f"""\
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestor de conocimiento - Servicio Forjar Restaurativo</title>
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
{JS_NAVEGACION}
</script>
</body>
</html>"""
    return html


# =====================================================================
# Escritura del archivo
# =====================================================================
if __name__ == "__main__":
    html = ensamblar_html()
    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Archivo generado: {ARCHIVO_SALIDA}")
