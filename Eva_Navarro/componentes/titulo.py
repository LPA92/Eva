# Importamos reflex
import reflex as rx
# Importamos los diferentes textos
import Eva_Navarro.estilos.texto as formato


def titulo(text: str) -> rx.Component:
    # heading = cabecera - equivalente a H1-H2... DE HTML
    return rx.heading(
        text,
        # Ponemos el estilo titulo definido en el archivo generico.py
        style=formato.texto_tabla,
    )
    
# Texto para la vista de servicios
def servicio(text: str) -> rx.Component:
    # heading = cabecera - equivalente a H1-H2... DE HTML
    return rx.heading(
        text,
        # Ponemos el estilo titulo definido en el archivo generico.py
        style=formato.texto_servicios,
    )
    
# Texto para la vista de servicios
def honorarios(text: str) -> rx.Component:
    # heading = cabecera - equivalente a H1-H2... DE HTML
    return rx.heading(
        text,
        # Ponemos el estilo titulo definido en el archivo generico.py
        style=formato.texto_honorarios,
    )     