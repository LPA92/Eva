# Importamos reflex
import reflex as rx
# Importamos los estilos
import Eva_Navarro.estilos.generico as comun

# Importamos los tamaños
from Eva_Navarro.estilos.valores import Texto as Tamanyo

from Eva_Navarro.estilos.colores import TextoColor
# Importamos las rutas
from Eva_Navarro.rutas import Rutas as ruta
# Importamos el botón flotante de la librería ant.design
from Eva_Navarro.componentes.antd_react import boton_flotante
# Importamos la plantilla de imagenes
from Eva_Navarro.componentes.imagenes import nav as  nav


class TabsState(rx.State):
    """The app state."""

    value = 'Incio'
    tab_selected = ''

    def change_value(self, val):
        self.tab_selected = f"{val} clicked!"
        self.value = val


# Definimos el componente navbar
def navegacion() -> rx.Component:
    # hstack: Para ver a los componentes en forma horizontal
    return rx.center(
        rx.flex(
            rx.text(f"{TabsState.value}  clicked !"),
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger(
                        nav(
                            '/svg/NV_Inicio.svg',
                            'Página Principal',
                            'Inicio',
                            ruta.INDEX.value,
                        ),
                        value='Inicio',
                    ),
                    rx.tabs.trigger(
                        nav(
                            '/svg/Partidos.svg',
                            'Partidos Judiciales',
                            'Partidos',
                            ruta.PARTIDOS.value,
                        ),
                        value='Partidos',
                    ),                      
                    rx.tabs.trigger(
                        nav(
                            '/svg/NV_SERVICIOS.svg',
                            'Servicios Procuradora',
                            'Servicios',
                            ruta.SERVICIOS.value,
                        ),
                        value='Servicios',
                    ),
                    rx.tabs.trigger(
                        nav(
                            '/svg/NV_Honorarios.svg',
                            'Honorarios de la Procuradora',
                            'Honorarios',
                            ruta.HONORARIOS.value,
                        ),
                        value='Honorarios', 
                    ),
                    rx.tabs.trigger(
                        nav(
                            '/svg/NV_Externas.svg',
                            'Webs Externas',
                            'Externas',
                            ruta.EXTERNOS.value,
                        ),
                        value='Externas',
                    ),                    
                    rx.tabs.trigger(                    
                        nav(
                            '/svg/NV_Privada.svg',
                            'Area Privada',
                            'Privada',
                            ruta.PRIVADO.value,
                        ),
                        value='Privada',
                    ),
                ),
                default_value='Inicio',
                value=TabsState.value,
                on_change=lambda x: TabsState.change_value(
                    x
                ),
            ),

            # Añadimos el botón flotante de la librería ant.design
            boton_flotante(
                icon = rx.image(
                    src = '/svg/Logo_Procurador.svg',
                    alt = ' Logo Procurador',
                    width='200%',
                    ),
                    href = ruta.INDEX.value,
                    # Posición fija ponemos position=’sticky y top=’0’
                    position = 'sticky',
                    # Se queda fija arriba del todo de la página web
                    top='0',
            ),
            # Separación entre los diferentes funciones que contiene el rx.flex
            spacing = '8',
            # Establecemos el estilo definido para la navegación
            style = comun.Fijo_Nav,
        ),
    ),
