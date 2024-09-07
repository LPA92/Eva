# enum = define un conjunto de nombres descriptivos vinculados a valores constantes
# 1rem = Tamaño de la fuente raíz, por defecto 16px
# 1em = Tamaño de la fuente del padre,si no se define el tamaño 16px.
# gap = Espacio entre dos componentes

# Tamaños de pantallas
# SD    =    640 x   480
# QHD =    960 x   540
# HD    = 1.280 x   720
# FHD = 1.920 x 1.080
# QHD = 2.560 x 1.440
# UHD = 3.840 x 2.160
# 8K    = 7.680 x 4.320

# Importamos reflex
import reflex as rx 
# Importamos la librería enum de python
from enum import Enum
# Importamos los colores
from .colores import Color as Color
# Importamos los colores de los textos
from .colores import TextoColor as TextoColor
# Importamos las fuentes
from .fuentes import Fuente as Fuente
# Importamos el peso de las fuentes
from .fuentes import Trazo as Trazo


# En mayúsculas para definir que es una constante
MAX_ANCHO = '80em', # 1em=16px → 1.280 de ancho
MAX_ALTO = '45em',  # 1em=16px →   720 de alto


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

# Tamaños a aplicar en la web
class Tamanyo(Enum):
    ZERO = '0'
    XXS = '0.25em',
    XS = '0.50em',
    S = '0.75em',
    DF = '1.00em',
    M = '1.25em',
    L = '1.50em',
    XL = '1.75em',
    XXL = '2.00em',
    BG = '2.25em',
    VB = '2.50em',
    EB = '2.75em'
    UB = '7.00em',

# Estilos Genéricos a aplicar en toda la página web
ESTILO_GENERICO = {
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
        'border_width': Tamanyo.XS.value,
        # Establecemos el color del borde rojo
        'border_color': Color.BORDE.value,
    },
    rx.table.row_header_cell: {
        # Definimos el color del texto 
        'color': TextoColor.CELDA.value,
        # Definimos el color de fondo de todos las celdas de tablas
        'background_color': TextoColor.CABEZA.value,
        # Establecemos el tipo del borde de la tabla
        'border': 'solid',        
        # Establecemos el grosor del borde de la tabla
        'border_width': Tamanyo.XS.value,
        # Establecemos el color del borde rojo
        'border_color': Color.BORDE.value,
    },
    rx.table.cell: {
        # Definimos el color del texto 
        'color': TextoColor.CELDA.value,
        # Definimos el color de fondo de todos las celdas de tablas
        'background_color': TextoColor.CABEZA.value,
        # Establecemos el tipo del borde de la tabla
        'border': 'solid',        
        # Establecemos el grosor del borde de la tabla
        'border_width': Tamanyo.XS.value,
        # Establecemos el color del borde rojo
        'border_color': Color.BORDE.value,
    },
}


# Texto de la barra de navegación
# dict = Diccionario
navbar_titulo_estilo = dict(
    # Tipo de fuente
    font_family = Fuente.LOGO.value,
    # Peso de la fuente
    font_weight = Trazo.NEGRITA.value,
    # Tamaño de la fuente del botón
    font_size = Tamanyo.L.value,
    color = TextoColor.NAV.value,
)

estilo_imagen_NAV = dict(
    # Establecemos el ancho de la imagen
    width = Tamanyo.L.value,
    # Definimos la altura de la imagen
    height = Tamanyo.L.value,
)

# Texto del título que especifica a un bloque de enlaces
titulo_estilo = dict(
    
    # Definimos el tipo de fuente
    font_family = Fuente.TITULO.value,
    # Definimos el peso de la fuente
    font_weight = Trazo.NEGRITA.value,
    # Establecemos el color de la fuente
    color = Color.PRIMARIO.value,
    # Definimos el tamaño de la fuente
    font_size = Tamanyo.VB.value,
    # El texto ocupa el 100% de la pantalla
    width = '100%',
)

# Texto en negrita para las vistas
negrita = dict(
    # Definimos el tipo de fuente
    font_family = Fuente.TITULO.value,
    # Definimos el peso de la fuente
    font_weight = Trazo.NEGRITA.value,
    # Establecemos el color de la fuente para el span
    color = TextoColor.CUERPO.value,
    # Definimos el tamaño de la fuente para todo lo que contiene el box
    font_size = Tamanyo.M.value,
    # El texto ocupa el 100% de la pantalla
    width = '100%',
    # Coloca en el centro los diferentes componentes
    align='center',
)

# Texto normal para las vistas
normal = dict(
    # Definimos el tipo de fuente
    font_family = Fuente.TITULO.value,
    # Definimos el peso de la fuente
    font_weight = Trazo.NORMAL.value,
    # Establecemos el color de la fuente para el span
    color = TextoColor.CUERPO.value,
    # Definimos el tamaño de la fuente para todo lo que contiene el box
    font_size = Tamanyo.M.value,
    # El texto ocupa el 100% de la pantalla
    width = '100%',
    # Coloca en el centro los diferentes componentes
    align='center',    
)

pie_comun = dict(
    # Establecemos que el texto ocupe el 100% de la pantalla
    width = '100%',    
    # Centramos el texto verticalmente
    text_align = 'center',
    # Definimos el tamaño de la letra
    font_size = Tamanyo.L.value,
    # Definimos el colr del texto del pie de página
    color = TextoColor.PIE.value,
        
    
    # Establecemos el margen superior del pie de página
    margin_top =Tamanyo.ZERO.value,
    # Especificamos el margen inferior
    margin_bottom = Tamanyo.BG.value,

    # Dentro del rx.flex()
    # Distribuye los elementos equitativamente con espacios entre ellos   
    justify = "between",        
    # Coloca en el centro los diferentes componentes
    align='center',

    
    # Dejamos una sepación entre los diferentes componentes
    spacing='2',

    # Ponemos un relleno a la derecha del componente
    padding_x = Tamanyo.XS.value,

)

estilo_imagen_PIE = dict(
    # Establecemos el ancho de la imagen
    width = Tamanyo.L.value,
    # Definimos la altura de la imagen
    height = Tamanyo.L.value,
    # Centramos la imagen
    align = 'center',
    # Establecemos un margen para la imagen
    # margin = Tamanyo.M.value,
)

# Texto del botón
# dict = Diccionario
boton_titulo_estilo = dict(
    # Tipo de fuente
    font_family = Fuente.TITULO.value,
    # Peso de la fuente
    font_weight = Trazo.NEGRITA.value,
    # Tamaño de la fuente del botón
    font_size = Tamanyo.L.value,
    color = TextoColor.CABEZA.value,
    margin_top = Tamanyo.XXS.value,
)

estilo_imagen_VISTA = dict(
    # Establecemos el ancho de la imagen
    width = '80%',
    # Definimos la altura de la imagen
    height = 'auto',
    # Centramos la imagen
)

# cuerpo del botón
# dict = Diccionario
boton_cuerpo_estilo = dict(
    # Peso de la fuente
    font_weight = Trazo.NORMAL.value,
    # Tamaño de la fuente del botón
    font_size = Tamanyo.L.value,
    # Color del texto del botón
    color = TextoColor.CUERPO.value,
    # Margen del botón
    margin_buttom = Tamanyo.XL.value,
)

estilo_Navegacion = dict(
    
    ### PARA FIJAR BARRA DE NAVEGACIÓN AL INICIO DE LA PÁGINA ###
    #  Para fijar la posición position='sticky', top='0' y z_index = '999' 
    position = 'sticky',
    # Se queda fija arriba del todo de la página web
    top='0',
    # Para asegurarnos de que permanece en la parte superior
    z_index = '999',

    # CARACTERISTICAS DEL rx.flex()
    # direction=row Alinea verticalmete,direction=column Alinea horizontalmente,
    align='center',
    # direction=row Alinea horizontalmente,direction=column Alinea verticialmente,
    justify="center",
    # Si ponemos los rx en filas (row) o en columnas (column)
    direction='row',
    # Dejamos una sepación entre la imagen y el hipervinculo
    spacing='2',
    
    # COLOR, PADDING, MARGIN,
    
    # Color de fondo 
    bg = Color.CONTENIDO.value,
    
    # Ponemos un espacio de BG [2,25em (36px)] alrededor del texto en el eje x
    padding_x = Tamanyo.BG.value,
    # Ponemos un espacio de DF [1em (16px)] alrededor del texto en el eje y
    padding_y = Tamanyo.DF.value,

    # margen Inferior
    margin_botton = Tamanyo.VB.value,
)

Pagina = dict(
    # Limitamos el ancho de la página a 80em definido en generico.py
    max_width = MAX_ANCHO,
    # limitamos el alto de la página a 45em definido en generico.py                    
    max_height = MAX_ALTO,
    # Para que ocupe el 100% lo que hay dentro del vstack
    width="100%",
    # Dejamos un margen de 1.25em en el eje y
    margin_y=Tamanyo.M.value,
    # Colocamos un relleno de 1.25em alrededor de la página
    padding=Tamanyo.M.value
)
