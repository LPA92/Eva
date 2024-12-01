# Importamos reflex
import reflex as rx
# Importamos los estados
import Eva_Navarro.estilos.estado as estado

# Importamos los espacios
from Eva_Navarro.estilos.valores import Separacion as Espacio
from Eva_Navarro.estilos.valores import Imagen as Imagen
from Eva_Navarro.estilos.valores import Anchos as Ancho
# Importamos los colores
from Eva_Navarro.estilos.colores import Color as Color
from Eva_Navarro.estilos.colores import TextoColor as Texto

CV = 'Este campo no puede estar vacío'


def form_valida (label:str, placeholder:str, on_change_function, nombre:str, vacio, msvacio:str, show, mserror:str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(
                label,
                color=Color.CELDA.value,
                font_size = Imagen.I02.value,
            ),
            rx.form.control(
                rx.input(
                    placeholder=placeholder,
                    on_change=on_change_function,
                    name=nombre,
                    required = True,
                ),
                as_child=True,
            ),
            rx.cond(
                vacio,
                rx.form.message(
                    msvacio,
                    color=Texto.CABEZA.value,
                    font_size = Imagen.I01.value,
                ),
            ),
            rx.form.message(
                mserror,
                name=nombre,
                match='valueMissing',
                force_match=show,
                color=Texto.CABEZA.value,
                font_size = Imagen.I01.value,
            ),
            direction='column',
            spacing='2',
            align='stretch',
        ),
        name=nombre,
        width = Ancho.A06.value,        
    ),
    
def form_oculta (label:str, placeholder:str, nombre:str,  on_change_function, tipo:str, mserror:str ) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(
                label,
                color=Color.CELDA.value,
                font_size = Imagen.I02.value,
            ),
            rx.form.control(
                rx.input(
                    placeholder=placeholder,
                    on_change=on_change_function,
                    name=nombre,                    
                    type=tipo,
                    required = True,
                ),
                as_child=True,
            ),
            rx.form.message(
                mserror,
                match="valueMissing",
                font_size = Imagen.I01.value,
                color = Color.LOGIN.value
            ),
            direction='column',
            spacing='2',
            align='stretch',
        ),
        name=nombre,
        width = Ancho.A06.value,
    ),
        
    
# Botón de envio del formualario de entrada
def boton (nombre:str) -> rx.Component:
    return rx.form.submit(
        rx.cond(
            estado.LoginEstado.loader,
            rx.center(
                rx.spinner(
                    color = Color.LOGIN.value,
                    size = '3'
                ),
                rx.button(
                    nombre,
                    font_size = Imagen.I02.value,
                    disabled=estado.LoginEstado.validacion,
                    width = Ancho.A16.value,
                ),
                as_child=True                
            ),

        ),
#        as_child = True,             
#        direction = 'column',
#        spacing = Espacio.DF.value,
#        width = Imagen.I09.value,

        # Alineación vertical
#        align = 'center',
        # Alineación horizontal
#        justify = 'center',
    ),
    
def invalido()-> rx.Component:
    return rx.cond(
        estado.LoginEstado.error,
        rx.callout(
            'Credenciales incorrectas',
            icon='triangle_alert',
            color_scheme = 'red',
            role='alert',
            style={'margin_top':'10px'}
        ),        
    )