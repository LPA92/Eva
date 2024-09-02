# Importamos reflex
import reflex as rx
# Importamos los estilos genericos
import Eva_Navarro.estilos.generico as comun

# Importamos los tamaños
from Eva_Navarro.estilos.generico import Tamanyo as Tamanyo
# Importamos los colores del texto
from Eva_Navarro.estilos.colores import TextoColor as TextoColor
# Importamos los colores de fondo
from Eva_Navarro.estilos.colores import Color as Color


def img_pie(src: str, alt: str, texto: str) -> rx.Component:
    return rx.flex(
        rx.image(
            # ruta donde tenemos la imagen a mostrar
            src,
            # Si no carga la imagen sale el texto alt        
            alt,
            # Estilo común de la imagen definido en el archivo generico.py
            style = comun.estilo_imagen_NAV,
        ),
        rx.text(
            # Texto que aparece dentro del link
            texto,
            # Estilo común del texto definido en el archivo generico.py
            style=comun.navbar_titulo_estilo,
        ),
        # Dejamos una sepación entre la imagen y el hipervinculo
        spacing='2',
        # row = fila  column = columna
        direction='row',
        # direction=row Alinea verticalmete,direction=column Alinea horizontalmente,
        align='center',
        # direction=row Alinea horizontalmente,direction=column Alinea verticialmente,        
        justify='between',
        margin_top=Tamanyo.L.value,
    )

    
def img_vista(src: str, alt: str, width: str ) -> rx.Component:
    return rx.image(
        src,
        alt,
        width,
        height = 'auto',
        align = 'center',       
    )
    
def nav(src: str, alt: str, texto: str, url:str) -> rx.Component:
    return rx.flex(
        rx.image(
            # ruta donde tenemos la imagen a mostrar
            src,
            # Si no carga la imagen sale el texto alt        
            alt,
            # Estilo común de la imagen definido en el archivo generico.py
            style = comun.estilo_imagen_NAV,
        ),
        rx.link(
            # Texto que aparece dentro del link
            texto,
            # Estilo común del texto definido en el archivo generico.py
            style=comun.navbar_titulo_estilo,
            # Hipervinculo que nos dirigue a otra página
            href=url,                  
        ),
        # Dejamos una sepación entre la imagen y el hipervinculo
        spacing='2',
        # row = fila  column = columna
        direction='row',
        # direction=row Alinea verticalmete,direction=column Alinea horizontalmente,
        align='center',
        # direction=row Alinea horizontalmente,direction=column Alinea verticialmente,        
        justify='between',
        margin_top=Tamanyo.L.value,
        
    )
    
def logo(src: str, alt: str, texto: str, titulo: str) -> rx.Component:
    return rx.flex(
        rx.image(
            # ruta donde tenemos la imagen a mostrar
            src,
            # Si no carga la imagen sale el texto alt        
            alt,
            # Estilo común de la imagen definido en el archivo generico.py
            style = comun.estilo_imagen_NAV,
        ),
        # Para que al pasar el ratón sobre él nos muestre el content
        rx.tooltip(
            rx.button(
                titulo,
                style=comun.navbar_titulo_estilo,
                color = TextoColor.NAV.value,
                ),
                content=texto,
                side='bottom',
                ),
        # Dejamos una sepación entre la imagen y el hipervinculo
        spacing='2',
        # row = fila  column = columna
        direction='row',
        # direction=row Alinea verticalmete,direction=column Alinea horizontalmente,
        align='center',
        # direction=row Alinea horizontalmente,direction=column Alinea verticialmente,        
        justify='between',
        margin_top=Tamanyo.L.value,
    )