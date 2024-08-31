"""Bienvenido a la página web Eva Maria Navarro Naranjo"""

# Importamos reflex
import reflex as rx
# Importamos los estilos
import Eva_Navarro.estilos.generico as generico

# Importamos la página inicio
from Eva_Navarro.paginas.inicio import index
# Importamos la página partidos
from Eva_Navarro.paginas.partidos import partidos
# Importamos la página servicios
from Eva_Navarro.paginas.servicios import servicios
# Importamos la página honorarios
from Eva_Navarro.paginas.honorarios import honorarios
# Importamos la página externos
from Eva_Navarro.paginas.externos import externos
# Importamos la página privada
from Eva_Navarro.paginas.privado import privado

class State(rx.State):
    ### Define tu bakend aqui ###
    ...

# Crea una aplicación con Reflex
app = rx.App(
    # Nos coge todos los estilos del archivo generico.py definidos en la variable HOJA_ESTILOS
    stylesheets=generico.HOJA_ESTILOS,
    # Nos coge todos los estilos del archivo generico definidos en la variable ESTILO_GENERICO
    style=generico.ESTILO_GENERICO
)
