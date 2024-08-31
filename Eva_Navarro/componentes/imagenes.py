# Importamos reflex
import reflex as rx
# Importamos los estilos genericos
import Eva_Navarro.estilos.generico as comun

# Importamos los tamaños
from Eva_Navarro.estilos.generico import Tamanyo as Tamanyo


def img_nav(titulo:str, src: str, alt: str) -> rx.Component:
    return rx.image(
        # ruta donde tenemos la imagen a mostrar
        src,
        # Si no carga la imagen sale el texto alt        
        alt = titulo,
        style = comun.estilo_imagen_NAV,
    )
    
def img_pie(src: str, alt: str) -> rx.Component:
    return rx.image(
        src,
        alt,
        style = comun.estilo_imagen_PIE,
    )   
    
def img_vista(src: str, alt: str) -> rx.Component:
    return rx.image(
        src,
        alt,
        style = comun.estilo_imagen_VISTA, 
    )