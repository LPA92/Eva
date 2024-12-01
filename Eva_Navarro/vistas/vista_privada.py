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
from Eva_Navarro.componentes.entrada import form_valida
from Eva_Navarro.componentes.entrada import form_oculta
# Importamos el boton
from Eva_Navarro.componentes.entrada import boton
# Importamos el mensaje de error
from Eva_Navarro.componentes.entrada import invalido




def vistaprivada() -> rx.Component:
    return rx.hstack(
        # hstack = Posiciona los componentes de forma horizontal
        rx.flex(
            # Pone la imagen Alto.svg
            rx.image(
                src = '/svg/Alto.svg',
                # Si no carga la imagen nos sale el texto definido en alt
                alt = 'Imagen de Area Privada',
                style = escala.escala_privada,
                # Margen derecho de la imagen
                margin_right = Sep.A01.value,
            ),
            rx.flex(
                rx.center(
                    rx.hstack(
                        rx.vstack(
                            rx.image(
                                src='/svg/Pie_Logo.svg',
                                alt='Imagen del logo de procuradores',
                                style = escala.escala_imagen,
                            ),
                            titulo('Inicia sesión en tu cuenta'),
                            reg( '¿Eres nuevo aquí?','Únete'),
                            align = 'center',
                            justify = 'center'

                        ),                           
                        rx.form.root(
                            rx.flex(
                                rx.vstack(
                                    form_valida('Correo electrónico','Ingrese su correo electrónico', estado.LoginEstado.set_correo, estado.LoginEstado.correo, estado.LoginEstado.correo_vacio, 'Este campo no puede estar vacio', estado.LoginEstado.correo_invalido,'Introduzca un correo válido'),
                                            
                                    form_oculta('Contraseña','Ingrese su contraseña',  estado.LoginEstado.contrasenya, estado.LoginEstado.set_contrasenya,'password', 'Este campo no puede estar vacio'),
                                            
                                    boton('Inicie sesión'),
    #                                spacing = '2',
                                ),
                            ),
                            invalido(),
                        ),
#                        flex_grow="1",
                        text_align = 'center',
                        align_items= 'center'
                    )


#                    direction='column',
                    # Alineación vertical dentro del vstack
#                    align = 'center',
                    # Alineación horizontal dentro del vstack
#                    justify = 'center',

                        # Para conectar con el backend
    #                    on_submit = estado.LoginEstado.loginService,
    #                    reset_on_submit = True,
    #                    width='80%',
                        
            ),
        ),
    ),
    style = Seccion,
    margin_top = Ancho.I05.value,
    margin_bottom = Ancho.I00.value,

)


