# Importamos reflex
import reflex as rx
# Importamos la libreria requests para realizar el post
import requests as rq
# Importamos las expresiones regulares
import re
# Importamos el estado
import Eva_Navarro.estilos.estado as estado
# Importamos las escalas
import Eva_Navarro.estilos.escalas as escala

import reflex.components.radix.primitives as rdxp



# Importamos los colores
from Eva_Navarro.estilos.colores import Color as Color
from Eva_Navarro.estilos.colores import TextoColor as Texto
from Eva_Navarro.estilos.valores import Imagen as Imagen
# Importamos los tamaños
from Eva_Navarro.estilos.valores import Anchos as Ancho
from Eva_Navarro.estilos.generico import Seccion as Seccion
from Eva_Navarro.estilos.generico import Centrado as Centra

# Importamos los espacios
from Eva_Navarro.estilos.valores import Separacion as Espacio
from Eva_Navarro.estilos.valores import Imagen as Ancho
from Eva_Navarro.estilos.valores import Anchos as Sep


# Importamos la plantilla de información profesional
from Eva_Navarro.componentes.titulo import titulo as titulo
from Eva_Navarro.componentes.titulo import registro as reg
# Importamos la entrada de correo electrónico
# from Eva_Navarro.componentes.entrada import form_tipo
# Importamos la entrada de contraseña 
# from Eva_Navarro.componentes.entrada import form_regla
from Eva_Navarro.componentes.entrada import form_valida
from Eva_Navarro.componentes.entrada import form_oculta
# Importamos el boton
from Eva_Navarro.componentes.entrada import boton
# Importamos el mensaje de error
from Eva_Navarro.componentes.entrada import invalido

class EstadoLogin(rx.State):
    loader: bool = False
    correo: str
    contrasenya: str
    error = False
    response: dict = {}
    
    @rx.var
    def invalid_email(self) -> bool:
        return not re.match(
            r"[^@]+@[^@]+\.[^@]+", self.correo
        )
        
    rx.var
    def correo_vacio(self) -> bool:
        return not self.correo.strip()
    
    rx.var
    def validacion(self) -> bool:
        return (
            self.correo_vacio
#            or self.invalid_email
        )
        
def vistaacceso() -> rx.Component:
    return rx.section(
        rx.flex(
            rx.image(
                src='/svg/Pie_Logo.svg',
                alt='Imagen del logo de procuradores',
                style = escala.escala_imagen,
            ),
            rx.heading('Inicio de sesión'),
            rx.form.root(
                rx.flex(
                    rx.form.field(
                        rx.flex(
                            rx.form.label('Ingrese su correo electrónico'),
                            rx.form.control(
                                rx.input(
                                    placeholder='correo electrónico',
                                    type='text',
                                    pattern = r'[a-z]{4}'
                                ),
                                as_child = True,
                            ),
                            rx.cond(
                                EstadoLogin.correo_vacio,
                                rx.form.message(
                                    "la contraseña no puede estar vacia",
                                    color="yellow",
                                ),
                            ),                            
                            rx.form.message(
                                'Por favor, ingrese un correo válido',
                                
                                match = 'patternMismatch',
                                
                                color = 'yellow',
                                font_size = Imagen.I01.value
                            ),
                            direction = 'column',
                            spacing = '2',
                            align = 'stretch'
                        ),
                        name = EstadoLogin.correo,
                        width = '30vw'                        
                    ),
                    rx.form.submit(
                        rx.cond(
                            EstadoLogin.loader,
                            rx.spinner(
                                color='yellow',
                                size = '3'
                            ),
                            rx.button(
                                'Iniciar Sesión',
                                disabled = EstadoLogin.invalid_email,
                                width = '30vw',
                            )
                        ),
                        as_child = True
                    ),
                    direction = 'column',
                    justify = 'center',
                    align = 'center',
                    spacing = '2'
                ),
                rx.cond(
                    EstadoLogin.error,
                    rx.callout(
                        'Credenciales incorrectas',
                        icon = 'triangle_alert',
                        color_scheme = 'red',
                        role = 'alert',
                        style = {'margin_top': '1em'}
                    )
                ),
                reset_on_submit = True,
                width = '80%'
            ),
            width = '100%',
            direction = 'column',
            align = 'center',
            justify = 'center'
        ),
        style = Seccion,
        justify = ' center',
        width = ' 100%'
    )
        