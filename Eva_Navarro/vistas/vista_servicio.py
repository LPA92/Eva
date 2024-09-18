# Importamos reflex
import reflex as rx
# Importamos las escalas
import Eva_Navarro.estilos.escalas as escala
# Importamos los estilos
import Eva_Navarro.estilos.generico as comun

# Importamos la plantilla del texto 
from Eva_Navarro.componentes.titulo import servicio as titulo
# Importamos los tamaños
from Eva_Navarro.estilos.valores import Texto as Tamanyo


# Añadimos los componentes que se van a ver en la página principal
def vistaservicio() -> rx.Component:
    
        # rx.flex = Para poder disponer de componentes flexibles
    return rx.flex(
        # hstack = Posiciona los componentes de forma horizontal
        rx.hstack(
            rx.box(
                # Pone la imagen Servicios.svg
                rx.image(
                    src = '/svg/Servicios.svg',
                    # Si no carga la imagen nos sale el texto definido en alt
                    alt = 'Servicios Procuradora',
                    style = escala.escala_servicio,
                    
                ),
                # Relleno de 1 rem alrededor del box.
                padding = Tamanyo.T04.value,
                margin_top = Tamanyo.T12.value,
                margin_righ = Tamanyo.T05.value,
            ),            
            rx.box(     
                # Creamos una caja flexible parea alterar sus dimnensiones y llenar el espacio disponible
                # Creamos una caja flexible parea alterar sus dimnensiones y llenar el espacio disponible
                rx.flex(
                    rx.vstack(
                        titulo(
                            '- Presentación de demandas, escritos y documentación.',
                        ),
                        rx.spacer(),
                        rx.spacer(),
                        titulo(
                                '- Representación procesal de los clientes.',
                        ),
                        rx.spacer(),
                        rx.spacer(),
                        titulo(
                            '- Emplazamientos y citaciones judiciales.',
                        ),
                        rx.spacer(),
                        rx.spacer(),
                        titulo(
                            '- Asistir con la comision judicial, a los lanzamientos de deshaucios.',
                        ),
                        rx.spacer(),
                        rx.spacer(),
                        titulo(
                            '- Notificaciones de resoluciones judiciales.',
                        ),
                        rx.spacer(),
                        rx.spacer(),
                        titulo(
                            '- Seguimiento de los procedimientos judiciales.',
                        ),
                        rx.spacer(),
                        rx.spacer(),
                        titulo(
                            '- Control de señalamientos y plazos judiciales.',
                        ),
                        rx.spacer(),
                        rx.spacer(),
                        titulo(
                            '- Utilización diaria de las Nuevas Tecnologías.',
                        ),
                    ),
                    style = comun.Flexible,
                    width ='100%',
                ),
            ),
            width ='100%',
        ), 
    )