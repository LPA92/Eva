# Importamos reflex
import reflex as rx
# Importamos las escalas
import Eva_Navarro.estilos.escalas as escala

# Importamos la plantilla de párrafos
from Eva_Navarro.componentes.info_profesional import texto_inicio
# Importamos las plantillas de imagenes para la vista


# Añadimos los componentes que se van a ver en la página principal
def vistaprivada() -> rx.Component:
    
        # vstack = Posiciona los componentes de forma vertical
    return rx.vstack(
        # hstack = Posiciona los componentes de forma horizontal
        rx.hstack(
            # Pone la imagen Servicios.svg
            rx.image(
                src = '/svg/UE.svg',
                # Si no carga la imagen nos sale el texto definido en alt
                alt = 'Imagen de área privada',
                style = escala.escala_privada,
            ),
            rx.box(     
                # Creamos una caja flexible parea alterar sus dimnensiones y llenar el espacio disponible
                rx.flex(
                    texto_inicio(
                        'Area Privada',
                        'Solo acceso a personas autorizadas',
                    ),
                ),
            ),
        ),            
    )