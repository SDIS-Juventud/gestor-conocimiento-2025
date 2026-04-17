import re

# === HTML GENERATORS ===
def card_2025(nombre, resena):
    return f'''                <div class="card" style="margin-bottom:10px; padding:15px 20px;">
                    <strong style="color:#3A3A3A;">{nombre}</strong>
                    <p style="font-size:0.85rem; color:#666; margin:5px 0 0;">{resena}</p>
                </div>'''

def card_2025_noresena(nombre):
    return f'''                <div class="card" style="margin-bottom:10px; padding:15px 20px;">
                    <strong style="color:#3A3A3A;">{nombre}</strong>
                </div>'''

def card_2026(nombre, proyecto, descripcion):
    return f'''                    <div class="card" style="margin-bottom:10px; padding:15px 20px;">
                        <strong style="color:#3A3A3A;">{nombre}</strong>
                        <p style="font-size:0.85rem; color:#555; margin:5px 0 0;"><em>{proyecto}</em></p>
                        <p style="font-size:0.85rem; color:#666; margin:3px 0 0;">{descripcion}</p>
                    </div>'''

# === DATA ===

# CASAS DE JUVENTUD 2025 (alphabetical)
casas_2025 = [
    ("ANDI / M&aacute;s Pa&iacute;s", "Alianza empresarial para el desarrollo sostenible y productividad nacional."),
    ("Canal Trece", "Medio de comunicaci&oacute;n p&uacute;blico con enfoque en cultura y juventud regional."),
    ("Claro", "Empresa de telecomunicaciones que aporta conectividad y alfabetizaci&oacute;n digital."),
    ("Compensar", "Caja de compensaci&oacute;n familiar con amplia oferta en salud, recreaci&oacute;n y empleo."),
    ("Disruptia", "Especialista en formaci&oacute;n de talento y cierre de brechas de empleabilidad."),
    ("EducaM&aacute;s", "Entidad dedicada a facilitar el acceso y permanencia en la educaci&oacute;n superior."),
    ("Fundaci&oacute;n ANDI", "Brazo social de los industriales que promueve competitividad y equidad."),
    ("Fundaci&oacute;n Gastronom&iacute;a Social", "Usa la cocina como herramienta de formaci&oacute;n e inclusi&oacute;n sociolaboral."),
    ("Fundaci&oacute;n Otero Li&eacute;vano", "Organizaci&oacute;n enfocada en el desarrollo integral de poblaciones vulnerables."),
    ("GOYN (Aspen Institute)", "Red global que busca mejorar el acceso de j&oacute;venes a empleos de calidad."),
    ("Innovers", "Estrategia distrital de formaci&oacute;n t&eacute;cnica y acompa&ntilde;amiento para emprendedores."),
    ("OIT", "Organismo internacional que dicta normas y principios del trabajo decente."),
    ("Red Conecta+Emprende", "Plataforma que facilita el ecosistema de emprendimiento y redes de contacto."),
    ("Sec. Desarrollo Econ&oacute;mico", "Entidad distrital encargada de la productividad y el empleo en Bogot&aacute;."),
    ("Teatro Nacional", "Instituci&oacute;n cultural que fomenta las artes esc&eacute;nicas y la formaci&oacute;n creativa."),
]

# CASAS DE JUVENTUD 2026 (alphabetical)
casas_2026_pre = [
    ("ANDI", "Escuela Distrital de Emprendimiento &middot; M&aacute;s Empleo", "Formaci&oacute;n en emprendimiento y conexi&oacute;n con oportunidades laborales del sector empresarial."),
    ("ATENEA", "Academia Atenea &middot; Horas por Bogot&aacute;", "Acceso a educaci&oacute;n posmedia y ciclo formativo de intervenci&oacute;n comunitaria con fortalecimiento de habilidades socioemocionales."),
    ("C&aacute;mara de Comercio de Bogot&aacute;", "Ruta de formalizaci&oacute;n", "Orientaci&oacute;n a j&oacute;venes emprendedores en la ruta hacia la formalidad mediante 3 masterclass."),
    ("Compensar", "Empleabilidad", "Masterclass mensuales con tips para construcci&oacute;n de hoja de vida y preparaci&oacute;n para entrevistas."),
    ("EducaM&aacute;s", "Data Lab", "Formaci&oacute;n en competencias digitales y an&aacute;lisis de datos para la inserci&oacute;n laboral."),
    ("Fundaci&oacute;n Gastronom&iacute;a Social", "Academia &Ntilde;AM", "Formaci&oacute;n como auxiliares de servicio gastron&oacute;mico con pr&aacute;cticas supervisadas y vinculaci&oacute;n laboral."),
    ("GOYN", "Escuela de liderazgo Potencia Joven", "Fortalecimiento de competencias de liderazgo, gesti&oacute;n de proyectos y conocimiento del sistema de juventud."),
]

idartes_casas = '''                    <div class="card" style="margin-bottom:10px; padding:15px 20px;">
                        <strong style="color:#3A3A3A;">IDARTES</strong>
                        <ul style="font-size:0.85rem; color:#666; margin:8px 0 0; padding-left:18px; line-height:1.8;">
                            <li><em>Circulaci&oacute;n en Festivales al Parque</em> &mdash; plataforma de circulaci&oacute;n art&iacute;stica juvenil</li>
                            <li><em>Formaci&oacute;n Art&iacute;stica CREA + CREA Impulso</em> &mdash; talleres, muestras de procesos y estudios de grabaci&oacute;n</li>
                            <li><em>Libro al Viento</em> &mdash; lectura, escritura y oralidad en territorio</li>
                            <li><em>Artes Pl&aacute;sticas y Visuales</em> &mdash; salidas a Galer&iacute;a Santa Fe, red de museos y arte urbano</li>
                            <li><em>Circulaci&oacute;n Danza</em> &mdash; visibilizaci&oacute;n de procesos r&iacute;tmicos en Festival de la Danza</li>
                            <li><em>Emprendimiento en gesti&oacute;n cultural</em> &mdash; microcurso y visitas a producci&oacute;n de festivales</li>
                        </ul>
                    </div>'''

casas_2026_post = [
    ("La Guarida Art&iacute;stica", "Asistencia a teatro", "Espacios de encuentro y formaci&oacute;n a trav&eacute;s de obras teatrales para las juventudes."),
    ("Mi Banco", "Inclusi&oacute;n financiera", "Talleres de educaci&oacute;n financiera en 6 casas de juventud."),
    ("OIT", "SENA TIC", "Cursos cortos de formaci&oacute;n en habilidades digitales aprovechando las salas de las Casas de Juventud."),
    ("Poderosas", "Salud sexual y reproductiva", "Curr&iacute;culo educativo y brigadas conjuntas en territorio para promover acceso a servicios de salud."),
    ("Sec. Distrital de Cultura", "Centro Cultural Juvenil", "Infraestructura destinada a servicios culturales y de bienestar para j&oacute;venes."),
]

# FORJAR 2025 (alphabetical)
forjar_2025 = [
    ("Bienestar Familiar (ICBF)", "Entidad nacional que trabaja por la prevenci&oacute;n y protecci&oacute;n de menores."),
    ("FUGA", "Entidad que promueve la transformaci&oacute;n del centro de Bogot&aacute; mediante el arte."),
    ("GOYN (Aspen Institute)", "Red global que busca mejorar el acceso de j&oacute;venes a empleos de calidad."),
    ("IDARTES", "Instituto encargado de las pol&iacute;ticas y pr&aacute;cticas art&iacute;sticas en la ciudad."),
    ("IDRD", "Instituto encargado del deporte, la recreaci&oacute;n y el uso del espacio p&uacute;blico."),
    ("La Esquina Redonda", "Proyecto de memoria y cuidado en el Bronx Distrito Creativo."),
    ("Proyecto Sue&ntilde;os", "Iniciativa del ICBF que busca el acceso a oportunidades y derechos de j&oacute;venes bajo medidas de protecci&oacute;n."),
    ("Rebel Business School", None),
    ("Sec. Distrital de Seguridad, Convivencia y Justicia", "Entidad distrital que lidera la convivencia y la justicia restaurativa."),
    ("Secretar&iacute;a de Educaci&oacute;n", "Rector de la pol&iacute;tica educativa en el distrito para niveles b&aacute;sica y media."),
    ("SENA", "Principal entidad p&uacute;blica de formaci&oacute;n t&eacute;cnica y tecnol&oacute;gica en Colombia."),
    ("Sodexo", "Multinacional que ofrece servicios de alimentaci&oacute;n y gesti&oacute;n de instalaciones."),
    ("Teatro Nacional", "Instituci&oacute;n cultural que fomenta las artes esc&eacute;nicas y la formaci&oacute;n creativa."),
    ("World Vision", "ONG internacional de ayuda humanitaria enfocada en la ni&ntilde;ez y juventud."),
]

# FORJAR 2026 (alphabetical)
forjar_2026 = [
    ("ANDI", "M&aacute;s Empleo", "Conexi&oacute;n con oportunidades laborales del sector empresarial."),
    ("ATENEA", "Academia Atenea", "Acceso a educaci&oacute;n posmedia para j&oacute;venes del SRPA."),
    ("Empresas aliadas", "M&aacute;s Manos por Bogot&aacute;", "Voluntariado corporativo: ropero solidario y comidas compartidas con j&oacute;venes."),
    ("ENMENTE", "Articulaci&oacute;n Bienestar", "Apoyo en salud mental y bienestar para j&oacute;venes del servicio."),
    ("IDARTES", "Libro al Viento", "Mediaciones de lectura con enfoque restaurativo y espacios de escritura reflexiva."),
    ("IDRD", "Recreaci&oacute;n y deporte", "Actividades deportivas y recreativas en unidades operativas."),
    ("Mi Banco", "Inclusi&oacute;n financiera", "Formaci&oacute;n en acceso y uso de servicios financieros."),
]

# JCO 2025 (alphabetical)
jco_2025 = [
    ("ANDI / M&aacute;s Pa&iacute;s", "Alianza empresarial para el desarrollo sostenible y productividad nacional."),
    ("ATENEA", "Agencia distrital que financia y gestiona el acceso a la educaci&oacute;n posmedia."),
    ("Educaci&oacute;n Posmedia EFT", "Programas de Educaci&oacute;n Formativa T&eacute;cnica orientados a la inserci&oacute;n laboral r&aacute;pida."),
    ("Red Conecta+Emprende", "Plataforma que facilita el ecosistema de emprendimiento y redes de contacto."),
    ("Sec. Desarrollo Econ&oacute;mico", "Entidad distrital encargada de la productividad y el empleo en Bogot&aacute;."),
    ("Secretar&iacute;a de Educaci&oacute;n", "Rector de la pol&iacute;tica educativa en el distrito para niveles b&aacute;sica y media."),
    ("SENA", "Principal entidad p&uacute;blica de formaci&oacute;n t&eacute;cnica y tecnol&oacute;gica en Colombia."),
]

# JCO 2026 (alphabetical)
jco_2026 = [
    ("ANDI", "M&aacute;s Empleo", "Conexi&oacute;n con oportunidades laborales del sector empresarial."),
    ("Mi Banco", "Inclusi&oacute;n financiera", "Formaci&oacute;n en acceso y uso de servicios financieros."),
]


# === BUILD SECTIONS ===
def build_casas_section():
    cards_2025 = "\n".join([card_2025(n, r) for n, r in casas_2025])
    cards_2026 = "\n".join([card_2026(n, p, d) for n, p, d in casas_2026_pre])
    cards_2026 += "\n" + idartes_casas
    cards_2026 += "\n" + "\n".join([card_2026(n, p, d) for n, p, d in casas_2026_post])

    return f'''            <div class="content-section" id="alianzas" style="display:none;"><div class="card">
                <h2 class="card-title">Aliados</h2>
                <p style="color:#666; margin-bottom:20px;">Aliados estrat&eacute;gicos del servicio Casas de Juventud.</p>

                <div style="background:#fff; border-radius:10px; padding:15px; margin-bottom:25px; text-align:center;">
                    <img src="../imagenes/Aliados/Aliados_Casas de Juventud.png" alt="Aliados estrat&eacute;gicos de Casas de Juventud" style="max-width:100%; border-radius:8px;">
                </div>

{cards_2025}

                <h3 class="card-subtitle" style="font-size:1.1rem; color:#253C5C; margin-top:35px; margin-bottom:15px; padding-top:20px; border-top:1px solid #e0e0e0;">Alianzas 2026</h3>
                <div style="padding-left:0;">
{cards_2026}
                </div>
            </div></div>'''


def build_forjar_section():
    cards_2025 = []
    for n, r in forjar_2025:
        if r:
            cards_2025.append(card_2025(n, r))
        else:
            cards_2025.append(card_2025_noresena(n))
    cards_2025_str = "\n".join(cards_2025)
    cards_2026 = "\n".join([card_2026(n, p, d) for n, p, d in forjar_2026])

    return f'''            <div class="content-section" id="aliados">
                <div class="card">
                    <h2 class="card-title">Aliados estrat&eacute;gicos</h2>
                    <p style="color:#666; margin-bottom:20px;">Entidades y organizaciones que apoyan la operaci&oacute;n del servicio Forjar Restaurativo.</p>
                    <div style="background:#fff; border-radius:10px; padding:15px; margin-bottom:25px; text-align:center;">
                        <img src="imagenes/Aliados/Aliados_Forjar.png" alt="Aliados estrat&eacute;gicos de Forjar" style="max-width:100%; border-radius:8px;">
                    </div>

{cards_2025_str}

                    <h3 class="card-subtitle" style="font-size:1.1rem; color:var(--accent); margin-top:35px; margin-bottom:15px; padding-top:20px; border-top:1px solid #e0e0e0;">Alianzas 2026</h3>
                    <div style="padding-left:0;">
{cards_2026}
                    </div>
                </div>
            </div>'''


def build_jco_section():
    cards_2025 = "\n".join([card_2025(n, r) for n, r in jco_2025])
    cards_2026 = "\n".join([card_2026(n, p, d) for n, p, d in jco_2026])

    return f'''            <div class="content-section" id="aliados">
                <div class="card">
                    <h2 class="card-title">Aliados estrat&eacute;gicos</h2>
                    <p style="color:#666; margin-bottom:20px;">Entidades y organizaciones que apoyan la operaci&oacute;n del servicio J&oacute;venes con Oportunidades.</p>
                    <div style="background:#fff; border-radius:10px; padding:15px; margin-bottom:25px; text-align:center;">
                        <img src="imagenes/Aliados/Aliados_JCO.png" alt="Aliados estrat&eacute;gicos de JCO" style="max-width:100%; border-radius:8px;">
                    </div>

{cards_2025}

                    <h3 class="card-subtitle" style="font-size:1.1rem; color:var(--accent); margin-top:35px; margin-bottom:15px; padding-top:20px; border-top:1px solid #e0e0e0;">Alianzas 2026</h3>
                    <div style="padding-left:0;">
{cards_2026}
                    </div>
                </div>
            </div>'''


# === APPLY TO FILES ===
base = "C:/Users/carol/CH_projects/SDIS/Gestion de conocimiento/gestor-conocimiento-2025"

# EJES
casas_html = build_casas_section()
ejes = ["Bienestar", "Cultura", "Inclusion", "Liderazgo"]
for eje in ejes:
    path = f"{base}/ejes/{eje}.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    pattern = r'<div class="content-section" id="alianzas"[^>]*>.*?</div></div>\s*</main>'
    replacement = casas_html + "\n        </main>"
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"OK: {eje}.html")

# FORJAR
forjar_html = build_forjar_section()
path = f"{base}/gestion_conocimiento_forjar_2025.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
pattern = r'<div class="content-section" id="aliados">.*?</div>\s*</div>\s*</main>'
replacement = forjar_html + "\n        </main>"
content = re.sub(pattern, replacement, content, flags=re.DOTALL)
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("OK: forjar.html")

# JCO
jco_html = build_jco_section()
path = f"{base}/gestion_conocimiento_jco_2025.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
pattern = r'<div class="content-section" id="aliados">.*?</div>\s*</div>\s*</main>'
replacement = jco_html + "\n        </main>"
content = re.sub(pattern, replacement, content, flags=re.DOTALL)
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("OK: jco.html")

print("\nListo!")
