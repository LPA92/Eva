# Importamos reflex
import reflex as rx
# Importamos las utilidades
import Eva_Navarro.meta as meta

# Importamos las rutas
from Eva_Navarro.rutas import Rutas as ruta
# Página de navegación
from Eva_Navarro.componentes.navegacion import navegacion
# Contenido de la página de inicio
from Eva_Navarro.vistas.vista_https import vistahttps
# Pie de página
from Eva_Navarro.componentes.pie import pie


# Estamos definiendo que el archivo index.py es una página de la web
@rx.page(
    route = ruta.EXTERNOS.value,
    # Solo admite una cadena alfanumérica.
    title = 'Webs Externas',
    # Solo admite una cadena alfanumérica.
    description = 'Páginas externas de interés para el ámbito judicial',
    image = meta.imagen_externo,
    # meta = Permite añadir o definido en otro archivo
    meta = meta.externo_meta,
)

# Añadimos los componentes que se van a ver en la página principal
def externos() -> rx.Component:
    # box: Caja genérica que se utiliza para usar otros elementos
    return rx.box(
        # Idioma de la página
        meta.lenguaje(),
        # Menu de Navegación
        navegacion(),
        vistahttps(),
        # Pie de página
        pie(),
    ),