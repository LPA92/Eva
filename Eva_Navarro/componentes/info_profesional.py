# Importamos reflex
import reflex as rx
# Importamos los estilos
import Eva_Navarro.estilos.generico as generico
# Importamos los tamaños
from Eva_Navarro.estilos.generico import Tamanyo as Tamanyo
# Importamos las fuentes
from Eva_Navarro.estilos.fuentes import Fuente as Fuente
# Importamos los pesos de las fuentes
from Eva_Navarro.estilos.fuentes import Trazo as Trazo
# Importamos los colores generales
from Eva_Navarro.estilos.colores import Color as Color
# Importamos los colores para los textos
from Eva_Navarro.estilos.colores import TextoColor as TextoColor

def texto_inicio(titulo: str, cuerpo: str) -> rx.Component:
    return rx.box(
        # Para poner un span → text.span
        rx.text.span(
            titulo,
            style = generico.negrita
        ),
        f' {cuerpo}',
        style = generico.normal
    )
    
def texto_parrafo(titulo: str, cuerpo: str, texto: str) -> rx.Component:
    return rx.box(
        # Para poner un span → text.span
        # Texto normal
        rx.text.span(
            titulo,
            style = generico.normal
        ),
        # Texto negrita
        rx.text.span(
            cuerpo,
            style = generico.negrita
        ),        
        # Texto normal
        rx.text.span(
            texto,
            style = generico.normal
        ),
    )    