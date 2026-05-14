"""
Diagramas de flujo SVG embebidos para los servicios JCO, Casas de Juventud
y Forjar Restaurativo.

Antes vivían como PNG (imagenes/diagrama_flujo_*.png) con errores de tipeo
heredados del documento original. Ahora se generan como SVG dentro del
propio HTML para que:

  - Compartan la misma tipografía del gestor (Anton / Antonio / Figtree).
  - Escalen sin pixelarse en cualquier zoom.
  - El texto sea seleccionable y se pueda editar directamente desde Python
    sin tener que abrir un editor gráfico.

Uso:

    from _comun.diagramas_flujo import svg_diagrama_jco
    html = f'<div class="diagrama-wrap">{svg_diagrama_jco()}</div>'

Cada función devuelve un string SVG completo (incluye <svg>...</svg>).
"""

# Tipografías y colores compartidos por los 3 diagramas. Coinciden con la
# identidad visual del resto del gestor.
FUENTE_TITULO = "'Anton', 'Antonio', 'Segoe UI', sans-serif"
FUENTE_HEADER = "'Antonio', 'Anton', 'Figtree', sans-serif"
FUENTE_TEXTO = "'Figtree', 'Segoe UI', sans-serif"
COLOR_FONDO_HEADER = "#2d2a28"   # negro cálido del header del gestor
COLOR_CREMA = "#f4f5de"          # crema institucional
COLOR_TEXTO = "#2F3E3C"          # gris verdoso oscuro del cuerpo
COLOR_LINEA = "#9aa3a1"          # gris medio para flechas
COLOR_RAIL_BG = "#fafafa"        # fondo suave de cada carril
COLOR_RAIL_BORDE = "#e0e2dc"     # separador entre carriles


def _hex_a_rgb(hex_color):
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _mezcla_con_blanco(hex_color, factor=0.85):
    """Aclara un color mezclándolo con blanco. factor=0 deja el color,
    factor=1 lo vuelve blanco."""
    r, g, b = _hex_a_rgb(hex_color)
    r = int(r + (255 - r) * factor)
    g = int(g + (255 - g) * factor)
    b = int(b + (255 - b) * factor)
    return f"#{r:02x}{g:02x}{b:02x}"


def _caja_actividad(x, y, ancho, alto, texto, color_servicio):
    """Rectángulo redondeado con borde del color del servicio. Para pasos
    de actividad normales."""
    color_relleno = _mezcla_con_blanco(color_servicio, 0.92)
    return f"""
    <g>
      <rect x="{x}" y="{y}" width="{ancho}" height="{alto}" rx="6" ry="6"
            fill="{color_relleno}" stroke="{color_servicio}" stroke-width="1.5"/>
      {_texto_centrado(x + ancho / 2, y + alto / 2, ancho - 16, texto)}
    </g>"""


def _caja_decision(cx, cy, ancho, alto, texto):
    """Rombo para decisión (sí/no)."""
    medio_w = ancho / 2
    medio_h = alto / 2
    puntos = f"{cx},{cy - medio_h} {cx + medio_w},{cy} {cx},{cy + medio_h} {cx - medio_w},{cy}"
    return f"""
    <g>
      <polygon points="{puntos}" fill="#ffffff" stroke="{COLOR_TEXTO}" stroke-width="1.5"/>
      {_texto_centrado(cx, cy, ancho - 24, texto, tam=10.5)}
    </g>"""


def _caja_fin(x, y, ancho, alto, texto, color_servicio):
    """Caja final del proceso: fondo del color del servicio, texto crema."""
    return f"""
    <g>
      <rect x="{x}" y="{y}" width="{ancho}" height="{alto}" rx="6" ry="6"
            fill="{color_servicio}" stroke="{color_servicio}" stroke-width="1.5"/>
      {_texto_centrado(x + ancho / 2, y + alto / 2, ancho - 16, texto,
                       color=COLOR_CREMA, peso=700, tam=12)}
    </g>"""


def _texto_centrado(cx, cy, ancho_max, texto, color=None, peso=600, tam=11):
    """Texto centrado con quiebre automático de línea en hasta 3 líneas.
    Aproxima el ancho del carácter para decidir cuándo cortar."""
    if color is None:
        color = COLOR_TEXTO
    palabras = texto.split()
    lineas = []
    actual = ""
    # 0.58em por carácter es una aproximación razonable para Figtree 600.
    chars_max = max(8, int(ancho_max / (tam * 0.55)))
    for palabra in palabras:
        if not actual:
            actual = palabra
        elif len(actual) + 1 + len(palabra) <= chars_max:
            actual += " " + palabra
        else:
            lineas.append(actual)
            actual = palabra
    if actual:
        lineas.append(actual)
    if len(lineas) > 3:
        lineas = lineas[:2] + [" ".join(lineas[2:])]
    altura_linea = tam * 1.15
    y_inicial = cy - (len(lineas) - 1) * altura_linea / 2
    tspans = ""
    for i, linea in enumerate(lineas):
        tspans += f'<tspan x="{cx}" y="{y_inicial + i * altura_linea + tam * 0.35}">{linea}</tspan>'
    return (f'<text text-anchor="middle" font-family="{FUENTE_TEXTO}" '
            f'font-size="{tam}" font-weight="{peso}" fill="{color}">{tspans}</text>')


def _flecha(x1, y1, x2, y2, marcador="url(#flecha)"):
    """Línea con flecha al final."""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{COLOR_LINEA}" stroke-width="1.6" marker-end="{marcador}"/>')


def _flecha_acodada(x1, y1, x2, y2):
    """Flecha en L: baja recto, luego horizontal, luego recto al destino.
    Para conectar cajas en distintos carriles sin cruzar otras."""
    if x1 == x2:
        return _flecha(x1, y1, x2, y2)
    y_medio = (y1 + y2) / 2
    return (f'<polyline points="{x1},{y1} {x1},{y_medio} {x2},{y_medio} {x2},{y2}" '
            f'fill="none" stroke="{COLOR_LINEA}" stroke-width="1.6" '
            f'marker-end="url(#flecha)"/>')


def _etiqueta_si_no(x, y, texto):
    """Etiqueta 'SI' o 'NO' que acompaña a las flechas que salen de un rombo."""
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-family="{FUENTE_HEADER}" '
            f'font-size="10" font-weight="700" fill="{COLOR_TEXTO}" '
            f'letter-spacing="0.5">{texto}</text>')


def _encabezado_diagrama(titulo, ancho_total, siglas=None):
    """Barra negra con el título en Anton más la simbología debajo. Si se
    pasan `siglas` (lista de tuplas (sigla, definición)) se imprime una
    línea adicional aclarándolas."""
    bloque_siglas = ""
    if siglas:
        partes = "  ·  ".join(
            f'<tspan font-weight="700">{sig}:</tspan> <tspan>{defi}</tspan>'
            for sig, defi in siglas
        )
        bloque_siglas = (
            f'<text x="{ancho_total - 20}" y="81" text-anchor="end" '
            f'font-family="{FUENTE_TEXTO}" font-size="10.5" '
            f'fill="{COLOR_TEXTO}" font-weight="500">{partes}</text>'
        )
    return f"""
    <rect x="0" y="0" width="{ancho_total}" height="56" fill="{COLOR_FONDO_HEADER}"/>
    <text x="{ancho_total / 2}" y="36" text-anchor="middle"
          font-family="{FUENTE_TITULO}" font-size="22" letter-spacing="1.2"
          fill="{COLOR_CREMA}">{titulo}</text>
    <g transform="translate(20, 70)">
      <rect x="0" y="0" width="14" height="14" fill="#ffffff" stroke="{COLOR_TEXTO}" stroke-width="1.2"/>
      <text x="22" y="11" font-family="{FUENTE_TEXTO}" font-size="10.5" fill="{COLOR_TEXTO}" font-weight="600">Actividad</text>
      <polygon points="120,7 130,0 140,7 130,14" fill="#ffffff" stroke="{COLOR_TEXTO}" stroke-width="1.2"/>
      <text x="150" y="11" font-family="{FUENTE_TEXTO}" font-size="10.5" fill="{COLOR_TEXTO}" font-weight="600">Decisión</text>
      <rect x="240" y="0" width="14" height="14" fill="#2F3E3C" stroke="{COLOR_TEXTO}" stroke-width="1.2"/>
      <text x="262" y="11" font-family="{FUENTE_TEXTO}" font-size="10.5" fill="{COLOR_TEXTO}" font-weight="600">Fin del proceso</text>
    </g>
    {bloque_siglas}"""


def _carriles(nombres, ancho_carril, alto_total, y_inicio, color_servicio,
              ancho_obs=0):
    """Pinta el fondo y los encabezados de los carriles (swimlanes).
    Si `ancho_obs` es mayor a cero, agrega también la cabecera y el fondo
    de la columna lateral de Registro / Observaciones."""
    salida = ""
    n = len(nombres)
    for i, nombre in enumerate(nombres):
        x = i * ancho_carril
        # Alternancia desde el último carril hacia atrás: el último siempre
        # blanco, así nunca queda pegado al gris de la columna lateral de
        # observaciones.
        relleno = "#ffffff" if (n - 1 - i) % 2 == 0 else COLOR_RAIL_BG
        salida += (f'<rect x="{x}" y="{y_inicio}" width="{ancho_carril}" '
                   f'height="{alto_total - y_inicio}" fill="{relleno}"/>')
        # Cabecera del carril con el nombre del equipo responsable.
        salida += (f'<rect x="{x}" y="{y_inicio}" width="{ancho_carril}" '
                   f'height="44" fill="{color_servicio}"/>')
        salida += (f'<text x="{x + ancho_carril / 2}" y="{y_inicio + 28}" '
                   f'text-anchor="middle" font-family="{FUENTE_HEADER}" '
                   f'font-size="11.5" font-weight="700" letter-spacing="0.8" '
                   f'fill="{COLOR_CREMA}">{nombre.upper()}</text>')
        # Línea divisoria entre carriles.
        if i > 0:
            salida += (f'<line x1="{x}" y1="{y_inicio}" x2="{x}" y2="{alto_total}" '
                       f'stroke="{COLOR_RAIL_BORDE}" stroke-width="1"/>')
    if ancho_obs > 0:
        x_obs = len(nombres) * ancho_carril
        salida += (f'<rect x="{x_obs}" y="{y_inicio}" width="{ancho_obs}" '
                   f'height="{alto_total - y_inicio}" fill="{COLOR_RAIL_BG}"/>')
        salida += (f'<line x1="{x_obs}" y1="{y_inicio}" x2="{x_obs}" y2="{alto_total}" '
                   f'stroke="{COLOR_RAIL_BORDE}" stroke-width="1"/>')
        salida += (f'<rect x="{x_obs}" y="{y_inicio}" width="{ancho_obs}" '
                   f'height="44" fill="{COLOR_FONDO_HEADER}"/>')
        salida += (f'<text x="{x_obs + ancho_obs / 2}" y="{y_inicio + 28}" '
                   f'text-anchor="middle" font-family="{FUENTE_HEADER}" '
                   f'font-size="11" font-weight="700" letter-spacing="0.8" '
                   f'fill="{COLOR_CREMA}">REGISTRO / OBSERVACIONES</text>')
    return salida


def _celdas_observaciones(observaciones, x_inicio, ancho_obs, cy_filas):
    """Renderiza las notas explicativas de la columna lateral, alineadas a
    las filas correspondientes. `observaciones` es una lista de tuplas
    (fila, texto)."""
    salida = ""
    for fila, texto in observaciones:
        if fila >= len(cy_filas):
            continue
        salida += _texto_envuelto(x_inicio + 12, cy_filas[fila],
                                  ancho_obs - 24, texto, tam=9.5)
    return salida


def _texto_envuelto(x_izq, cy, ancho_max, texto, tam=10, peso=500,
                    color=None, max_lineas=5):
    """Texto alineado a la izquierda con quiebre por palabra hasta
    `max_lineas`. Útil para notas largas en la columna de observaciones."""
    if color is None:
        color = COLOR_TEXTO
    palabras = texto.split()
    lineas = []
    actual = ""
    chars_max = max(10, int(ancho_max / (tam * 0.5)))
    for palabra in palabras:
        if not actual:
            actual = palabra
        elif len(actual) + 1 + len(palabra) <= chars_max:
            actual += " " + palabra
        else:
            lineas.append(actual)
            actual = palabra
    if actual:
        lineas.append(actual)
    if len(lineas) > max_lineas:
        lineas = lineas[:max_lineas - 1] + [" ".join(lineas[max_lineas - 1:])]
    altura_linea = tam * 1.3
    y_inicial = cy - (len(lineas) - 1) * altura_linea / 2
    tspans = ""
    for i, linea in enumerate(lineas):
        tspans += f'<tspan x="{x_izq}" y="{y_inicial + i * altura_linea + tam * 0.35}">{linea}</tspan>'
    return (f'<text text-anchor="start" font-family="{FUENTE_TEXTO}" '
            f'font-size="{tam}" font-weight="{peso}" fill="{color}">{tspans}</text>')


def _envoltura_svg(ancho, alto, contenido_interno, color_servicio):
    """Genera el <svg> completo con definiciones de marcadores."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {alto}"
     role="img" aria-label="Diagrama de flujo del proceso"
     style="width:100%; height:auto; display:block; background:#ffffff;
            border:1px solid #e0e0e0; border-radius:8px;
            box-shadow:0 2px 8px rgba(0,0,0,0.05);">
  <defs>
    <marker id="flecha" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6"
            markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="{COLOR_LINEA}"/>
    </marker>
  </defs>
  {contenido_interno}
</svg>"""


# ---------------------------------------------------------------------------
# JCO — Jóvenes con Oportunidades
# ---------------------------------------------------------------------------

def svg_diagrama_jco():
    color = "#8e6bbf"
    ancho_carril = 220
    ancho_obs = 240
    carriles = [
        "Equipo de focalización DADE",
        "Equipo de analítica JCO",
        "Equipo SII DADE",
        "Equipo psicosocial JCO",
    ]
    cols_ancho = ancho_carril * len(carriles)  # 880
    ancho = cols_ancho + ancho_obs              # 1120
    y_carril_top = 100  # debajo de header + simbología
    fila_h = 100
    box_w, box_h = 170, 60
    n_filas = 9
    alto = y_carril_top + 44 + fila_h * n_filas + 30

    cx = [i * ancho_carril + ancho_carril / 2 for i in range(len(carriles))]
    y_top_filas = y_carril_top + 44 + 25
    cy = [y_top_filas + i * fila_h + box_h / 2 for i in range(n_filas)]

    pasos = [
        (0, 0, "act", "Caracterización e identificación de participantes"),
        (1, 1, "act", "Identificación y selección de participantes"),
        (1, 2, "act", "Ingreso del joven al servicio"),
        (1, 3, "act", "Organizar base de datos"),
        (2, 4, "act", "Cargue de base de datos"),
        (1, 5, "act", "Revisión de datos cargados"),
        (1, 6, "dec", "¿Cumple las condiciones?"),
        (1, 7, "act", "Solicitar a DADE ajustes"),
        (2, 7, "act", "Ajustar y enviar datos"),
        (3, 6, "act", "Seguimiento y actualización de los estados"),
        (3, 7, "act", "Acceso y permanencia al modelo"),
        (3, 8, "fin", "Mantener actualizado y egresar del servicio"),
    ]

    observaciones = [
        (0, "El proceso de caracterización toma como insumo principal la información del SISBEN VI."),
        (1, "Aplicación del criterio de priorización y del portafolio de servicios. Punto de control."),
        (2, "Confirmación del ingreso del joven al servicio. Punto de control."),
        (3, "Se consolida la base con las variables necesarias para el registro en SIRBE."),
        (4, "Recibir y revisar la base de datos antes del cargue."),
        (7, "Supervisión del cumplimiento, por parte de los y las jóvenes, de los requisitos establecidos en el marco de las actividades condicionadas."),
        (8, "Mantener los registros actualizados y egresar a los jóvenes cuando aplique o finalice el servicio."),
    ]

    contenido = ""
    for col, fila, tipo, texto in pasos:
        if tipo == "act":
            contenido += _caja_actividad(cx[col] - box_w / 2, cy[fila] - box_h / 2,
                                         box_w, box_h, texto, color)
        elif tipo == "dec":
            contenido += _caja_decision(cx[col], cy[fila], box_w + 10, box_h + 20, texto)
        elif tipo == "fin":
            contenido += _caja_fin(cx[col] - box_w / 2, cy[fila] - box_h / 2,
                                   box_w, box_h, texto, color)

    def borde(col, fila, lado):
        x = cx[col]
        if lado == "top":
            return x, cy[fila] - box_h / 2
        if lado == "bottom":
            return x, cy[fila] + box_h / 2
        if lado == "left":
            return x - box_w / 2, cy[fila]
        return x + box_w / 2, cy[fila]

    # Flechas en línea recta (misma columna o misma fila).
    flechas_simples = [
        (0, 0, 1, 1),    # Caracterización -> Selección (misma fila no, acodada)
        (1, 1, 1, 2),    # Selección -> Ingreso
        (1, 2, 1, 3),    # Ingreso -> Organizar
        (1, 3, 2, 4),    # Organizar -> Cargue (acodada)
        (2, 4, 1, 5),    # Cargue -> Revisión (acodada, cruza a col 1)
        (1, 5, 1, 6),    # Revisión -> Decisión (misma col, recto)
        (3, 6, 3, 7),    # Seguimiento -> Acceso
        (3, 7, 3, 8),    # Acceso -> Mantener
    ]
    for ori_c, ori_f, dst_c, dst_f in flechas_simples:
        if ori_c == dst_c:
            x1, y1 = borde(ori_c, ori_f, "bottom")
            x2, y2 = borde(dst_c, dst_f, "top")
            contenido += _flecha(x1, y1, x2, y2)
        elif ori_f == dst_f:
            lado_o, lado_d = ("right", "left") if dst_c > ori_c else ("left", "right")
            x1, y1 = borde(ori_c, ori_f, lado_o)
            x2, y2 = borde(dst_c, dst_f, lado_d)
            contenido += _flecha(x1, y1, x2, y2)
        else:
            x1, y1 = borde(ori_c, ori_f, "bottom")
            x2, y2 = borde(dst_c, dst_f, "top")
            contenido += _flecha_acodada(x1, y1, x2, y2)

    # Rombo de decisión (col 1, fila 6): SÍ cruza a psicosocial (col 3, fila 6)
    # pasando por encima del carril SII; NO baja recto a "Solicitar a DADE
    # ajustes" (col 1, fila 7).
    dec_w, dec_h = box_w + 10, box_h + 20
    # SÍ: salida por la derecha del rombo hacia caja a la derecha (col 3).
    x_si, y_si = cx[1] + dec_w / 2, cy[6]
    x_dst_si, y_dst_si = borde(3, 6, "left")
    contenido += _flecha(x_si, y_si, x_dst_si, y_dst_si)
    contenido += _etiqueta_si_no((x_si + x_dst_si) / 2, y_si - 8, "SÍ")
    # NO: salida por debajo del rombo, recto a "Solicitar a DADE ajustes".
    x_no, y_no = cx[1], cy[6] + dec_h / 2
    x_dst_no, y_dst_no = borde(1, 7, "top")
    contenido += _flecha(x_no, y_no, x_dst_no, y_dst_no)
    contenido += _etiqueta_si_no(x_no + 14, (y_no + y_dst_no) / 2, "NO")

    # Solicitar a DADE ajustes (col 1 fila 7) -> Ajustar y enviar (col 2 fila 7)
    x1, y1 = borde(1, 7, "right")
    x2, y2 = borde(2, 7, "left")
    contenido += _flecha(x1, y1, x2, y2)

    # Loop: Ajustar y enviar (col 2 fila 7) vuelve a Revisión (col 1 fila 5).
    # Ruta abajo → izquierda → arriba → llega: sale por debajo de Ajustar,
    # desciende un poco, va horizontal hacia la izquierda por debajo de toda
    # la fila 7, sube por el margen izquierdo del carril 1 (sin tocar las
    # cajas que están centradas) y entra a Revisión por la izquierda.
    x_aj_bottom = cx[2]
    y_aj_bottom = cy[7] + box_h / 2
    y_descenso = y_aj_bottom + 30
    x_pivote = cx[1] - box_w / 2 - 22  # interior del carril 1, a la izquierda
    x_rev_left = cx[1] - box_w / 2
    y_rev = cy[5]
    contenido += (f'<polyline points="{x_aj_bottom},{y_aj_bottom} '
                  f'{x_aj_bottom},{y_descenso} '
                  f'{x_pivote},{y_descenso} '
                  f'{x_pivote},{y_rev} '
                  f'{x_rev_left},{y_rev}" '
                  f'fill="none" stroke="{COLOR_LINEA}" stroke-width="1.6" '
                  f'marker-end="url(#flecha)" stroke-dasharray="4 3"/>')

    siglas = [
        ("DADE", "Dirección de Análisis y Diseño Estratégico"),
        ("SII", "Subdirección de Investigación e Información"),
    ]
    encabezado = _encabezado_diagrama("Diagrama de flujo del proceso", ancho,
                                      siglas=siglas)
    carriles_svg = _carriles(carriles, ancho_carril, alto, y_carril_top, color,
                             ancho_obs=ancho_obs)
    obs_svg = _celdas_observaciones(observaciones, cols_ancho, ancho_obs, cy)

    return _envoltura_svg(ancho, alto,
                          encabezado + carriles_svg + contenido + obs_svg, color)


# ---------------------------------------------------------------------------
# Casas de Juventud
# ---------------------------------------------------------------------------

def svg_diagrama_casas():
    color = "#253C5C"
    ancho_carril = 250
    ancho_obs = 240
    carriles = [
        "Equipo territorial",
        "Equipo administrativo",
        "Equipo SII",
    ]
    cols_ancho = ancho_carril * len(carriles)  # 750
    ancho = cols_ancho + ancho_obs              # 990
    y_carril_top = 100
    fila_h = 100
    box_w, box_h = 180, 60
    dec_w, dec_h = box_w + 20, box_h + 24
    n_filas = 12
    alto = y_carril_top + 44 + fila_h * n_filas + 30

    cx = [i * ancho_carril + ancho_carril / 2 for i in range(len(carriles))]
    y_top_filas = y_carril_top + 44 + 25
    cy = [y_top_filas + i * fila_h + box_h / 2 for i in range(n_filas)]

    pasos = [
        (0, 0, "act", "Registro de participantes en la ficha SIRBE"),
        (0, 1, "act", "Diligenciar base de control"),
        (1, 2, "act", "Revisión de la ficha"),
        (1, 3, "dec", "¿Está bien diligenciada?"),
        (1, 4, "act", "Cargue en SIRBE"),
        (1, 5, "dec", "¿Hay novedades?"),
        (1, 6, "act", "Creación de caso y envío de solicitud"),
        (2, 7, "act", "Ajustar según solicitud condicionada"),
        (2, 8, "dec", "¿Se ajustó el registro?"),
        (2, 9, "act", "Notificar al servicio"),
        (1, 10, "act", "Cargue de los ajustes realizados"),
        (1, 11, "fin", "Fin del servicio"),
    ]

    observaciones = [
        (0, "La ficha se registra en el desarrollo de la actividad."),
        (1, "Se diligencia el drive de control con la información recolectada en territorio."),
        (2, "Se revisa que las fichas estén bien diligenciadas antes del cargue en SIRBE."),
        (6, "Se diligencia el formato que corresponde y se envía la solicitud por Aranda."),
        (10, "Una vez confirmado el ajuste, el equipo administrativo carga los cambios en SIRBE."),
        (11, "Cierre del registro tras confirmar el ajuste o tras descartar novedades."),
    ]

    contenido = ""
    for col, fila, tipo, texto in pasos:
        if tipo == "act":
            contenido += _caja_actividad(cx[col] - box_w / 2, cy[fila] - box_h / 2,
                                         box_w, box_h, texto, color)
        elif tipo == "dec":
            contenido += _caja_decision(cx[col], cy[fila], dec_w, dec_h, texto)
        elif tipo == "fin":
            contenido += _caja_fin(cx[col] - box_w / 2, cy[fila] - box_h / 2,
                                   box_w, box_h, texto, color)

    def borde(col, fila, lado):
        x = cx[col]
        if lado == "top":
            return x, cy[fila] - box_h / 2
        if lado == "bottom":
            return x, cy[fila] + box_h / 2
        if lado == "left":
            return x - box_w / 2, cy[fila]
        return x + box_w / 2, cy[fila]

    # Flechas rectas o acodadas (camino principal SÍ).
    flechas = [
        (0, 0, 0, 1),    # Registro -> Diligenciar
        (0, 1, 1, 2),    # Diligenciar -> Revisión
        (1, 2, 1, 3),    # Revisión -> ¿bien diligenciada?
        (1, 4, 1, 5),    # Cargue -> ¿novedades?
        (1, 6, 2, 7),    # Creación -> Ajustar (SII)
        (2, 7, 2, 8),    # Ajustar -> ¿Se ajustó?
        (1, 10, 1, 11),  # Cargue de ajustes -> Fin
    ]
    for ori_c, ori_f, dst_c, dst_f in flechas:
        if ori_c == dst_c:
            x1, y1 = borde(ori_c, ori_f, "bottom")
            x2, y2 = borde(dst_c, dst_f, "top")
            contenido += _flecha(x1, y1, x2, y2)
        elif ori_f == dst_f:
            lado_o, lado_d = ("right", "left") if dst_c > ori_c else ("left", "right")
            x1, y1 = borde(ori_c, ori_f, lado_o)
            x2, y2 = borde(dst_c, dst_f, lado_d)
            contenido += _flecha(x1, y1, x2, y2)
        else:
            x1, y1 = borde(ori_c, ori_f, "bottom")
            x2, y2 = borde(dst_c, dst_f, "top")
            contenido += _flecha_acodada(x1, y1, x2, y2)

    # === Decisión "¿Está bien diligenciada?" (col 1, fila 3) ===
    # SÍ baja a Cargue (col 1 fila 4).
    x_si, y_si = cx[1], cy[3] + dec_h / 2
    x_dst, y_dst = borde(1, 4, "top")
    contenido += _flecha(x_si, y_si, x_dst, y_dst)
    contenido += _etiqueta_si_no(x_si + 14, (y_si + y_dst) / 2, "SÍ")
    # NO vuelve hasta el primer paso "Registro de participantes" (col 0, fila 0),
    # por el costado izquierdo del diagrama para no cruzar el flujo principal.
    x_no, y_no = cx[1] - dec_w / 2, cy[3]
    x_pivote = 18
    x_reg_left = cx[0] - box_w / 2
    contenido += (f'<polyline points="{x_no},{y_no} {x_pivote},{y_no} '
                  f'{x_pivote},{cy[0]} {x_reg_left},{cy[0]}" fill="none" '
                  f'stroke="{COLOR_LINEA}" stroke-width="1.6" '
                  f'marker-end="url(#flecha)" stroke-dasharray="4 3"/>')
    contenido += _etiqueta_si_no(x_no - 18, y_no - 8, "NO")

    # === Decisión "¿Hay novedades?" (col 1, fila 5) ===
    # SÍ baja a Creación de caso (col 1 fila 6).
    x_si, y_si = cx[1], cy[5] + dec_h / 2
    x_dst, y_dst = borde(1, 6, "top")
    contenido += _flecha(x_si, y_si, x_dst, y_dst)
    contenido += _etiqueta_si_no(x_si + 14, (y_si + y_dst) / 2, "SÍ")
    # NO salta directo al Fin del servicio por la izquierda del carril.
    x_no, y_no = cx[1] - dec_w / 2, cy[5]
    x_pivote = cx[1] - box_w / 2 - 38
    x_fin_left = cx[1] - box_w / 2
    contenido += (f'<polyline points="{x_no},{y_no} {x_pivote},{y_no} '
                  f'{x_pivote},{cy[11]} {x_fin_left},{cy[11]}" fill="none" '
                  f'stroke="{COLOR_LINEA}" stroke-width="1.6" '
                  f'marker-end="url(#flecha)"/>')
    contenido += _etiqueta_si_no(x_pivote - 14, y_no - 8, "NO")

    # === Decisión "¿Se ajustó el registro?" (col 2, fila 8) ===
    # SÍ sale por la IZQUIERDA del rombo y cruza al "Cargue de los ajustes
    # realizados" (col 1, fila 10). Va horizontal hasta el pivote entre
    # col 1 y col 2, baja, y entra por arriba de la caja Cargue.
    x_si, y_si = cx[2] - dec_w / 2, cy[8]
    x_dst_si, y_dst_si = borde(1, 10, "top")
    x_pivote_si = cx[1] + box_w / 2 + (ancho_carril - box_w) / 2  # entre col 1 y col 2
    contenido += (f'<polyline points="{x_si},{y_si} {x_pivote_si},{y_si} '
                  f'{x_pivote_si},{y_dst_si - 18} {x_dst_si},{y_dst_si - 18} '
                  f'{x_dst_si},{y_dst_si}" fill="none" stroke="{COLOR_LINEA}" '
                  f'stroke-width="1.6" marker-end="url(#flecha)"/>')
    contenido += _etiqueta_si_no((x_si + x_pivote_si) / 2, y_si - 8, "SÍ")
    # NO baja recto a "Notificar al servicio" (col 2, fila 9).
    x_no, y_no = cx[2], cy[8] + dec_h / 2
    x_dst_no, y_dst_no = borde(2, 9, "top")
    contenido += _flecha(x_no, y_no, x_dst_no, y_dst_no)
    contenido += _etiqueta_si_no(x_no + 14, (y_no + y_dst_no) / 2, "NO")
    # Notificar vuelve al rombo "¿Se ajustó el registro?" (loop) por la
    # derecha — línea punteada. Entra al rombo por su vértice derecho.
    x_not_r, y_not_r = borde(2, 9, "right")
    x_dec_r, y_dec_r = cx[2] + dec_w / 2, cy[8]
    x_pivote_loop = cx[2] + box_w / 2 + 28
    contenido += (f'<polyline points="{x_not_r},{y_not_r} {x_pivote_loop},{y_not_r} '
                  f'{x_pivote_loop},{y_dec_r} {x_dec_r},{y_dec_r}" fill="none" '
                  f'stroke="{COLOR_LINEA}" stroke-width="1.6" '
                  f'marker-end="url(#flecha)" stroke-dasharray="4 3"/>')

    siglas = [
        ("SII", "Subdirección de Investigación e Información"),
    ]
    encabezado = _encabezado_diagrama("Diagrama de flujo del proceso", ancho,
                                      siglas=siglas)
    carriles_svg = _carriles(carriles, ancho_carril, alto, y_carril_top, color,
                             ancho_obs=ancho_obs)
    obs_svg = _celdas_observaciones(observaciones, cols_ancho, ancho_obs, cy)

    return _envoltura_svg(ancho, alto,
                          encabezado + carriles_svg + contenido + obs_svg, color)


# ---------------------------------------------------------------------------
# Forjar Restaurativo
# ---------------------------------------------------------------------------

def svg_diagrama_forjar():
    color = "#1e7895"  # azul Forjar (el mismo de los títulos del bloque "A tener en cuenta")
    ancho_carril = 300
    ancho_obs = 260
    carriles = [
        "Equipo administrativo",
        "Equipo SII",
    ]
    cols_ancho = ancho_carril * len(carriles)  # 600
    ancho = cols_ancho + ancho_obs              # 860
    y_carril_top = 100
    fila_h = 100
    box_w, box_h = 200, 60
    dec_w, dec_h = box_w + 20, box_h + 24
    n_filas = 10
    alto = y_carril_top + 44 + fila_h * n_filas + 30

    cx = [i * ancho_carril + ancho_carril / 2 for i in range(len(carriles))]
    y_top_filas = y_carril_top + 44 + 25
    cy = [y_top_filas + i * fila_h + box_h / 2 for i in range(n_filas)]

    pasos = [
        (0, 0, "act", "Diligenciar ficha SIRBE"),
        (0, 1, "act", "Cargue en SIRBE"),
        (0, 2, "dec", "¿Hay novedades?"),
        (0, 3, "act", "Creación de caso y envío de solicitud"),
        (1, 4, "act", "Ajustar según solicitud condicionada"),
        (1, 5, "dec", "¿Se ajustó el registro?"),
        (1, 6, "act", "Notificar al servicio"),
        (0, 7, "act", "Cargue de ajustes realizados"),
        (0, 8, "act", "Seguimiento y actualización de los estados"),
        (0, 9, "fin", "Fin del servicio — Mantener actualizado y egresar"),
    ]

    observaciones = [
        (0, "La ficha se diligencia con la información del joven al ingreso del servicio."),
        (1, "Recibir y revisar la base antes de subirla a SIRBE."),
        (3, "Se diligencia el formato que corresponde y se envía por Aranda."),
        (7, "Cargar en SIRBE los ajustes confirmados por el equipo SII."),
        (8, "Supervisión del cumplimiento de los requisitos por parte de los y las jóvenes."),
        (9, "Mantener los registros actualizados y egresar cuando aplique o finalice el servicio."),
    ]

    contenido = ""
    for col, fila, tipo, texto in pasos:
        if tipo == "act":
            contenido += _caja_actividad(cx[col] - box_w / 2, cy[fila] - box_h / 2,
                                         box_w, box_h, texto, color)
        elif tipo == "dec":
            contenido += _caja_decision(cx[col], cy[fila], dec_w, dec_h, texto)
        elif tipo == "fin":
            contenido += _caja_fin(cx[col] - box_w / 2, cy[fila] - box_h / 2,
                                   box_w, box_h, texto, color)

    def borde(col, fila, lado):
        x = cx[col]
        if lado == "top":
            return x, cy[fila] - box_h / 2
        if lado == "bottom":
            return x, cy[fila] + box_h / 2
        if lado == "left":
            return x - box_w / 2, cy[fila]
        return x + box_w / 2, cy[fila]

    # Flechas rectas o acodadas que no involucran decisiones.
    flechas = [
        (0, 0, 0, 1),
        (0, 1, 0, 2),
        (0, 3, 1, 4),   # Creación (admin) -> Ajustar (SII), acodada
        (1, 4, 1, 5),   # Ajustar -> ¿Se ajustó el registro?
        (0, 7, 0, 8),
        (0, 8, 0, 9),
    ]
    for ori_c, ori_f, dst_c, dst_f in flechas:
        if ori_c == dst_c:
            x1, y1 = borde(ori_c, ori_f, "bottom")
            x2, y2 = borde(dst_c, dst_f, "top")
            contenido += _flecha(x1, y1, x2, y2)
        elif ori_f == dst_f:
            lado_o, lado_d = ("right", "left") if dst_c > ori_c else ("left", "right")
            x1, y1 = borde(ori_c, ori_f, lado_o)
            x2, y2 = borde(dst_c, dst_f, lado_d)
            contenido += _flecha(x1, y1, x2, y2)
        else:
            x1, y1 = borde(ori_c, ori_f, "bottom")
            x2, y2 = borde(dst_c, dst_f, "top")
            contenido += _flecha_acodada(x1, y1, x2, y2)

    # === Decisión "¿Hay novedades?" (col 0, fila 2) ===
    # SÍ baja recto a "Creación de caso y envío de solicitud" (col 0, fila 3).
    x_si, y_si = cx[0], cy[2] + dec_h / 2
    x_dst, y_dst = borde(0, 3, "top")
    contenido += _flecha(x_si, y_si, x_dst, y_dst)
    contenido += _etiqueta_si_no(x_si + 14, (y_si + y_dst) / 2, "SÍ")
    # NO sale por la izquierda y salta directo a "Seguimiento y actualización
    # de los estados" (col 0, fila 8). Razón: si no hay novedades, no hay
    # ajustes que cargar, así que se omite ese paso intermedio.
    x_no, y_no = cx[0] - dec_w / 2, cy[2]
    x_pivote = cx[0] - box_w / 2 - 32
    x_dst_no = cx[0] - box_w / 2
    contenido += (f'<polyline points="{x_no},{y_no} {x_pivote},{y_no} '
                  f'{x_pivote},{cy[8]} {x_dst_no},{cy[8]}" fill="none" '
                  f'stroke="{COLOR_LINEA}" stroke-width="1.6" '
                  f'marker-end="url(#flecha)"/>')
    contenido += _etiqueta_si_no(x_pivote - 14, y_no - 8, "NO")

    # === Decisión "¿Se ajustó el registro?" (col 1, fila 5) ===
    # SÍ sale por la IZQUIERDA del rombo y cruza al "Cargue de ajustes
    # realizados" (col 0, fila 7). Va horizontal hasta el pivote entre col 0
    # y col 1, baja, y entra por arriba de la caja Cargue.
    x_si, y_si = cx[1] - dec_w / 2, cy[5]
    x_dst_si, y_dst_si = borde(0, 7, "top")
    x_pivote_si = cx[0] + box_w / 2 + (ancho_carril - box_w) / 2  # entre col 0 y col 1
    contenido += (f'<polyline points="{x_si},{y_si} {x_pivote_si},{y_si} '
                  f'{x_pivote_si},{y_dst_si - 18} {x_dst_si},{y_dst_si - 18} '
                  f'{x_dst_si},{y_dst_si}" fill="none" stroke="{COLOR_LINEA}" '
                  f'stroke-width="1.6" marker-end="url(#flecha)"/>')
    contenido += _etiqueta_si_no((x_si + x_pivote_si) / 2, y_si - 8, "SÍ")
    # NO baja recto a "Notificar al servicio" (col 1, fila 6).
    x_no, y_no = cx[1], cy[5] + dec_h / 2
    x_dst_no, y_dst_no = borde(1, 6, "top")
    contenido += _flecha(x_no, y_no, x_dst_no, y_dst_no)
    contenido += _etiqueta_si_no(x_no + 14, (y_no + y_dst_no) / 2, "NO")
    # Notificar vuelve al rombo "¿Se ajustó el registro?" (loop) por la
    # derecha — línea punteada. Entra al rombo por su vértice derecho.
    x_not_r, y_not_r = borde(1, 6, "right")
    x_dec_r, y_dec_r = cx[1] + dec_w / 2, cy[5]
    x_pivote_loop = cx[1] + box_w / 2 + 50
    contenido += (f'<polyline points="{x_not_r},{y_not_r} {x_pivote_loop},{y_not_r} '
                  f'{x_pivote_loop},{y_dec_r} {x_dec_r},{y_dec_r}" fill="none" '
                  f'stroke="{COLOR_LINEA}" stroke-width="1.6" '
                  f'marker-end="url(#flecha)" stroke-dasharray="4 3"/>')

    siglas = [
        ("SII", "Subdirección de Investigación e Información"),
    ]
    encabezado = _encabezado_diagrama("Diagrama de flujo del proceso", ancho,
                                      siglas=siglas)
    carriles_svg = _carriles(carriles, ancho_carril, alto, y_carril_top, color,
                             ancho_obs=ancho_obs)
    obs_svg = _celdas_observaciones(observaciones, cols_ancho, ancho_obs, cy)

    return _envoltura_svg(ancho, alto,
                          encabezado + carriles_svg + contenido + obs_svg, color)
