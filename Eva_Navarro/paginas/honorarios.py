# Importamos reflex
import reflex as rx
# Importamos las utilidades
import Eva_Navarro.meta as meta

# Importamos las rutas
from Eva_Navarro.rutas import Rutas as ruta
# Página de navegación
from Eva_Navarro.componentes.navegacion import navegacion
# Contenido de la página de inicio
from Eva_Navarro.vistas.vista_honorario import vistahonorario
# Pie de página
from Eva_Navarro.componentes.pie import pie


# Estamos definiendo que el archivo index.py es una página de la web
@rx.page(
    route = ruta.HONORARIOS.value,
    # Solo admite una cadena alfanumérica.
    title = 'Honorarios de los Procuradores',
    # Solo admite una cadena alfanumérica.
    description = 'Esta es la página de los honorarios de la Procuradora Eva Navarro',
    image=meta.imagen_honorarios,
    # meta = Permite añadir o definido en otro archivo
    meta = meta.honorarios_meta,
)

# Añadimos los componentes que se van a ver en la página principal
def honorarios() -> rx.Component:
    # box: Caja genérica que se utiliza para usar otros elementos
    return rx.box(
        # Idioma de la página
        meta.lenguaje(),
        # Menu de Navegación
        navegacion(),
        vistahonorario(),
        # Pie de página
        pie(),
    ),