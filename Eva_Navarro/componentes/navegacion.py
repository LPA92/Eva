# Importamos reflex
import reflex as rx

# Importamos los tamaños
from Eva_Navarro.estilos.generico import Tamanyo as Tamanyo
# Importamos los colores generales
from Eva_Navarro.estilos.colores import Color as Color
# Importamos los colores de los textos
from Eva_Navarro.estilos.colores import TextoColor as TextoColor
# Importamos las rutas
from Eva_Navarro.rutas import Rutas as ruta
# Importamos el botón flotante de la librería ant.design
from Eva_Navarro.componentes.antd_react import boton_flotante
# Importamos la plantilla de imagenes
from Eva_Navarro.componentes.imagenes import nav as  nav


# Definimos el componente navbar
def navegacion() -> rx.Component:
    # hstack: Para ver a los componentes en forma horizontal
    return rx.center(
        rx.flex(
            nav(
                '/svg/NV_Inicio.svg',
                'Página Principal',
                'Inicio',
                ruta.INDEX.value,
            ),
            nav(
                '/svg/Partidos.svg',
                'Partidos Judiciales',
                'Partidos',
                ruta.PARTIDOS.value,
            ),                        
            nav(
                '/svg/NV_SERVICIOS.svg',
                'Servicios Procuradora',
                'Servicios',
                ruta.SERVICIOS.value,
            ),                        
            nav(
                '/svg/NV_Honorarios.svg',
                'Honorarios de la Procuradora',
                'Honorarios',
                ruta.HONORARIOS.value,
            ),            
            nav(
                '/svg/NV_Externas.svg',
                'Webs Externas',
                'Externas',
                ruta.EXTERNOS.value,
            ),
            nav(
                '/svg/NV_Privada.svg',
                'Area Privada',
                'Privada',
                ruta.PRIVADO.value,
            ),
            # Añadimos el botón flotante de la librería ant.design
            boton_flotante(
                icon = rx.image(
                    src = '/svg/Logo_Procurador.svg',
                    alt = ' Logo Procurador',
                    width='100%',
                    ),
                    href = ruta.INDEX.value,
                    # Posición fija ponemos position=’sticky y top=’0’
                    position = 'sticky',
                    # Se queda fija arriba del todo de la página web
                    top='0',
            ),
            # Separación horizontal entre los diferentes elementos que contiene el flex
            spacing='5',
        ),
        # Establecemos el margen superior
        margin_top=Tamanyo.XL.value,
    ),