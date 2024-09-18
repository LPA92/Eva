# Importamos reflex
import reflex as rx

# Importamos los tamaños
from Eva_Navarro.estilos.texto import Texto as Tamanyo
# Importamos los espacios
from Eva_Navarro.estilos.generico import Espacio as Espacio

rejilla = dict(
    # auto_fit: Crea tantas columnas como quepa dentro del contenedor
    # minmax: 13em es el tamaño minimo y una fraccion el máximo que puede ocupar la columna.
    grid_template_columns=[
        "repeat(auto_fit,minmax(15em, 1fr)",
    ],
    # Para dejar una separación vertical entre las imagenes
    gap = Tamanyo.T04.value,
    # Separacion horizontal de las imagenes
    spacing = '1',
    # Creamos el número de columnas según la pantalla
    columns = rx.breakpoints(
        initial=Espacio.XXS.value,
        xs=Espacio.XS.value,
        sm=Espacio.S.value,
        md=Espacio.DF.value,
        lg=Espacio.M.value,
        xl=Espacio.L.value,
    ),
    width="100%",
)

                