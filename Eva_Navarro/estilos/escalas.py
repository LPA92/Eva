# Importamos reflex
import reflex as rx
# Importamos los valores para las imagenes
from .valores import Imagen as Imagen


# Escala para las imagenes del menu de navegación
escala_nav = dict(

    width = rx.breakpoints(
        initial = Imagen.I01.value,
        xs = Imagen.I02.value,
        sm = Imagen.I02.value,
        md = Imagen.I03.value,
        lg = Imagen.I03.value,
        xl = Imagen.I03.value,
    ),
    height = 'auto',
    display=["flex", "flex", "flex", "flex", "flex"],
)

# Escala para las imagenes del icono con enlace de página
escala_icono = dict(

    width = rx.breakpoints(
        initial = Imagen.I01.value,
        xs = Imagen.I02.value,
        sm = Imagen.I02.value,
        md = Imagen.I03.value,
        lg = Imagen.I03.value,
        xl = Imagen.I03.value,
    ),
    height = 'auto',
    display=["flex", "flex", "flex", "flex", "flex"],
)


# Escala para la imagen de la vista inicio
escala_inicio = dict(

    width = rx.breakpoints(
        initial = Imagen.I13.value,
        xs = Imagen.I13.value,
        sm = Imagen.I15.value,
        md = Imagen.I15.value,
        lg = Imagen.I16.value,
        xl = Imagen.I17.value,
    ),
    height = 'auto',
    display=["flex", "flex", "flex", "flex", "flex"],  
)

# Escala para la imagen de la vista servicios
escala_servicio = dict(
    width = rx.breakpoints(
        initial = Imagen.I05.value,
        xs = Imagen.I05.value,
        sm = Imagen.I06.value,
        md = Imagen.IS3.value,
        lg = Imagen.IS2.value,
        xl = Imagen.IS1.value,
    ),
    height = 'auto',
    display=["flex", "flex", "flex", "flex", "flex"],  
)

# Escala para la imagen de la vista partidos
escala_partido = dict(

    width = rx.breakpoints(
        initial = Imagen.I08.value,
        xs = Imagen.I09.value,
        sm = Imagen.I10.value,
        md = Imagen.I11.value,
        lg = Imagen.I12.value,
        xl = Imagen.I13.value,
    ),
    height = 'auto',
    display=["flex", "flex", "flex", "flex", "flex"],   
)

# Escala para la imagen de la vista Honorarios
escala_honorarios = dict(

    width = rx.breakpoints(
        initial = Imagen.I04.value,
        xs = Imagen.I05.value,
        sm = Imagen.I06.value,
        md = Imagen.I07.value,
        lg = Imagen.I08.value,
        xl = Imagen.I09.value,
    ),
    height = 'auto',
    display=["flex", "flex", "flex", "flex", "flex"],   
)

# Escala para la imagen de la vista https
escala_https = dict(

    width = rx.breakpoints(
        initial = Imagen.I02.value,
        xs = Imagen.I03.value,
        sm = Imagen.I04.value,
        md = Imagen.I05.value,
        lg = Imagen.I06.value,
        xl = Imagen.I08.value,
    ),
    height = 'auto',
    display=["flex", "flex", "flex", "flex", "flex"],    
)

# Escala para las imagenes para el pie de la página web
escala_pie = dict(

    width = rx.breakpoints(
        initial = Imagen.I01.value,
        xs = Imagen.I02.value,
        sm = Imagen.I02.value,
        md = Imagen.I03.value,
        lg = Imagen.I03.value,
        xl = Imagen.I03.value,
    ),
    height = 'auto',
    display=["flex", "flex", "flex", "flex", "flex"],    
)

# Escala para las imagenes para el área privada
escala_privada = dict(

    width = rx.breakpoints(
        initial = Imagen.I01.value,
        xs = Imagen.I02.value,
        sm = Imagen.I03.value,
        md = Imagen.I04.value,
        lg = Imagen.I05.value,
        xl = Imagen.I06.value,
    ),
    height = 'auto',
    display=["flex", "flex", "flex", "flex", "flex"],   
)