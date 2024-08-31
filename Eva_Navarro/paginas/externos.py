# Importamos reflex
import reflex as rx
# Importamos las utilidades
import Eva_Navarro.meta as meta

# Página de navegación
from Eva_Navarro.componentes.navegacion import navegacion
# Contenido de la página de inicio
from Eva_Navarro.vistas.vista_https import vistahttps
# Pie de página
from Eva_Navarro.componentes.pie import pie


# Estamos definiendo que el archivo index.py es una página de la web
@rx.page(
    # Solo admite una cadena alfanumérica.
    title = 'Páginas externas de interes judicial',
    # Solo admite una cadena alfanumérica.
    description='Esta es la página de páginas externas',
    image='/svg/https.svg',
    # meta = Permite añadir o definido en otro archivo
    meta = meta.indice_meta,
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