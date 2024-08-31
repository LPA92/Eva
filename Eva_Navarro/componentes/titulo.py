# Importamos reflex
import reflex as rx
# importamos los estilos
import Eva_Navarro.estilos.generico as generico
# Importamos los tamaños
from Eva_Navarro.estilos.generico import Tamanyo as Tamanyo

def titulo(text: str) -> rx.Component:
    # heading = cabecera - equivalente a H1-H2... DE HTML
    return rx.heading(
        text,
        # Definimos el tamaño del título. Propiedad propia del componente
        size='4',
        # Ponemos el estilo titulo definido en el archivo generico.py
        style=generico.titulo_estilo,
        # Ponemos un relleno a la izquierda del componente
        padding_left=Tamanyo.DF.value
    )