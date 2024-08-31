# Importamos reflex
import reflex as rx
# Importamos los estilos
import Eva_Navarro.estilos.generico as generico
# Importamos los tamaños
from Eva_Navarro.estilos.generico import Tamanyo as Tamanyo
# Importamos los colores generales
from Eva_Navarro.estilos.colores import Color as Color
# Importamos los colores de los textos
from Eva_Navarro.estilos.colores import TextoColor as TextoColor
# Importamos las rutas
from Eva_Navarro.rutas import Router as ruta
# Importamos el botón flotante de la librería ant.design
from Eva_Navarro.componentes.antd_react import boton_flotante
# Importamos la plantilla de imagenes
from Eva_Navarro.componentes.imagenes import img_nav as imagen

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, font_size=Tamanyo.DF.value), href=url
    )


# Definimos el componente navbar
def navegacion() -> rx.Component:
    # hstack: Para ver a los componentes en forma horizontal
    return rx.hstack(
        #### Página de Inicio ####
        # rx.link = Para ir a otra página web
        rx.link(
            rx.box(
                rx.text.span(
                    'Eva Mª ',
                    color = Color.PRIMARIO.value,
                ),
                rx.text.span(
                    'Navarro',
                    color = Color.SECUNDARIO.value,
                ),
                style = generico.navbar_titulo_estilo,
            ),
            # Para que regrese a la página principal
            href=ruta.INDEX.value,
        ),
        
        # tabs.root -> Donde se definen las pestañas de la web
        # tabs.list -> Donde se colocan los tabs.trigger
        # tabs.trigger -> Nombre de la pestaña y color del texto
        # tabs.content -> para poner una descripción enla pestaña
        
        rx.hstack(
            rx.hstack(
                imagen(
                    src = '/svg/NV_Inicio.svg',
                    alt = 'Inicio',
                ),
                navbar_link("Inicio", "/"),
            ),
            rx.hstack(
                imagen(
                    src = '/svg/NV_Partidos.svg',
                    alt = 'Partidos Judiciales ',
                ),
                navbar_link("Partidos", ruta.PARTIDOS.value),
            ),            
            rx.hstack(
                imagen(
                    src = '/svg/NV_Servicios.svg',
                    alt = ' Servicios Procuradora',
                ),
                navbar_link("Servicios", ruta.SERVICIOS.value),
            ),            
            
            rx.hstack(
                imagen(
                    src = '/svg/NV_Honorarios.svg',
                    alt = 'Honorarios Procuradora ',
                ),
                navbar_link("Honorarios", ruta.HONORARIOS.value),
            ),            
            rx.hstack(
                imagen(
                    src = '/svg/NV_Externas.svg',
                    alt = 'Paginas Externas',
                ),
                navbar_link("Externas", ruta.EXTERNOS.value),
            ),  
            rx.hstack(
                imagen(
                    src = '/svg/NV_Privada.svg',
                    alt = 'Area Privada',
                ),
                navbar_link("Privada", ruta.PRIVADO.value),
            ),
            justify="end",
            spacing="5",
        ),        

        # Añadimos el botón flotante de la librería ant.design
        boton_flotante(
            icon = rx.image(
                src = '/svg/Logo_Procurador.svg',
                alt = ' Logo Procurador',
                width = 'auto',
                height = 'auto',
            ),
            href = ruta.INDEX.value,
            # Posición fija ponemos position=’sticky y top=’0’
            position = 'sticky',
            # Se queda fija arriba del todo de la página web
            top='0',            
        ),
        justify="between",
        align_items="center",
        # Posición fija hay que poner position=’sticky y top=’0’
        position = 'sticky',
        # Se queda fija arriba del todo de la página web
        top='0',
        # Color de fondo 
        bg = Color.CONTENIDO.value,
        # Ponemos un espacio de BG [2,25em (36px)] alrededor del texto en el eje x
        padding_x = Tamanyo.BG.value,
        # Ponemos un espacio de DF [1em (16px)] alrededor del texto en el eje y
        padding_y = Tamanyo.DF.value,
        # Para asegurarnos de que permanece en la parte superior
        z_index = '999',
        # margen Inferior
        margin_botton = Tamanyo.VB.value,
    )
