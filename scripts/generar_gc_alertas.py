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
                    <div class="sidebar-item" onclick="showContent('descripcion')">Objetivos</div>
                    <div class="sidebar-item" onclick="showContent('triage')">Detecci&oacute;n de alertas</div>
                    <div class="sidebar-item" onclick="showContent('protocolos')">C&oacute;mo opera</div>
                    <div class="sidebar-item" onclick="showContent('estadisticas')">Estad&iacute;sticas</div>
                </div>
            </div>"""

# Se ensambla el sidebar completo
SIDEBAR_HTML = f"""\
        <nav class="sidebar">
            <div class="sidebar-title" onclick="showContent('welcome')" style="cursor:pointer;"><span>Inicio</span></div>

{SIDEBAR_CONTEXTO}
        </nav>"""

# ─── Secciones de contenido ─────────────────────────────────────────────────
# Cada sección corresponde a un ítem del sidebar.

SECCION_WELCOME = """\
            <div class="content-section active" id="welcome">
                <div class="welcome-section">
                    <div style="font-family:'Anton','Figtree',sans-serif; font-weight:400; font-size:1.9rem; line-height:1.05; letter-spacing:1px; text-transform:uppercase; background:#2d2a28; color:#f4f5de; padding:14px 24px 11px; margin:0 auto 28px; display:block; width:fit-content; max-width:100%; text-align:center;">Parche seguro</div>
                    <p>Sistema de identificaci&oacute;n y seguimiento de alertas tempranas para la protecci&oacute;n integral de la poblaci&oacute;n joven. A partir del triage psicosocial, el equipo identifica situaciones de riesgo y activa los protocolos de atenci&oacute;n correspondientes.</p>
                    <div style="margin:30px auto 0; max-width:450px;">
                        <img src="imagenes/alertas.jpeg" alt="Parche seguro" style="width:100%; border-radius:12px; box-shadow:0 4px 15px rgba(0,0,0,0.1);">
                    </div>
                </div>
            </div>"""

SECCION_DESCRIPCION = """\
            <div class="content-section" id="descripcion">
                <div class="card">
                    <h2 class="card-title">Objetivos</h2>

                    <h3 class="card-subtitle">Objetivo general</h3>
                    <p style="line-height:1.7;">Implementar una estrategia integral de prevenci&oacute;n, atenci&oacute;n y fortalecimiento de capacidades que permita mejorar las condiciones de vida de los y las j&oacute;venes vinculadas a los servicios de la Subdirecci&oacute;n para la Juventud, mediante el establecimiento de rutas de atenci&oacute;n a alertas, articulaciones interinstitucionales y acompa&ntilde;amiento t&eacute;cnico a los equipos territoriales.</p>

                    <h3 class="card-subtitle">Objetivos espec&iacute;ficos</h3>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#5f9ea0; color:#fff; min-width:72px; padding:14px 24px 14px 18px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.6rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">1</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.9rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">
                            <strong>Prevenci&oacute;n y fortalecimiento de capacidades.</strong> Implementar acciones para la prevenci&oacute;n, formaci&oacute;n y atenciones colectivas que mejoren las condiciones de vida de los j&oacute;venes, en coordinaci&oacute;n con los equipos territoriales y de anal&iacute;tica.
                        </div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#e07850; color:#fff; min-width:72px; padding:14px 24px 14px 18px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.6rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">2</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.9rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">
                            <strong>Rutas de atenci&oacute;n.</strong> Establecer las rutas de atenci&oacute;n frente a las alertas que se generen en los servicios de la Subdirecci&oacute;n para la Juventud.
                        </div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#7b6b99; color:#fff; min-width:72px; padding:14px 24px 14px 18px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.6rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">3</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.9rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">
                            <strong>Articulaci&oacute;n interinstitucional.</strong> Articular con entidades p&uacute;blicas y privadas a nivel distrital que cuentan con oferta de servicios para la atenci&oacute;n de las alertas reportadas por los j&oacute;venes.
                        </div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#d4a84b; color:#fff; min-width:72px; padding:14px 24px 14px 18px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.6rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">4</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.9rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">
                            <strong>Asesor&iacute;a t&eacute;cnica.</strong> Brindar asesor&iacute;a a los equipos territoriales de la Subdirecci&oacute;n para la identificaci&oacute;n, gesti&oacute;n y remisi&oacute;n de las alertas presentadas por los j&oacute;venes participantes.
                        </div>
                    </div>
                </div>
            </div>"""

SECCION_TRIAGE = """\
            <div class="content-section" id="triage">
                <div class="card">
                    <h2 class="card-title">Detecci&oacute;n de alertas</h2>
                    <p style="line-height:1.7;">La detecci&oacute;n de alertas es la primera etapa del trabajo de Parche seguro. Un gestor o profesional psicosocial identifica si el joven presenta alguna situaci&oacute;n de riesgo: problemas de salud, consumo de sustancias, riesgos de salud mental u otras vulnerabilidades. Posteriormente se clasifica la urgencia y se activa la ruta de atenci&oacute;n correspondiente.</p>

                    <h3 class="card-subtitle">&iquest;Para qu&eacute; sirve?</h3>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px; margin-top:15px;">
                        <div style="background:#5f9ea0; color:#fff; min-width:180px; padding:14px 24px 14px 18px; display:flex; align-items:center; font-weight:700; font-size:0.9rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">Identificar y clasificar alertas</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">Detecta situaciones de vulneraci&oacute;n de derechos y las clasifica. Identifica alertas inmediatas con alto riesgo (como <strong>prevenci&oacute;n del suicidio</strong> y <strong>violencia intrafamiliar</strong>) y alertas mediatas (como <strong>salud mental</strong> o <strong>prevenci&oacute;n del consumo de sustancias psicoactivas</strong>).</div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#e07850; color:#fff; min-width:180px; padding:14px 24px 14px 18px; display:flex; align-items:center; font-weight:700; font-size:0.9rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">Definir el nivel de acompa&ntilde;amiento</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">Los resultados canalizan al joven hacia la atenci&oacute;n adecuada seg&uacute;n la urgencia: <strong>Salas de Escucha Especializadas</strong> (riesgos inmediatos), <strong>Salas de Escucha Psicosocial</strong> (riesgos mediatos) o ruta <strong>Te conectamos</strong> (situaciones que limitan el acceso a ofertas o el goce de derechos).</div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#7b6b99; color:#fff; min-width:180px; padding:14px 24px 14px 18px; display:flex; align-items:center; font-weight:700; font-size:0.9rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">Referenciaci&oacute;n institucional</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">Facilita la conexi&oacute;n y referenciaci&oacute;n del joven hacia otros servicios que brinda la Secretar&iacute;a Distrital de Integraci&oacute;n Social y el Distrito Capital.</div>
                    </div>

                    <h3 class="card-subtitle">Las tres categor&iacute;as de alertas</h3>
                    <p style="line-height:1.7;">Las alertas se clasifican en tres grupos seg&uacute;n la urgencia de atenci&oacute;n que demandan:</p>

                    <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:18px; margin:20px 0;">
                        <div style="background:#2B2F3A; border-radius:12px; padding:20px; box-shadow:7px 7px 0 #f5b8a8; color:#fff;">
                            <h4 style="font-size:0.95rem; color:#fff; margin:0 0 10px; font-weight:700;">Alertas inmediatas</h4>
                            <p style="font-size:0.82rem; color:rgba(255,255,255,0.85); margin:0; line-height:1.55;">Situaciones que ponen en riesgo inminente la vida o la integridad del o la joven y requieren atenci&oacute;n prioritaria. Los j&oacute;venes son canalizados a las Salas de Escucha Especializadas.</p>
                        </div>
                        <div style="background:#2B2F3A; border-radius:12px; padding:20px; box-shadow:7px 7px 0 #f2c89a; color:#fff;">
                            <h4 style="font-size:0.95rem; color:#fff; margin:0 0 10px; font-weight:700;">Alertas mediatas</h4>
                            <p style="font-size:0.82rem; color:rgba(255,255,255,0.85); margin:0; line-height:1.55;">Situaciones que desmejoran la calidad de vida y afectan el bienestar integral, sin implicar riesgo para la vida. Se canalizan a las Salas de Escucha Psicosocial.</p>
                        </div>
                        <div style="background:#2B2F3A; border-radius:12px; padding:20px; box-shadow:7px 7px 0 #9ed4ab; color:#fff;">
                            <h4 style="font-size:0.95rem; color:#fff; margin:0 0 10px; font-weight:700;">Te conectamos</h4>
                            <p style="font-size:0.82rem; color:rgba(255,255,255,0.85); margin:0; line-height:1.55;">Situaciones que impiden el goce de derechos fundamentales o limitan el acceso a ofertas. Habilitan la vinculaci&oacute;n del joven a programas y estrategias de otras entidades distritales.</p>
                        </div>
                    </div>
                </div>
            </div>"""

SECCION_PROTOCOLOS = """\
            <div class="content-section" id="protocolos">
                <div class="card">
                    <h2 class="card-title">C&oacute;mo opera</h2>
                    <p style="line-height:1.7;">El equipo de Parche seguro opera a partir de una <strong>ruta metodol&oacute;gica</strong> que va desde la detecci&oacute;n de la alerta hasta el cierre del caso. A continuaci&oacute;n se describe la tipolog&iacute;a completa de alertas, los instrumentos que usa el equipo, el flujo de atenci&oacute;n y los estados de seguimiento.</p>

                    <h3 class="card-subtitle">Diagrama de alertas</h3>
                    <p style="line-height:1.7;">Cada alerta tiene un <strong>tipo</strong> (inmediata, mediata o &ldquo;te conectamos&rdquo;) y uno o varios <strong>subtipos</strong>. La tabla consolida todas las alertas que gestiona el equipo.</p>

                    <div style="overflow-x:auto; margin:18px 0 30px;">
                        <table style="width:100%; border-collapse:collapse; font-size:0.85rem;">
                            <thead>
                                <tr style="background:#2F3E3C; color:#F8F4E1;">
                                    <th style="padding:12px 14px; text-align:left; font-weight:700;">Nombre de la alerta</th>
                                    <th style="padding:12px 14px; text-align:left; font-weight:700; width:130px;">Tipo</th>
                                    <th style="padding:12px 14px; text-align:left; font-weight:700;">Subtipos</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr style="background:#fafafa; border-bottom:1px solid #e0e0e0;">
                                    <td style="padding:12px 14px; vertical-align:top;"><strong>Amenazas a la vida</strong></td>
                                    <td style="padding:12px 14px; vertical-align:top;"><span style="display:inline-block; padding:3px 10px; border-radius:10px; background:#d93a5c; color:#fff; font-size:0.72rem; font-weight:700; text-transform:uppercase;">Inmediata</span></td>
                                    <td style="padding:12px 14px; vertical-align:top; color:#666;">No aplica</td>
                                </tr>
                                <tr style="background:#fff; border-bottom:1px solid #e0e0e0;">
                                    <td style="padding:12px 14px; vertical-align:top;"><strong>Amenazas a l&iacute;deres y lideresas</strong></td>
                                    <td style="padding:12px 14px; vertical-align:top;"><span style="display:inline-block; padding:3px 10px; border-radius:10px; background:#d93a5c; color:#fff; font-size:0.72rem; font-weight:700; text-transform:uppercase;">Inmediata</span></td>
                                    <td style="padding:12px 14px; vertical-align:top; color:#666;">No aplica</td>
                                </tr>
                                <tr style="background:#fafafa; border-bottom:1px solid #e0e0e0;">
                                    <td style="padding:12px 14px; vertical-align:top;"><strong>Violencias</strong></td>
                                    <td style="padding:12px 14px; vertical-align:top;"><span style="display:inline-block; padding:3px 10px; border-radius:10px; background:#d93a5c; color:#fff; font-size:0.72rem; font-weight:700; text-transform:uppercase;">Inmediata</span></td>
                                    <td style="padding:12px 14px; vertical-align:top;">Violencia intrafamiliar &middot; Violencia basada en g&eacute;nero / LGBTIQ+ &middot; Bullying</td>
                                </tr>
                                <tr style="background:#fff; border-bottom:1px solid #e0e0e0;">
                                    <td style="padding:12px 14px; vertical-align:top;"><strong>Violencia sexual</strong></td>
                                    <td style="padding:12px 14px; vertical-align:top;"><span style="display:inline-block; padding:3px 10px; border-radius:10px; background:#d93a5c; color:#fff; font-size:0.72rem; font-weight:700; text-transform:uppercase;">Inmediata</span></td>
                                    <td style="padding:12px 14px; vertical-align:top; font-size:0.8rem;">Acceso carnal violento &middot; Acto sexual violento &middot; Acceso carnal o acto sexual en persona puesta en incapacidad de resistir &middot; Acceso carnal abusivo con menor de 14 a&ntilde;os &middot; Actos sexuales con menor de 14 a&ntilde;os &middot; Acceso carnal o acto sexual abusivos con incapaz de resistir &middot; Acoso sexual &middot; Inducci&oacute;n a la prostituci&oacute;n &middot; Proxenetismo con menor de edad &middot; Constre&ntilde;imiento a la prostituci&oacute;n &middot; Est&iacute;mulo a la prostituci&oacute;n de menores &middot; Pornograf&iacute;a con menores de 18 a&ntilde;os &middot; Turismo sexual &middot; Omisi&oacute;n de denuncia</td>
                                </tr>
                                <tr style="background:#fafafa; border-bottom:1px solid #e0e0e0;">
                                    <td style="padding:12px 14px; vertical-align:top;"><strong>Riesgo de habitabilidad en calle</strong></td>
                                    <td style="padding:12px 14px; vertical-align:top;"><span style="display:inline-block; padding:3px 10px; border-radius:10px; background:#d93a5c; color:#fff; font-size:0.72rem; font-weight:700; text-transform:uppercase;">Inmediata</span></td>
                                    <td style="padding:12px 14px; vertical-align:top; color:#666;">No aplica</td>
                                </tr>
                                <tr style="background:#fff; border-bottom:1px solid #e0e0e0;">
                                    <td style="padding:12px 14px; vertical-align:top;"><strong>Situaciones cr&iacute;ticas de salud</strong></td>
                                    <td style="padding:12px 14px; vertical-align:top;"><span style="display:inline-block; padding:3px 10px; border-radius:10px; background:#d93a5c; color:#fff; font-size:0.72rem; font-weight:700; text-transform:uppercase;">Inmediata</span></td>
                                    <td style="padding:12px 14px; vertical-align:top;">Enfermedades cr&oacute;nicas y situaciones de salud sin atenci&oacute;n &middot; Emergencias de salud en el marco de las actividades condicionadas</td>
                                </tr>
                                <tr style="background:#fafafa; border-bottom:1px solid #e0e0e0;">
                                    <td style="padding:12px 14px; vertical-align:top;"><strong>Conducta suicida</strong></td>
                                    <td style="padding:12px 14px; vertical-align:top;"><span style="display:inline-block; padding:3px 10px; border-radius:10px; background:#d93a5c; color:#fff; font-size:0.72rem; font-weight:700; text-transform:uppercase;">Inmediata</span></td>
                                    <td style="padding:12px 14px; vertical-align:top;">Ideaci&oacute;n &middot; Amenaza &middot; Intento</td>
                                </tr>
                                <tr style="background:#fff; border-bottom:1px solid #e0e0e0;">
                                    <td style="padding:12px 14px; vertical-align:top;"><strong>Salud mental</strong></td>
                                    <td style="padding:12px 14px; vertical-align:top;"><span style="display:inline-block; padding:3px 10px; border-radius:10px; background:#e67e22; color:#fff; font-size:0.72rem; font-weight:700; text-transform:uppercase;">Mediata</span></td>
                                    <td style="padding:12px 14px; vertical-align:top;">Riesgos psicosociales con barreras de acceso a salud &middot; Trastornos mentales diagnosticados con barreras de acceso a salud</td>
                                </tr>
                                <tr style="background:#fafafa; border-bottom:1px solid #e0e0e0;">
                                    <td style="padding:12px 14px; vertical-align:top;"><strong>Consumo de SPA</strong></td>
                                    <td style="padding:12px 14px; vertical-align:top;"><span style="display:inline-block; padding:3px 10px; border-radius:10px; background:#e67e22; color:#fff; font-size:0.72rem; font-weight:700; text-transform:uppercase;">Mediata</span></td>
                                    <td style="padding:12px 14px; vertical-align:top;">Consumo problem&aacute;tico de sustancias psicoactivas</td>
                                </tr>
                                <tr style="background:#fff; border-bottom:1px solid #e0e0e0;">
                                    <td style="padding:12px 14px; vertical-align:top;"><strong>Personas sin aseguramiento en salud</strong></td>
                                    <td style="padding:12px 14px; vertical-align:top;"><span style="display:inline-block; padding:3px 10px; border-radius:10px; background:#e67e22; color:#fff; font-size:0.72rem; font-weight:700; text-transform:uppercase;">Mediata</span></td>
                                    <td style="padding:12px 14px; vertical-align:top; color:#666;">No aplica</td>
                                </tr>
                                <tr style="background:#fafafa; border-bottom:1px solid #e0e0e0;">
                                    <td style="padding:12px 14px; vertical-align:top;"><strong>Cuidadoras</strong></td>
                                    <td style="padding:12px 14px; vertical-align:top;"><span style="display:inline-block; padding:3px 10px; border-radius:10px; background:#3aa064; color:#fff; font-size:0.72rem; font-weight:700; text-transform:uppercase;">Te conectamos</span></td>
                                    <td style="padding:12px 14px; vertical-align:top;">J&oacute;venes con alta carga de cuidado</td>
                                </tr>
                                <tr style="background:#fff; border-bottom:1px solid #e0e0e0;">
                                    <td style="padding:12px 14px; vertical-align:top;"><strong>Gestantes y lactantes</strong></td>
                                    <td style="padding:12px 14px; vertical-align:top;"><span style="display:inline-block; padding:3px 10px; border-radius:10px; background:#3aa064; color:#fff; font-size:0.72rem; font-weight:700; text-transform:uppercase;">Te conectamos</span></td>
                                    <td style="padding:12px 14px; vertical-align:top;">Mujeres en estado de embarazo &middot; Lactantes hasta los 2 a&ntilde;os del ni&ntilde;o o ni&ntilde;a</td>
                                </tr>
                                <tr style="background:#fafafa; border-bottom:1px solid #e0e0e0;">
                                    <td style="padding:12px 14px; vertical-align:top;"><strong>Menores de 5 a&ntilde;os sin educaci&oacute;n inicial</strong></td>
                                    <td style="padding:12px 14px; vertical-align:top;"><span style="display:inline-block; padding:3px 10px; border-radius:10px; background:#3aa064; color:#fff; font-size:0.72rem; font-weight:700; text-transform:uppercase;">Te conectamos</span></td>
                                    <td style="padding:12px 14px; vertical-align:top;">Ni&ntilde;os o ni&ntilde;as de 0 a 5 a&ntilde;os</td>
                                </tr>
                                <tr style="background:#fff;">
                                    <td style="padding:12px 14px; vertical-align:top;"><strong>Orientaci&oacute;n jur&iacute;dica</strong></td>
                                    <td style="padding:12px 14px; vertical-align:top;"><span style="display:inline-block; padding:3px 10px; border-radius:10px; background:#3aa064; color:#fff; font-size:0.72rem; font-weight:700; text-transform:uppercase;">Te conectamos</span></td>
                                    <td style="padding:12px 14px; vertical-align:top;">Definici&oacute;n de situaci&oacute;n militar &middot; Comparendos &middot; Alimentos, visitas y custodia &middot; Otros</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <h3 class="card-subtitle">Formulario de alertas</h3>
                    <p style="line-height:1.7;">El primer paso para gestionar cualquier alerta es la captaci&oacute;n de la informaci&oacute;n y el registro de los casos. Una vez el profesional psicosocial identifica una alerta, diligencia un formulario de Outlook que recolecta la informaci&oacute;n necesaria para cada tipo de alerta, con &iacute;tems adaptados a lo que las entidades receptoras requieren al momento de hacer la canalizaci&oacute;n.</p>

                    <p style="line-height:1.7;">El formulario tiene preguntas ramificadas, de modo que el enrutamiento posterior no requiere volver a preguntarle al profesional o al joven. En el caso de las alertas inmediatas o de atenci&oacute;n urgente, cada equipo de alertas define los medios de comunicaci&oacute;n con los equipos territoriales que reportan la situaci&oacute;n.</p>

                    <h3 class="card-subtitle">Base de datos de alertas</h3>
                    <p style="line-height:1.7;">Cuando la informaci&oacute;n est&aacute; cargada, el equipo de anal&iacute;tica la descarga semanalmente y la organiza en un Excel centralizado con todas las alertas de la Subdirecci&oacute;n. En esta base se puede filtrar por tipolog&iacute;a y consultar el estado y los seguimientos de cada caso, para tener un panorama actualizado de su evoluci&oacute;n y detectar los casos m&aacute;s complejos que requieren ajustes en la ruta de enrutamiento.</p>

                    <h3 class="card-subtitle">Ruta de atenci&oacute;n en 4 pasos</h3>
                    <p style="line-height:1.7;">El flujo de atenci&oacute;n de cada alerta pasa por cuatro momentos:</p>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px; margin-top:15px;">
                        <div style="background:#d93a5c; color:#fff; min-width:160px; padding:14px 24px 14px 18px; display:flex; align-items:center; font-weight:700; font-size:0.95rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">1. Recepci&oacute;n</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">El profesional psicosocial identifica la alerta en intervenciones, salas de escucha o reportes. Busca un espacio seguro para conversar y determina la urgencia: <strong>urgente</strong> (riesgo inminente → llamar al 123, informar al l&iacute;der de alertas y luego reportar), <strong>no urgente</strong> (deterioro progresivo → contactar l&iacute;der y registrar) o <strong>te conectamos</strong> (limita el acceso a ofertas → registro directo).</div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#3aa064; color:#fff; min-width:160px; padding:14px 24px 14px 18px; display:flex; align-items:center; font-weight:700; font-size:0.95rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">2. Reporte</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">El psicosocial diligencia el <strong>formulario de alertas</strong> con todos los datos requeridos. El l&iacute;der de alertas de cada servicio recibe semanalmente el consolidado generado por anal&iacute;tica para continuar con el enrutamiento.</div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#4a7ba7; color:#fff; min-width:160px; padding:14px 24px 14px 18px; display:flex; align-items:center; font-weight:700; font-size:0.95rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">3. Enrutamiento</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">El equipo de alertas de cada servicio activa la ruta correspondiente. Las <strong>alertas urgentes</strong> se enrutan de forma inmediata apenas se diligencia el formulario. Las <strong>no urgentes</strong> se enrutan semanalmente con el consolidado que env&iacute;a anal&iacute;tica.</div>
                    </div>

                    <div style="display:flex; align-items:stretch; margin-bottom:12px; border-radius:8px;">
                        <div style="background:#e67e22; color:#fff; min-width:160px; padding:14px 24px 14px 18px; display:flex; align-items:center; font-weight:700; font-size:0.95rem; clip-path:polygon(0 0, calc(100% - 20px) 0, 100% 50%, calc(100% - 20px) 100%, 0 100%); z-index:2;">4. Seguimiento</div>
                        <div style="background:#2F3E3C; color:#F8F4E1; flex:1; padding:14px 20px 14px 28px; font-size:0.88rem; line-height:1.6; margin-left:-20px; border-radius:0 8px 8px 0;">Se verifica el estado del caso en <strong>SIVIGILA</strong> y se contrasta con la informaci&oacute;n del psicosocial. El <strong>primer seguimiento</strong> se hace a los 5 d&iacute;as de creada la alerta y los <strong>tres posteriores</strong> cada 2 meses. Tambi&eacute;n hay mesas de seguimiento con l&iacute;deres de alertas, coordinadores e instituciones.</div>
                    </div>

                    <h3 class="card-subtitle">Estados de seguimiento</h3>
                    <p style="line-height:1.7;">Cada alerta puede terminar en uno de los siguientes estados, seg&uacute;n su evoluci&oacute;n:</p>

                    <div style="overflow-x:auto; margin:18px 0 30px;">
                        <table style="width:100%; border-collapse:collapse; font-size:0.87rem;">
                            <thead>
                                <tr style="background:#2F3E3C; color:#F8F4E1;">
                                    <th style="padding:12px 14px; text-align:left; font-weight:700; width:240px;">Estado</th>
                                    <th style="padding:12px 14px; text-align:left; font-weight:700;">Definici&oacute;n</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr style="background:#fafafa; border-bottom:1px solid #e0e0e0;"><td style="padding:12px 14px;"><strong>Atendido por servicio</strong></td><td style="padding:12px 14px;">El caso fue atendido por la entidad competente de la Secretar&iacute;a Distrital de Integraci&oacute;n Social.</td></tr>
                                <tr style="background:#fff; border-bottom:1px solid #e0e0e0;"><td style="padding:12px 14px;"><strong>En lista de espera</strong></td><td style="padding:12px 14px;">Cumpli&oacute; con todo el proceso dentro de la entidad competente y se encuentra en espera de atenci&oacute;n.</td></tr>
                                <tr style="background:#fafafa; border-bottom:1px solid #e0e0e0;"><td style="padding:12px 14px;"><strong>No cumple con requisitos</strong></td><td style="padding:12px 14px;">No cumple con los requisitos para el ingreso al servicio de la entidad competente.</td></tr>
                                <tr style="background:#fff; border-bottom:1px solid #e0e0e0;"><td style="padding:12px 14px;"><strong>No requiere atenci&oacute;n</strong></td><td style="padding:12px 14px;">Al verificar la situaci&oacute;n el o la joven reporta que ya se solucion&oacute; y no desea reportar a ninguna entidad.</td></tr>
                                <tr style="background:#fafafa; border-bottom:1px solid #e0e0e0;"><td style="padding:12px 14px;"><strong>No se puede contactar</strong></td><td style="padding:12px 14px;">Se intent&oacute; contactar 3 veces al joven y no fue posible establecer ning&uacute;n tipo de contacto.</td></tr>
                                <tr style="background:#fff; border-bottom:1px solid #e0e0e0;"><td style="padding:12px 14px;"><strong>Ya estaba en el servicio</strong></td><td style="padding:12px 14px;">Ya se hab&iacute;a reportado la situaci&oacute;n con anterioridad a la entidad competente.</td></tr>
                                <tr style="background:#fafafa; border-bottom:1px solid #e0e0e0;"><td style="padding:12px 14px;"><strong>No desea la atenci&oacute;n</strong></td><td style="padding:12px 14px;">No desea acceder al servicio o proceso para atender la situaci&oacute;n reportada.</td></tr>
                                <tr style="background:#fff;"><td style="padding:12px 14px;"><strong>Cierre del caso</strong></td><td style="padding:12px 14px;">Finalizaci&oacute;n del seguimiento de la situaci&oacute;n reportada.</td></tr>
                            </tbody>
                        </table>
                    </div>

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

{SECCION_TRIAGE}

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
