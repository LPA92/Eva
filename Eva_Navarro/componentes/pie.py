# Tipo de borde,    5px,10px,4px,9px→(arriba, dcha, bajo izqda )
# solido = solid,	5px, 20px → (arriba y abajo, en los lados )
# puenteado = dotted,
# doble = double

# Importamos reflex
import reflex as rx 
# Importamos los enlaces
import Eva_Navarro.constantes as ctes

# Importamos los tamaños
from Eva_Navarro.estilos.generico import Tamanyo as Tamanyo
# Importamos los colores generales
from Eva_Navarro.estilos.colores import Color as Color
# Importamos los colores de los textos
from Eva_Navarro.estilos.colores import TextoColor as TextoColor
# Importamos la plantilla de imagenes del pie
from Eva_Navarro.componentes.imagenes import img_pie as imagen
# Importamos la plantilla de imagenes del nav
from Eva_Navarro.componentes.imagenes import nav as nav
# Importamos la plantilla de imagenes
from Eva_Navarro.componentes.imagenes import logo as logo



# Definimos el componente pie (pie de página)
def pie() -> rx.Component:
        # rx.center -> centramos todo lo que contiene
    return rx.center(
        rx.flex(           
            logo(
                '/svg/Pie_Logo.svg',
                'Logo Procurador',
                'Procuradora de los Tribunales',
                'Eva Maria Navarro Naranjo',        
            ),
            imagen(
                '/svg/Pie_Movil.svg',
                'Movil',
                ctes.MOVIL,
            ),
            nav(
                '/svg/Pie_Linkedin.svg',
                'Linkedin',
                'Linkedin',
                ctes.LINKEDIN_URL,
            ),
            nav(
                '/svg/Pie_Info.svg',
                'Conctacto',
                'Contacto',
                f'mailto:{ctes.EMAIL}',
            ),
            spacing='5',
        ),

    ),            
        
        
        
