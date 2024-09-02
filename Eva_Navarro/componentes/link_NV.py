# Importamos reflex
import reflex as rx
# Importamos los estilos
import Eva_Navarro.estilos.generico as estilo

# Importamos los tamaños
from Eva_Navarro.estilos.generico import Tamanyo as Tamanyo


# Definimos el componente botón para usarlo en las diferentes vistas
# Hay que poner dos textos,( title y body ) una url y una imagen
# Ponemos por defecto que la url se habrá en una pestaña diferente


def link_NV(titulo:str, imagen: str, url: str, is_external=True) -> rx.Component:
    return rx.link(
        # Para poner el texto dentro del botón y ocupe todo el ancho del link
        rx.button(
            # Para que coloque horizontalmente dentro del botón
            rx.hstack(
                # Para que salga la imagen dentro del botón
                rx.image(
                    src = imagen,
                    # Texto que sale si no carga la imagen
                    alt = titulo,
                    style=estilo.estilo_imagen_NAV,
                ),
                # Tamaño del texto definido en boton_titulo_estilo
                rx.text(titulo, style=estilo.boton_titulo_estilo),
                align_items='start',
                # Ponemos un relleno en el eje Y ( vertical ) en el componente botón
                padding_y = Tamanyo.XS.value,
                # Ponemos un relleno a la derecha del componente botón
                padding_right = Tamanyo.XS.value,
                # Para que todos los botones ocupen el 100%              
                width = '100%',
            ),            
        ),
        # Para poner el enlace donde ira la página web
        href=url,
        # Opción para que no se abra en una página nueva.
        is_external = is_external,
        # Para que todos los botones ocupen el 100%
        width = '100%',    
    )
