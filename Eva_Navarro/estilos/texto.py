# Importamos reflex
import reflex as rx

# Importamos los espacios
from Eva_Navarro.estilos.valores import Separacion as Espacio
# Importamos las fuentes
from Eva_Navarro.estilos.fuentes import Fuente as Fuente
# Importamos los pesos de las fuentes
from Eva_Navarro.estilos.fuentes import Trazo as Trazo
# Importamos los colores generales
from Eva_Navarro.estilos.colores import Color as Color
# Importamos los colores para los textos
from Eva_Navarro.estilos.colores import TextoColor as TextoColor
# importamos los valores para los textos
from .valores import Texto as Texto


# Texto de la barra de navegación
# dict = Diccionario
texto_navbar = dict(
    # Tipo de fuente
    font_family = Fuente.LOGO.value,
    # Peso de la fuente
    font_weight = Trazo.NEGRITA.value,
    # Definimos el tamaño del texto en función de la pantalla
    font_size = rx.breakpoints(
        initial=Texto.T04.value,
        xs=Texto.T05.value,
        sm=Texto.T06.value,
        md=Texto.T07.value,
        lg=Texto.T08.value,
        xl=Texto.T09.value,
    ),
    # Color del texto
    color = TextoColor.NAV.value,
    # El texto ocupa el 100% de la pantalla
    # width = '100%',
    # Para cambiar los tamaños de la letra en función de la pantalla
    # display=["flex", "flex", "flex", "flex", "flex"],
)

# Texto de la barra de navegación
# dict = Diccionario
texto_pulsa = dict(
    # Tipo de fuente
    font_family = Fuente.LOGO.value,
    # Peso de la fuente
    font_weight = Trazo.NEGRITA.value,
    # Definimos el tamaño del texto en función de la pantalla
    font_size = rx.breakpoints(
        initial=Texto.T04.value,
        xs=Texto.T05.value,
        sm=Texto.T06.value,
        md=Texto.T07.value,
        lg=Texto.T08.value,
        xl=Texto.T09.value,
    ),
    # Color del texto
    color = TextoColor.NAV.value,
    # El texto ocupa el 100% de la pantalla
    # width = '100%',
    # Para cambiar los tamaños de la letra en función de la pantalla
    # display=["flex", "flex", "flex", "flex", "flex"],
)

# Texto en negrita para la vista inicio
negrita = dict(
    # Definimos el tipo de fuente
    font_family = Fuente.TITULO.value,
    # Definimos el peso de la fuente
    font_weight = Trazo.NEGRITA.value,
    # Establecemos el color de la fuente para el span
    color = TextoColor.CUERPO.value,
    # El texto ocupa el 100% de la pantalla
    # Definimos el tamaño del texto en función de la pantalla
    font_size = rx.breakpoints(
        initial=Texto.T02.value,
        xs=Texto.T03.value,
        sm=Texto.T04.value,
        md=Texto.T05.value,
        lg=Texto.T06.value,
        xl=Texto.T07.value,
    ),    
    # width = '100%',
    # Coloca en el centro los diferentes componentes
    # align='center',
    # Para cambiar los tamaños de la letra en función de la pantalla
    # display=["flex", "flex", "flex", "flex", "flex"],    
)

# Texto normal para la vista inicio
normal = dict(
    # Definimos el tipo de fuente
    font_family = Fuente.TITULO.value,
    # Definimos el peso del texto
    font_weight = Trazo.NORMAL.value,
    # Establecemos el color del texto para el span
    color = TextoColor.CUERPO.value,
    # Definimos el tamaño del texto en función de la pantalla
    font_size = rx.breakpoints(
        initial=Texto.T03.value,
        xs=Texto.T04.value,
        sm=Texto.T05.value,
        md=Texto.T06.value,
        lg=Texto.T07.value,
        xl=Texto.T07.value,
    ),
    # El texto ocupa el 100% de la pantalla
    # width = '100%', 
)

# Texto para el pie de página
texto_pie = dict(
    # Establecemos que el texto ocupe el 100% de la pantalla
    width = '100%',    
    # Centramos el texto verticalmente
    text_align = 'center',
    # Definimos el tamaño del texto en función de la pantalla
    font_size = rx.breakpoints(
        initial=Texto.T01.value,
        xs=Texto.T02.value,
        sm=Texto.T02.value,
        md=Texto.T03.value,
        lg=Texto.T03.value,
        xl=Texto.T03.value,
    ),
    # Definimos el color del texto del pie de página
    color = TextoColor.PIE.value,
    # Para cambiar los tamaños de la letra en función de la pantalla
    # display=["flex", "flex", "flex", "flex", "flex"],
    # El texto ocupa el 100% de la pantalla
    # width = '100%',  
)

# Texto del título que esta encima de la tabla de partidos judiciales
texto_tabla = dict(
    # Definimos el tipo de fuente
    font_family = Fuente.TITULO.value,
    # Definimos el peso del texto
    font_weight = Trazo.NEGRITA.value,
    # Establecemos el color del texto
    color = Color.PRIMARIO.value,
    
    # El texto ocupa el 100% de la pantalla
    width = '100%',    
    
    # Definimos el tamaño del texto en función de la pantalla
    font_size = rx.breakpoints(
        initial=Texto.T07.value,
        xs=Texto.T08.value,
        sm=Texto.T09.value,
        md=Texto.T10.value,
        lg=Texto.T10.value,
        xl=Texto.T10.value,
    ),

    # Para cambiar los tamaños de la letra en función de la pantalla
    display=["flex", "flex", "flex", "flex", "flex"],    
)

# Texto de la vista servicios
texto_servicios = dict(
    # Definimos el tipo de fuente
    font_family = Fuente.TITULO.value,
    # Definimos el peso del texto
    font_weight = Trazo.NEGRITA.value,
    # Establecemos el color del texto
    # Definimos el tamaño del texto en función de la pantalla
    font_size = rx.breakpoints(
        initial=Texto.T05.value,
        xs=Texto.T06.value,
        sm=Texto.T07.value,
        md=Texto.T08.value,
        lg=Texto.T09.value,
        xl=Texto.T10.value,
    ),    
    color = TextoColor.CABEZA.value,
    # El texto ocupa el 100% de la pantalla
    width = '100%',
    # Para cambiar los tamaños de la letra en función de la pantalla
    display=["flex", "flex", "flex", "flex", "flex"],    
)

# Texto de la vista servicios
texto_honorarios = dict(
    
    # Definimos el tipo de fuente
    font_family = Fuente.TITULO.value,
    # Definimos el peso del texto
    font_weight = Trazo.NEGRITA.value,
    # Establecemos el color del texto
    # Definimos el tamaño del texto en función de la pantalla
    font_size = rx.breakpoints(
        initial = Texto.T02.value,
        xs = Texto.T03.value,
        sm = Texto.T04.value,
        md = Texto.T05.value,
        lg = Texto.T06.value,
        xl = Texto.T07.value,
    ),  
    color = TextoColor.CABEZA.value,
    # El texto ocupa el 100% de la pantalla
    width = '100%',
    # Para cambiar los tamaños de la letra en función de la pantalla
    display=["flex", "flex", "flex", "flex", "flex"],    
)

# Texto del botón
# dict = Diccionario
boton_titulo_estilo = dict(
    # Tipo de fuente
    font_family = Fuente.TITULO.value,
    # Peso de la fuente
    font_weight = Trazo.NEGRITA.value,
    # Definimos el tamaño del texto en función de la pantalla
    font_size = rx.breakpoints(
        initial=Texto.T04.value,
        xs=Texto.T05.value,
        sm=Texto.T06.value,
        md=Texto.T07.value,
        lg=Texto.T08.value,
        xl=Texto.T09.value,
    ), 
    color = TextoColor.CABEZA.value,
    # margin_top = Texto.T01.value,
    # El texto ocupa el 100% de la pantalla
    # width = '100%',
    # Para cambiar los tamaños de la letra en función de la pantalla
    # display=["flex", "flex", "flex", "flex", "flex"],        
)

# Texto para el cuerpo del botón
# dict = Diccionario
boton_cuerpo_estilo = dict(
    # Peso de la fuente
    font_weight = Trazo.NORMAL.value,
    # Definimos el tamaño del texto en función de la pantalla
    font_size = rx.breakpoints(
        initial=Texto.T04.value,
        xs=Texto.T05.value,
        sm=Texto.T06.value,
        md=Texto.T07.value,
        lg=Texto.T08.value,
        xl=Texto.T09.value,
    ),  
    # Color del texto del botón
    color = TextoColor.CUERPO.value,
    # Margen del botón
    # margin_buttom = Texto.T07.value,
    # Para cambiar los tamaños de la letra en función de la pantalla
    # display=["flex", "flex", "flex", "flex", "flex"],
    # El texto ocupa el 100% de la pantalla
    # width = '100%',    
)
