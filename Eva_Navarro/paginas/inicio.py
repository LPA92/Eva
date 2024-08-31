# Importamos reflex
import reflex as rx
# Importamos las utilidades
import Eva_Navarro.meta as meta
# Iportamos los estilos
import Eva_Navarro.estilos.generico as comun

# Importamos los tamaños
from Eva_Navarro.estilos.generico import Tamanyo as Tamanyo 
# Página de navegación
from Eva_Navarro.componentes.navegacion import navegacion
# Contenido de la página de inicio
from Eva_Navarro.vistas.vista_inicio import vistainicio
# Pie de página
from Eva_Navarro.componentes.pie import pie


# Estamos definiendo que el archivo inicio.py es una página de la web
@rx.page(
    # Solo admite una cadena alfanumérica.
    title = 'Página de inicio',
    # Solo admite una cadena alfanumérica.
    description='Esta es la página de inicio de la Procuradora Eva Navarro',
    image='/svg/Logo_Procurador.svg',
    # meta = Permite añadir o definido en otro archivo
    meta = meta.indice_meta,
    
)

# Añadimos los componentes que se van a ver en la página principal
def index() -> rx.Component:
    # box: Caja genérica que se utiliza para usar otros elementos
    return rx.box(
        # Idioma de la página
        meta.lenguaje(),
        # Menu de Navegación
        navegacion(),
        vistainicio(),
        # Pie de página
        pie(),
        # Limitamos el ancho de la página a 80em definido en generico.py
        max_width=comun.MAX_ANCHO,
        # limitamos el alto de la página a 45em definido en generico.py
        max_height = comun.MAX_ALTO,
        # Para que ocupe el 100% lo que hay dentro del vstack
        width='100%',
        # dejamos un margen de 1.25em en el eje y
        margin_y=Tamanyo.XXL,
        # Ponemos todos los textos al margén izquierdo de la pantalla
        align='center',      
    ),