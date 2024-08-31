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
    UB = '3.00em', 

# Estilos Genéricos a aplicar en toda la página web
ESTILO_GENERICO = {
    # Establecemos la fuente por defecto
    'font_family': Fuente.DEFECTO.value,
    # Definimos el peso de la fuente por defecto
    'font_weight': Trazo.NORMAL.value,
    'background_color': Color.FONDO.value,

    # Todos los botones van a tener el mismo estilo
    rx.button: {
        # Para ocupar todo el ancho disponible
        'width': '100%',
        # Para ocupar toda la altura disponible
        'height':'100%',
        # Definimos el radio del borde
        'border_radius':Tamanyo.DF.value,
        # Definimos el color del texto en los botones
        'color': TextoColor.CABEZA.value,
        # Definimos el color de fondo de todos los botones
        'background_color': Color.CONTENIDO.value,

        # Si no entra en una línea, nos aparezca en dos líneas
        'white_space': 'normal',
        # Para alinear el texto al principio de la página web
        'text_align': 'start',

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
}


# Texto de la barra de navegación
# dict = Diccionario
navbar_titulo_estilo = dict(
    # Tipo de fuente
    font_family = Fuente.LOGO.value,
    # Peso de la fuente
    font_weight = Trazo.NEGRITA.value,
    # Tamaño de la fuente del botón
    font_size = Tamanyo.DF.value,
    color = TextoColor.NAV.value,
)

# Texto del título que especifica a un bloque de enlaces
titulo_estilo = dict(

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
    font_size = Tamanyo.L.value,
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
    font_size = Tamanyo.L.value,
    # El texto ocupa el 100% de la pantalla
    width = '100%',
    # Coloca en el centro los diferentes componentes
    align='center',    
)

pie_comun = dict(
    # Definimos el tamaño de la letra
    font_size = Tamanyo.DF.value,
    # Establecemos el margen superior del pie de página
    margin_top =Tamanyo.ZERO.value,
    # El texto ocupa el 100% de la pantalla
    width = '100%',
    # Coloca en el centro los diferentes componentes
    align='center',     
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

estilo_imagen_NAV = dict(
    # Establecemos el ancho de la imagen
    width = Tamanyo.DF.value,
    # Definimos la altura de la imagen
    height = Tamanyo.DF.value,
    # Centramos la imagen
    align = 'center',
    # Establecemos un margen para la imagen
    margin = Tamanyo.M.value    
)

estilo_imagen_PIE = dict(
    # Establecemos el ancho de la imagen
    width = Tamanyo.S.value,
    # Definimos la altura de la imagen
    height = Tamanyo.S.value,
    # Centramos la imagen
    align = 'center',
    # Establecemos un margen para la imagen
    margin = Tamanyo.M.value
)

estilo_imagen_VISTA = dict(
    # Establecemos el ancho de la imagen
    width = Tamanyo.UB.value,
    # Definimos la altura de la imagen
    height = Tamanyo.UB.value,
    # Centramos la imagen
    align = 'center',
    # Establecemos un margen para la imagen
    margin = Tamanyo.M.value
)

# cuerpo del botón
# dict = Diccionario
boton_cuerpo_estilo = dict(
    # Peso de la fuente
    font_weight = Trazo.NORMAL.value,
    # Tamaño de la fuente del botón
    font_size = Tamanyo.DF.value,
    # Color del texto del botón
    color = TextoColor.CUERPO.value,
    # Margen del botón
    margin_buttom = Tamanyo.XXL.value,
)