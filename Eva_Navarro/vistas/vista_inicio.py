# Importamos reflex
import reflex as rx
# Importamos la libreria datetime de python
import datetime
# Importamos los estilos
import Eva_Navarro.estilos.generico as comun

# Importamos los tamaños
from Eva_Navarro.estilos.texto import Texto as Tamanyo
# Importamos la plantilla de información profesional
from Eva_Navarro.componentes.info_profesional import texto_inicio, texto_parrafo

# Importamos las escalas
import Eva_Navarro.estilos.escalas as escala


# Añadimos los componentes que se van a ver en la página principal
def vistainicio() -> rx.Component:
    
        # vstack = Posiciona los componentes de forma horizontal
    return rx.hstack(
        # hstack = Posiciona los componentes de forma horizontal
        rx.flex(
            # Pone la imagen Justicia.svg
            rx.image(
                src = '/svg/Justicia.svg',
                alt = 'Imagen de Justicia',
                style = escala.escala_inicio,
            ),
            rx.box(     
                # Creamos una caja flexible parea alterar sus dimnensiones y llenar el espacio disponible
                rx.flex(
                    rx.vstack(
                        rx.hstack(
                            texto_inicio(
                                'Eva Maria Navarro Narnajo',
                                f'licenciada en derecho, disponiendo de una experiencia de {experiencia()}  años, como Procuradora de los Tribunales de España.',
                            ),
                        ),

                        # Deja un espacio desplazando todo hacia la derecha                    
                        rx.spacer(),
                        texto_parrafo(
                            'Su labor profesional se caracteriza por ofrecer una ágil y rápida respuesta dentro de los partidos judiciales de la isla de Gran Canaria, ',
                                            
                            'disponiendo de una amplia experiencia, ',
                                    
                            'acompañada de su seriedad, responsabilidad u trato inmejorable con los clientes y demás profesionales de la justicia.',
                        ),
                        # Deja un espacio desplazando todo hacia la derecha                    
                        rx.spacer(),
                        texto_parrafo(
                            'Hemos de destacar que en todos los procedimientos judiciales, tanto en los que he trabajado como los que actualmente estoy tabajando, tanto el cliente como los letrados estan al corriente de los asuntos que tengo asignados, ',

                            'haciendo uso de las nuevas tecnologías',
                                            
                            'para el desarrollo de mi profesión',
                        ),
                        # Deja un espacio desplazando todo hacia la derecha                      
                        rx.spacer(),
                        texto_parrafo(
                            'Entre los servicios que presto se encuentran, ',
                                            
                            'la Representación Procesal, tanto de las personas jurídicas como de las físicas, ',
                                            
                            'para cualquier procedimiento judicial radicado en la isla de Gran Canaria',
                        ),    
                    ),
                    style = comun.Flexible,                    
                ),
                # Para separar la imagen del texto
                margin_left = Tamanyo.T08.value
            ),
            align_items = 'center'
        ),            
    ),  


# Para calcular los años de experiencia desde que empece a trabajar    
def experiencia() -> int:
    return datetime.date.today().year - 2001    