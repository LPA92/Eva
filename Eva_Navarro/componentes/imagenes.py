# Importamos reflex
import reflex as rx
# Importamos los diferentes textos
import Eva_Navarro.estilos.texto as formato
# Importamos las escalas
import Eva_Navarro.estilos.escalas as escala
import Eva_Navarro.estilos.generico as comun


# Importamos los colores del texto
from Eva_Navarro.estilos.colores import TextoColor as TextoColor
# Importamos las rutas
from Eva_Navarro.rutas import Rutas as ruta
# Importamos los tamaños del texto
from Eva_Navarro.estilos.valores import Texto as Texto


def img_pie(src: str, alt: str, texto: str) -> rx.Component:
    return rx.flex(
        rx.image(
            # ruta donde tenemos la imagen a mostrar
            src,
            # Si no carga la imagen sale el texto alt        
            alt,
            # Estilo común de la imagen definido en el archivo generico.py
            style = escala.escala_nav,
        ),
        rx.text(
            # Texto que aparece dentro del link
            texto,
            # Estilo común del texto definido en el archivo generico.py
            style = formato.texto_navbar,
        ),
        # Dejamos una sepación entre la imagen y el hipervinculo
        spacing = '4',
        # style = comun.Flexible,
    )
    
def nav(src: str, alt: str, texto: str, url:str) -> rx.Component:
    return rx.flex(
        rx.image(
            # ruta donde tenemos la imagen a mostrar
            src,
            # Si no carga la imagen sale el texto alt        
            alt,
            style = escala.escala_nav,
#           display=["flex", "flex", "flex", "flex", "flex"]
        ),    
        rx.link(
            # Texto que aparece dentro del link
            texto,
            # Definimos el tamaño de la imagen según la pantalla
            style = formato.texto_navbar,
            # Hipervinculo que nos dirigue a otra página
            href=url,                  
        ),
        # Dejamos una sepación entre la imagen y el hipervinculo
        spacing = '4',
    )
    
def logo(src: str, alt: str, texto: str, titulo: str) -> rx.Component:
    return rx.flex(
        rx.image(
            # ruta donde tenemos la imagen a mostrar
            src,
            # Si no carga la imagen sale el texto alt        
            alt,
            # Estilo común de la imagen definido en el archivo generico.py
            style = escala.escala_nav,
        ),
        # Para que al pasar el ratón sobre él nos muestre el content
        rx.tooltip(
            rx.link(
                rx.button(
                    titulo,
                    style = formato.texto_navbar,
                    color = TextoColor.NAV.value,
                ),
                href=ruta.INDEX.value,
            ),
            content = texto,            
            side = 'bottom',
        ),
        # Dejamos una sepación entre la imagen y el hipervinculo
        # spacing = '4',
        style = comun.Flexible,
    )