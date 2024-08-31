# Tipo de borde,    5px,10px,4px,9px→(arriba, dcha, bajo izqda )
# solido = solid,	5px, 20px → (arriba y abajo, en los lados )
# puenteado = dotted,
# doble = double

# Importamos reflex
import reflex as rx 
# Importamos los enlaces
import Eva_Navarro.constantes as ctes
# Importamos los estilos
import Eva_Navarro.estilos.generico as generico
# Importamos los tamaños
# Importamos el componente link imagen pie de página
import Eva_Navarro.componentes.link_PIE as link_Pie

from Eva_Navarro.estilos.generico import Tamanyo as Tamanyo
# Importamos los colores generales
from Eva_Navarro.estilos.colores import Color as Color
# Importamos los colores de los textos
from Eva_Navarro.estilos.colores import TextoColor as TextoColor
# Importamos la plantilla de imagenes
from Eva_Navarro.componentes.imagenes import img_pie as imagen



# Definimos el componente pie (pie de página)
def pie() -> rx.Component:
    # Colocamos los componentes de forma horizontal
    return rx.hstack(
        rx.hstack(
            imagen(
                src="/svg/Pie_Logo.svg",
                alt='Logotipo de Procurador',            
            ),
            # Texto que nos sale en la página web   
            rx.text(
                ctes.PROCURADOR,
                # Establecemos el estilo del texto
                style = generico.pie_comun,
            ),
        ),
        rx.hstack(
            imagen(
                src = '/svg/Pie_Movil.svg',
                alt = 'Móvil',
            ),        
            # Texto que nos sale en la página web   
            rx.text(
                ctes.MOVIL,
                # Establecemos el estilo del texto
                style = generico.pie_comun,
            ),            
        ),
        link_Pie(
            # titulo
            'Contacto',
            # Ruta donde esta la imagen
            '/svg/Pie_Movil',
            # correo electrónico para enviar el cliente
            f'mailto:{ctes.EMAIL}',
        ),
        rx.hstack(
            imagen(
                src = '/svg/Pie_Linkedin.svg',
                alt = 'Linkedin',
            ),
            # Texto que nos sale en la página web   
            rx.text(
                ctes.LINKEDIN_URL,
                # Establecemos el estilo del texto
                style = generico.pie_comun,
            ),          
        ),   
        # Coloca en el centro los diferentes componentes
        align='center',
        # No deja sepación entre los diferentes componentes
        spacing='0',

        # Especificamos el margen inferior
        margin_bottom = Tamanyo.BG.value,
        # padding_bottom = Tamanyo.BG.value,
        color = TextoColor.PIE.value,
        # Ponemos un relleno a la derecha del componente
        padding_x = Tamanyo.XS.value,
        # Margen superior
        margin_top = Tamanyo.XXL.value,
    )