# Importamos reflex
import reflex as rx
# Importamos los estilos
import Eva_Navarro.estilos.generico as comun

# Importamos la plantilla de información profesional
from Eva_Navarro.componentes.titulo import titulo as titulo
# Importamos los tamaños
from Eva_Navarro.estilos.texto import Texto as Tamanyo
# Importamos las escalas
import Eva_Navarro.estilos.escalas as escala
# Importamos los espacios
from Eva_Navarro.estilos.generico import Espacio as Espacio


# Añadimos los componentes que se van a ver en la página principal
def vistapartido() -> rx.Component:
    
        # vstack = Posiciona los componentes de forma vertical
    return rx.hstack(
        # hstack = Posiciona los componentes de forma horizontal
        rx.flex(
            # Pone la imagen Justicia.svg
            rx.image(
                src = '/svg/Partidos.svg',
                # Si no carga la imagen nos sale el texto definido en alt
                alt = 'Imagen de Partidos Judiciales',
                style = escala.escala_partido,
            ),            
            rx.vstack(
                rx.flex(
                    rx.box(
                        titulo(
                            'Partidos Judiciales de la isla de Gran Canaria',
                        ),
                    ),
                ),
                rx.table.root(
                    # Encabezamiento de la tabla ( parte superior )
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("Arucas"),
                            rx.table.column_header_cell("Sta Mª de Guia G.C."),
                            rx.table.column_header_cell("Telde"),
                            rx.table.column_header_cell("Las Palmas G.C."),
                            rx.table.column_header_cell("San Bartolome de Tirajana"),
                        ),
                    ),
                    # Datos de la tabla que vienen debajo del encabezamiento
                    # table.row_header_cell = texto en negrita
                    # table.cell = texto normal
                        
                    rx.table.body(
                            rx.table.row(
                            rx.table.row_header_cell("Artenara"),
                            rx.table.row_header_cell("Agaete"),
                            rx.table.row_header_cell("Agüimes"),
                            rx.table.row_header_cell("Las Palmas de G.C."),
                            rx.table.row_header_cell("Mogan"),
                        ),
                        rx.table.row(
                            rx.table.row_header_cell("Arucas"),                           rx.table.row_header_cell("San Nicolas Tolentino"),
                            rx.table.row_header_cell("Ingenio"),
                            rx.table.row_header_cell("Sta Brigida"),
                            rx.table.row_header_cell("San Bartolome de Tirajana"),
                        ),
                        rx.table.row(
                            rx.table.row_header_cell("Firgas"),
                            rx.table.row_header_cell("Galdar"),
                            rx.table.row_header_cell("Telde"),
                            rx.table.row_header_cell("Vega San Mateo"),
                            rx.table.row_header_cell("Sta Lucia de Tirajana"),
                        ),
                        rx.table.row(
                            rx.table.row_header_cell("Tejeda"),
                            rx.table.row_header_cell("Moya"),
                            rx.table.row_header_cell("Valsequillo GC"),
                            rx.table.row_header_cell(""),
                            rx.table.row_header_cell(""),
                        ),                                        rx.table.row(
                            rx.table.row_header_cell("Teror"),
                            rx.table.row_header_cell("Sta Mª de Guia G.C."),
                            rx.table.cell(""),
                            rx.table.cell(""),
                            rx.table.cell(""),
                        ),
                        rx.table.row(
                            rx.table.row_header_cell("Teror"),
                            rx.table.cell("Valleso"),
                            rx.table.cell(""),
                            rx.table.cell(""),
                            rx.table.cell(""),
                        ),
                    ),
                ),
                # Alineación vertical dentro del vstack
                align = 'center',
                # Alineación horizontal dentro del vstack
                justify = 'center',
            ),
            # Separación entre la imagen y la tabla
            spacing = '8',
            # Centra verticalmente la imagen
            vertical_items = 'center',
        ),
        style = comun.Flexible,                
        margin_top = Tamanyo.T07.value,
        margin_bottom = Tamanyo.T08.value,
    )