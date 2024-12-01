# Importamos reflex
import reflex as rx
# Importamos las utilidades
# import Eva_Navarro.meta as meta
# Importamos la libreria requests para realizar el post
import requests as rq
# Importamos las expresiones regulares
import re
# Importamos el estado
import Eva_Navarro.estilos.estado as estado
# Importamos los estilos
import Eva_Navarro.estilos.generico as comun

# Importamos las rutas
from Eva_Navarro.rutas import Rutas as ruta
# Página de navegación
from Eva_Navarro.componentes.navegacion import navegacion
# Contenido de la página del área privada
from Eva_Navarro.vistas.vista_privada import vistaprivada
# Pie de página
from Eva_Navarro.componentes.pie import pie

# Contenido de la página del área privada
# from Eva_Navarro.vistas.vista_acceso import vistaacceso

# Importamos las expresiones regulares
import re
# Importamos las escalas
import Eva_Navarro.estilos.escalas as escala

# Importamos los colores
from Eva_Navarro.estilos.colores import Color as Color
# Importamos los tamaños
from Eva_Navarro.estilos.valores import Texto as Tamanyo
# Importamos la plantilla de información profesional
from Eva_Navarro.componentes.titulo import titulo as titulo


# Importamos los espacios
from Eva_Navarro.estilos.valores import Separacion as Espacio


# Estamos definiendo que el archivo provado.py es una página de la web
@rx.page(
    route = ruta.PRIVADO.value,
    # Solo admite una cadena alfanumérica.
    title = 'Area Privada',
    # Solo admite una cadena alfanumérica.
    description = 'Esta es el área privada de la Procuradora Eva Navarro',
    # image = meta.imagen_privado,
    # meta = Permite añadir o definido en otro archivo
    # meta = meta.privado_meta,
)

# Añadimos los componentes que se van a ver en la página principal
def privado() -> rx.Component:
    # box: Caja genérica que se utiliza para usar otros elementos
    return rx.box(
        # Idioma de la página
        # meta.lenguaje(),
        # Menu de Navegación
        navegacion(),
        rx.center(
            rx.vstack(            
                rx.hstack(
                vistaprivada(),
                style = comun.Privada,
                ),
            ),
        ),
        # Pie de página
        pie(),
    ),
    
