# Importamos reflex
import reflex as rx

# Importamos los tamaños
from Eva_Navarro.estilos.texto import Texto as Tamanyo
# Importamos los espacios
from Eva_Navarro.estilos.generico import Espacio as Espacio

rejilla = dict(
    # auto_fit: Crea tantas columnas como quepa dentro del contenedor
    # minmax: 13em es el tamaño minimo y una fraccion el máximo que puede ocupar la columna.
#    grid_template_columns=[
#        "repeat(auto_fit,minmax(15em, 1fr)",
#    ],

    # Separacion vertical entre las imagenes
    gap = Tamanyo.T09.value,
    # Creamos el número de columnas según la pantalla
    grid_template_columns=[
        # Para el tamaño de pantalla más pequeño
        "1fr",
        # Para el tamaño de pantalla pequeño
        "repeat(2, 1fr)",
        # Para el tamaño de pantalla mediano
        "repeat(2, 1fr)",
        # Para el tamaño de pantalla intermedio
        "repeat(3, 1fr)",
        # Para el tamaño de pantalla más grandre
        "repeat(4, 1fr)",
    ],
    # Para ocupar el máximo dentro de la columna
    width="100%",
)

                