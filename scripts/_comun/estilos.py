"""
CSS base compartido por todos los generadores del gestor de conocimiento.

Antes de abril de 2026 cada generador tenía su propio bloque CSS duplicado
(cuatro copias con pequeñas diferencias). Esto se centralizó aquí para que
cambiar un color o un espaciado afecte a todos los servicios al mismo tiempo.

Uso:

    from _comun.estilos import construir_css

    CSS_BASE = construir_css(accent="#8e6bbf")  # JCO
    CSS_BASE = construir_css(accent="#da686d", accent_bg="#fdf0f2", accent_border="#f5d2d4")  # Alertas

Para agregar reglas específicas de un servicio (como las barras horizontales
de Casas de Juventud), pasar el CSS adicional en el parámetro `extras`, que
se concatena al final y puede hacer override de reglas base.
"""


# Reglas comunes a los cinco generadores (forjar, jco, alertas, home, juventud).
# Usa variables CSS --accent, --accent-bg y --accent-border que se definen
# en el :root generado dinámicamente por construir_css.
_CSS_BASE = """\
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
.sidebar-title { padding: 12px 20px; font-weight: 600; color: var(--accent); cursor: pointer; display: flex; justify-content: space-between; align-items: center; transition: background 0.2s; }
.sidebar-title:hover { background: var(--accent-bg); }
.sidebar-title .arrow { transition: transform 0.2s; }
.sidebar-title.active .arrow { transform: rotate(90deg); }
.sidebar-items { display: none; padding-left: 20px; }
.sidebar-items.show { display: block; }
.sidebar-item { padding: 10px 20px; cursor: pointer; font-size: 0.9rem; color: #3A3A3A; transition: all 0.2s; }
.sidebar-item:hover { background: var(--accent-bg); }
.sidebar-item.active { background: var(--accent-border); color: var(--accent); font-weight: 600; }
.sidebar-link { display: block; padding: 12px 20px; font-weight: 600; color: var(--accent); text-decoration: none; transition: background 0.2s; }
.sidebar-link:hover { background: var(--accent-bg); }
.main-content { flex: 1; padding: 30px; overflow-y: auto; }
.content-section { display: none; }
.content-section.active { display: block; }
.card { background: white; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); padding: 25px; margin-bottom: 20px; }
.card-title { font-size: 1.4rem; color: var(--accent); margin-bottom: 15px; padding-bottom: 10px; border-bottom: 2px solid var(--accent-border); }
.card-subtitle { font-size: 1.15rem; color: var(--accent); font-weight: 500; margin: 25px 0 10px 0; opacity: 0.85; }
.card p { margin-bottom: 15px; }
.badge { display: inline-block; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 500; margin-right: 8px; margin-bottom: 8px; }
.badge-primary { background: var(--accent-border); color: var(--accent); }
.badge-warning { background: #FFF3E0; color: #F58B53; }
.badge-info { background: #e0f4f5; color: #1E9DA3; }
.welcome-section { text-align: center; padding: 60px 20px; }
.welcome-section h2 { font-size: 2rem; color: var(--accent); margin-bottom: 20px; }
.welcome-section p { font-size: 1.1rem; color: #666; max-width: 700px; margin: 0 auto 20px; line-height: 1.7; }
.methodology-box { background: var(--accent-bg); border-left: 4px solid var(--accent); padding: 15px 20px; margin: 15px 0; border-radius: 0 8px 8px 0; }
.pending-box { background: #FFF3E0; border-left: 4px solid #F58B53; padding: 15px 20px; margin: 15px 0; border-radius: 0 8px 8px 0; color: #8B5E3C; }
/* Línea de tiempo */
.timeline { position: relative; padding-left: 30px; margin: 20px 0; }
.timeline::before { content: ''; position: absolute; left: 8px; top: 0; bottom: 0; width: 3px; background: var(--accent-border); }
.timeline-item { position: relative; margin-bottom: 25px; }
.timeline-item::before { content: ''; position: absolute; left: -26px; top: 4px; width: 12px; height: 12px; border-radius: 50%; background: var(--accent); border: 3px solid var(--accent-border); }
.timeline-year { font-weight: 700; color: var(--accent); font-size: 1rem; }
.timeline-text { color: #555; font-size: 0.9rem; margin-top: 4px; line-height: 1.5; }
/* Footer */
.footer { text-align: center; padding: 35px 30px; color: #bbb; font-size: 0.82rem; }
@media (max-width: 768px) {
    .container { flex-direction: column; }
    .sidebar { width: 100%; border-right: none; border-bottom: 1px solid #e0e0e0; }
    .rutas-formacion-grid { grid-template-columns: 1fr !important; gap: 20px !important; }
}"""


# Colores por servicio. Cuando se agrega un servicio nuevo, registrarlo aquí.
COLORES = {
    "juventud": {
        "accent": "#663A93",
        "accent_bg": "#f5f0fa",
        "accent_border": "#ede7f6",
    },
    "forjar": {
        "accent": "#5f9ea0",
        "accent_bg": "#edf6f6",
        "accent_border": "#d4eaeb",
    },
    "jco": {
        "accent": "#8e6bbf",
        "accent_bg": "#f3eef9",
        "accent_border": "#e5ddf0",
    },
    "alertas": {
        "accent": "#da686d",
        "accent_bg": "#fdf0f2",
        "accent_border": "#f5d2d4",
    },
    "home": {
        "accent": "#663A93",
        "accent_bg": "#f5f0fa",
        "accent_border": "#ede7f6",
    },
}


def construir_css(
    accent: str = "#663A93",
    accent_bg: str = "#f5f0fa",
    accent_border: str = "#ede7f6",
    extras: str = "",
) -> str:
    """Devuelve el CSS completo del servicio.

    Construye el bloque `:root` con los colores pedidos, antepone el CSS base
    compartido (que usa las variables --accent, --accent-bg, --accent-border)
    y añade al final las reglas extra del servicio si las hay.
    """
    root = (
        f":root {{ --accent: {accent}; --accent-bg: {accent_bg}; "
        f"--accent-border: {accent_border}; }}\n"
    )
    # Se inserta :root después del @import y del selector universal, para
    # que la cascada CSS funcione igual que antes del refactor.
    lineas = _CSS_BASE.split("\n")
    resultado = []
    root_insertado = False
    for linea in lineas:
        resultado.append(linea)
        if not root_insertado and linea.startswith("* "):
            resultado.append(root.rstrip("\n"))
            root_insertado = True
    base = "\n".join(resultado)
    if extras:
        base += "\n" + extras.strip()
    return base


def css_para(servicio: str, extras: str = "") -> str:
    """Atajo para construir el CSS de un servicio registrado en COLORES."""
    colores = COLORES[servicio]
    return construir_css(
        accent=colores["accent"],
        accent_bg=colores["accent_bg"],
        accent_border=colores["accent_border"],
        extras=extras,
    )
