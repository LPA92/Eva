# Importamos reflex
import reflex as rx

# Importamos la plantilla de información profesional
from Eva_Navarro.componentes.titulo import titulo as titulo
# Importamos los colores de texto
from Eva_Navarro.estilos.colores import TextoColor as TextoColor
# Importamos los tamaños
from Eva_Navarro.estilos.generico import Tamanyo as Tamanyo
# Importamos las plantillas de imagenes para la vista
from Eva_Navarro.componentes.imagenes import img_vista as imagen

# Añadimos los componentes que se van a ver en la página principal
def vistapartido() -> rx.Component:
    
        # vstack = Posiciona los componentes de forma vertical
    return rx.vstack(
        # hstack = Posiciona los componentes de forma horizontal
        rx.hstack(
            rx.box(
                # Pone la imagen Justicia.svg
                rx.image(
                    src = '/svg/Partidos.svg',
                    # Si no carga la imagen nos sale el texto definido en alt
                    alt = 'Imagen de Partidos Judiciales',
                    width ='150%',
                    height = 'auto',
                ),
                # Relleno de 1 rem alrededor del box.
                padding = Tamanyo.DF.value,
            ),            
            rx.box(  
                rx.flex(
                    rx.vstack(
                        rx.box(
                            titulo(
                                'Partidos Judiciales de la isla de Gran Canaria'
                            ),
                            margin_left=Tamanyo.XXL.value,
                        ),
                        rx.spacer(),
                        rx.spacer(),
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
                                # Para centrar el encabezado de la tabla
                                align='center',
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
                                    rx.table.row_header_cell("Arucas"),
                                    rx.table.row_header_cell("San Nicolas Tolentino"),
                                    rx.table.row_header_cell("Ingenio"),
                                    rx.table.row_header_cell("Sta Brigida"),
                                    rx.table.row_header_cell("San Bartolome de Tirajana"),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell("Firgas"),
                                    rx.table.row_header_cell("Galdar"),
                                    rx.table.row_header_cell("Telde"),
                                    rx.table.row_header_cell("Vega de San Mateo"),
                                    rx.table.row_header_cell("Sta Lucia de Tirajana"),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell("Tejeda"),
                                    rx.table.row_header_cell("Moya"),
                                    rx.table.row_header_cell("Valsequillo de G.C."),
                                    rx.table.row_header_cell(""),
                                    rx.table.row_header_cell(""),
                                ),                       
                                rx.table.row(
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
                                width="100%",
                            ),
                        ),
                    ),
                ),
                # Para separar la imagen del texto
                margin_left = Tamanyo.XL.value,
                # Especifica que los elementos flexibles se ajustaran si es necesario
                Flex_wrap = 'wrap',
            ),
        ),
        margin_top = Tamanyo.XXL.value,
        margin_bottom = Tamanyo.XL.value,
        margin_left = Tamanyo.XL.value,        
    )