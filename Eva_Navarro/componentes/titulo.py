# Importamos reflex
import reflex as rx
# Importamos los diferentes textos
import Eva_Navarro.estilos.texto as formato

# Importamos las rutas
from Eva_Navarro.rutas import Rutas as ruta
# Importamos las fuentes
from Eva_Navarro.estilos.fuentes import Fuente as Fuente
from Eva_Navarro.estilos.fuentes import Trazo as Trazo
# Importamos los colores generales
from Eva_Navarro.estilos.colores import TextoColor as Color
from Eva_Navarro.estilos.colores import Color as Cl

# Importamos los tamaños
from Eva_Navarro.estilos.valores import Texto as Tamanyo

from Eva_Navarro.estilos.generico import Centrado as Centra


def titulo(text: str) -> rx.Component:
    # heading = cabecera - equivalente a H1-H2... DE HTML
    # rx.heading('Nivel 1',as_ = 'h1')
    return rx.heading(
        text,
        align="center",
        as_ = 'h1',
        margin_bottom = Tamanyo.T02.value,
        # Ponemos el estilo titulo definido en el archivo generico.py
        style=formato.texto_tabla,
    )
    
def registro(texto1: str, texto2: str) -> rx.Component:
    # heading = cabecera - equivalente a H1-H2... DE HTML
    # rx.heading('Nivel 1',as_ = 'h1')
    return rx.vstack(
        rx.heading(
            texto1,
            as_ = 'h1',
            margin_bottom = Tamanyo.T02.value,            
            justify = 'center',
            align = 'center',
            # Establecemos el color del texto
            color = Cl.CLARO.value,
        ),
        rx.link(
            rx.heading(
                texto2,
                as_ = 'h2',
                justify = 'center',
                align = 'center',
                color = Cl.CLARO.value,                                
            ),
            href=ruta.INDEX.value,
            size='4'
        ),
        # Definimos el tipo de fuente
        font_family = Fuente.TITULO.value,
        # Definimos el peso del texto
        font_weight = Trazo.NEGRITA.value,
        # Establecemos el color del texto
#        color = Cl.CELDA.value,
            
        # El texto ocupa el 100% de la pantalla
        width = '100%',    
            
        # Definimos el tamaño del texto en función de la pantalla
        font_size = rx.breakpoints(
            initial=Tamanyo.T07.value,
            xs=Tamanyo.T08.value,
            sm=Tamanyo.T09.value,
            md=Tamanyo.T10.value,
            lg=Tamanyo.T10.value,
            xl=Tamanyo.T10.value,
        ),

        # Para cambiar los tamaños de la letra en función de la pantalla
        display=["flex", "flex", "flex", "flex", "flex"],         
        
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