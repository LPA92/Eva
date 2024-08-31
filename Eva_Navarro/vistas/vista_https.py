# Importamos reflex
import reflex as rx

from Eva_Navarro.estilos.colores import TextoColor as TextoColor
# Importamos la plantilla de párrafos
from Eva_Navarro.componentes.info_profesional import texto_inicio
# Importamos las plantillas de imagenes para la vista
from Eva_Navarro.componentes.imagenes import img_vista as imagen

# Añadimos los componentes que se van a ver en la página principal
def vistahttps() -> rx.Component:
    
        # vstack = Posiciona los componentes de forma vertical
    return rx.vstack(
        # hstack = Posiciona los componentes de forma horizontal
        rx.hstack(
            # Pone la imagen Servicios.svg
            imagen(
                src = '/svg/https.svg',
                # Si no carga la imagen nos sale el texto definido en alt
                alt='Imagen de páginas externas',
            ),
            rx.box(     
                # Creamos una caja flexible parea alterar sus dimnensiones y llenar el espacio disponible
                rx.flex(
                    texto_inicio(
                        'Páginas externas',
                        'de interes judicial',
                    ),
                ),
            ),
        ),            
    )