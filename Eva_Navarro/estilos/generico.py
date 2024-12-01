# enum = define un conjunto de nombres descriptivos vinculados a valores constantes
# 1rem = Tamaño de la fuente raíz, por defecto 16px
# 1em = Tamaño de la fuente del padre,si no se define el tamaño 16px.
# gap = Espacio entre dos componentes

# Tamaños de pantallas
# SD  =   640 x   480  ->  40em
# QHD =   960 x   540  ->  60em
# HD  = 1.280 x   720  ->  80em , 45.0em
# FHD = 1.920 x 1.080  -> 120em , 67.5em
# QHD = 2.560 x 1.440  -> 160em
# UHD = 3.840 x 2.160  -> 240em
# 8K  = 7.680 x 4.320  -> 480em

# Tamaños flexibles por defecto de reflex
# initial = 0px,
# xs = 30em, ->   480 px
# sm = 48em, ->   768 px
# md = 62em, ->   992 px
# lg = 80em, -> 1.280 px
# xl = 96em, -> 1.536 px

# Tamaños a diseñar para el diseño flexible en reflex
# xs    [ 960 x 540 ]
#    -> Ancho =  60.00em
#    -> Alto  =  33.75em

# sm   [ 1.024 x 576 ]
#    -> Ancho =  64em
#    -> Alto  =  36em 

# md   [ 1.280 *  720 ]
#    -> Ancho =  80em
#    -> Alto  =  45em

# lg   [ 1.328 * 736 ]
#    -> Ancho =  83em
#    -> Alto  =  46em

# xl  [ 1.920 * 1.072 ]
#    -> Ancho = 120em
#    -> Alto  =  67em




# Importamos reflex
import reflex as rx 

# Importamos los colores
from .colores import Color as Color
# Importamos los colores de los textos
from .colores import TextoColor as TextoColor
# Importamos las fuentes
from .fuentes import Fuente as Fuente
# Importamos el peso de las fuentes
from .fuentes import Trazo as Trazo
# Importamos los tamaños para el texto
from .valores import Texto as Tamanyo
# Importamos los valores para las separaciones
from .valores import Separacion as Espacio
# Importamos las diferentes pantallas
# from .valores import Monitor as Monitor
# Importamos los tamaños
from Eva_Navarro.estilos.valores import Anchos as Ancho

    # Para establecer los puntos de interrupción para las diferentes pantallas (responsive)
    # xs =  60em, 33.75em ->   960 px ,   540 px
    # sm =  64em, 36.00em -> 1.024 px ,   576 px
    # md =  80em, 45.00em -> 1.280 px ,   720 px
    # lg =  83em, 46.00em -> 1.328 px ,   736 px
    # xl = 120em, 67.50em -> 1.920 px , 1.080 px

# En mayúsculas para definir que es una constante
MAX_ANCHO = '90em', # 1em=16px → 1.440 de ancho
MAX_ALTO = '46em',  # 1em=16px →   736 de alto

FLEX_DIRECCION = ["column", "column", "row", "row", "row"]

# Hoja de estilos ( cargamos las fuentes )
HOJA_ESTILOS = [

    # fuente poppins
    "https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"

    # fuente roboto
    "https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap"


    # fuente conforta
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@300..700&display=swap"
    
    # Animaciones de css
    "/css/animacion.css"
    
    ]

# Estilos Genéricos a aplicar en toda la página web
ESTILO_GENERICO = {

    # Para establecer los puntos de interrupción para las diferentes pantallas (responsive)
    # xs =  60em, ->   960 px ,   540 px  [ 33.75em ]
    # sm =  64em, -> 1.024 px ,   576 px  [ 36.00em ]
    # md =  80em, -> 1.280 px ,   720 px  [ 45.00em ]
    # lg =  83em, -> 1.328 px ,   736 px  [ 46.00em ]
    # xl = 120em, -> 1.920 px , 1.080 px  [ 67.50em ]

    # Establecemos los puntos de ruptura para las diferentes pantallas.    
    "breakpoints": [
        '960px',
        '1024px',
        '1280px',
        '1328px',
        '1920px',
    ],

    # Establecemos la fuente por defecto
    'font_family': Fuente.DEFECTO.value,
    # Definimos el peso de la fuente por defecto
    'font_weight': Trazo.NORMAL.value,
    'background_color': Color.FONDO.value,

    # Todos los botones van a tener el mismo estilo
    rx.button: {
        # Definimos el color del texto en los botones
        'color': TextoColor.NAV.value,
        # Definimos el color de fondo de todos los botones
        'background_color': Color.FONDO.value,
        # Definimos el color de fondo del botón al pasar el ratón
        '_hover': {
        'background_color': Color.SECUNDARIO.value,
        }
    },

    # Todos los enlaces van a tener el mismo estilo
    rx.link: {
        # Para quitar el subrayado del enlace
        'text_decoration': 'none',
        # Para que se quede igual al pasar el ratón encima de él
        '_hover': {},
    },
    
    # border-width: thick;
    
    rx.table.column_header_cell: {
        # Definimos el color del texto 
        'color': TextoColor.CABEZA.value,
        # Definimos el color de fondo de todos los encabezados de tablas
        'background_color': Color.TABLA.value,
        # Establecemos el tipo del borde de la tabla
        'border': 'solid',
        # Establecemos el grosor del borde de la tabla
        'border_width': Tamanyo.T02.value,
        # Establecemos el color del borde rojo
        'border_color': Color.BORDE.value,
        # Para que todos los elementos ocupen lo mismo
        'flex_grow': '1',
        # Centramos el texto en el eje horizontal
        'text_align': 'center',
        # Centramos el texto en el eje vertical
        'vertical_align' : 'center',          
        # Definimos el tamaño de la letra        
        'font_size': Tamanyo.T05.value,
    },
    rx.table.row_header_cell: {
        # Definimos el color del texto 
        'color': TextoColor.CELDA.value,
        # Definimos el color de fondo de todos las celdas de tablas
        'background_color': TextoColor.CABEZA.value,
        # Establecemos el tipo del borde de la tabla
        'border': 'solid',        
        # Establecemos el grosor del borde de la tabla
        'border_width': Tamanyo.T02.value,
        # Establecemos el color del borde rojo
        'border_color': Color.BORDE.value,
        # Para que todos los elementos ocupen lo mismo
        'flex_grow': '1',
        # Centramos el texto en el eje horizontal
        'text_align': 'center',
        # Centramos el texto en el eje vertical
        'vertical_align' : 'center',          
        # Definimos el tamaño de la letra
        'font_size': Tamanyo.T05.value,         
    },
    rx.table.cell: {
        # Definimos el color del texto 
        'color': TextoColor.CELDA.value,
        # Definimos el color de fondo de todos las celdas de tablas
        'background_color': TextoColor.CABEZA.value,
        # Establecemos el tipo del borde de la tabla
        'border': 'solid',        
        # Establecemos el grosor del borde de la tabla
        'border_width': Tamanyo.T02.value,
        # Establecemos el color del borde rojo
        'border_color': Color.BORDE.value,
        # Para que todos los elementos ocupen lo mismo
        'flex_grow': '1',
        # Centramos el texto en el eje horizontal
        'text_align': 'center',
        # Centramos el texto en el eje vertical
        'vertical_align' : 'center',          
        # Definimos el tamaño de la letra
        'font_size': Tamanyo.T05.value,
    },

}

Flexible = dict(
    
    # Flex_grow = Cantidad de espacio que ocupa horizontalmente el elemento especificado en comparación con el resto de elementos.
    
    # flex_shrink = el elemento especificado se reduce tantas veces como le indiquemos con respecto a los demás elementos 
    
    # Estable la forma de alineación en el eje x
    # space_between = Excepto los extremos dejan el mismo espacio entre sí lo diferentes elemetos
    #space_around = Dejan el mismo espacio horizontal entre todos los elementos
    justify_content = 'space_around',
    # Alienación vertical en elementos flexibles ( FLEX )
    align_items = 'center',
    # Para ajustar la distancia en el eje vertical cuando hay multilineas
    # align_content = 'start'
    flex_direction = FLEX_DIRECCION,
    # Permite que se desborde o no los elementos, si lo permite pasan a la siguiente línea.
    flex_wrap = 'wrap',
)

Fijo_Nav = dict(
    
    ### PARA FIJAR BARRA DE NAVEGACIÓN AL INICIO DE LA PÁGINA ###
    #  Para fijar la posición position='sticky', top='0' y z_index = '999' 
    position = 'sticky',
    # Se queda fija arriba del todo de la página web
    top='0',
    # Para asegurarnos de que permanece en la parte superior
    z_index = '999',

    # CARACTERISTICAS DEL rx.flex()
    # direction=row Alinea verticalmete,direction=column Alinea horizontalmente,
    justify_content = 'space_around',
    # Alienación vertical en elementos flexibles ( FLEX )
    align_items = 'Center',
    # Para ajustar la distancia en el eje vertical cuando hay multilineas
    # align_content = 'start'
    flex_direction = FLEX_DIRECCION,
    # Permite que se desborde o no los elementos, si lo permite pasan a la siguiente línea.
    flex_wrap = 'wrap',  

    
    # COLOR, PADDING, MARGIN,
    
    # Color de fondo 
    bg = Color.CONTENIDO.value,
    
    # margen Inferior
    margin_botton = Tamanyo.T10.value,
    
    # Establecemos el margen superior
    margin_top=Tamanyo.T07.value,    
)

Pagina = dict(
    # Limitamos el ancho de la página a 80em definido en generico.py
    max_width = MAX_ANCHO,
    # limitamos el alto de la página a 45em definido en generico.py                    
    max_height = MAX_ALTO,
    # Para que ocupe el 100% lo que hay dentro del vstack
    width="100%",
    # Dejamos un margen de 1.25em en el eje y
    margin_y=Tamanyo.T05.value,
    # Colocamos un relleno de 1.25em alrededor de la página
    padding=Tamanyo.T05.value
)

Privada = dict(
    # Limitamos el ancho de la página a 80em definido en generico.py
    max_width = MAX_ANCHO,
    # limitamos el alto de la página a 45em definido en generico.py                    
    max_height = MAX_ALTO,
    # Para que ocupe el 100% lo que hay dentro del vstack
    width="100%",
    # Dejamos un margen de 1.25em en el eje y
    # margin_y=Tamanyo.T05.value,
    # Colocamos un relleno de 1.25em alrededor de la página
    padding=Tamanyo.T05.value
)

Centrado = dict(
    direction = 'column',
    justify = 'center',
    align = 'center'
)



Seccion = {
    'height': Ancho.A06.value,
    'width': '100%',
    'margin': 'auto',
    # Separación vertical
#    'spacing':Espacio.XXS.value 
}

