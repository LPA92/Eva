## Importamos reflex
import reflex as rx
# Importamos las utilidades
# import Eva_Navarro.meta as meta
# Importamos los estilos
import Eva_Navarro.estilos.generico as comun

# Importamos las rutas
from Eva_Navarro.rutas import Rutas as ruta
# Página de navegación
from Eva_Navarro.componentes.navegacion import navegacion
# Contenido de la página de inicio
from Eva_Navarro.vistas.vista_acceso import vistaacceso
# Pie de página
from Eva_Navarro.componentes.pie import pie




# Estamos definiendo que el archivo index.py es una página de la web
@rx.page(
    route = ruta.ACCESO.value,
    # Solo admite una cadena alfanumérica.
    title = 'Area Privada',
    # Solo admite una cadena alfanumérica.
    description = 'Solo para personal autorizado',
    # image = meta.imagen_privado,
    # meta = Permite añadir o definido en otro archivo
    # meta = meta.externo_meta,
)

# Añadimos los componentes que se van a ver en la página principal
def acceso() -> rx.Component:
    # box: Caja genérica que se utiliza para usar otros elementos
    return rx.box(
        # Idioma de la página
        meta.lenguaje(),
        # Menu de Navegación
        navegacion(),
        rx.center(
            rx.vstack(            
                vistaacceso(),
                style = comun.Pagina,
            ),
        ),
        # Pie de página
        pie(),
    ),