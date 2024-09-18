# Bajarse iconos →
# https://fontawesome.com/ → Pestaña iconos
# en el buscador ponemos el icono a localizar → pulso en la flecha (dcha)
# Pulsamos en el icono → Pulsamos en descargar ( flecha hacía abajo )
# Para cambiar el color → Pulso en herramientas de estilo → última opción de color mitad amarillo mitad azul → aparece un cuadro para definir el color que queremos  ( en la parte inferior sale las casillas para establecer el color RGB manual.

# Para pasar imagenes a vectoriales ( svg ) usamos Inkscape
# Escogemos la imagen a pasar a vector -> Abrir -> Ok
# Pulso en la pestaña Vectorizar mapa de bits
# Pulso en la pestaña multicolor -> selecciono Colores 
# Selecciono la imagen pulsando sobre ella -> Fijamos el nº de pasadas hasta que quede bien la imagen -> Aplicar
# Archivo -> guardar como -> directorio a guardar

# Importamos reflex
import reflex as rx

# Importamos las escalas
import Eva_Navarro.estilos.escalas as escala
# Importamos los tamaños
from Eva_Navarro.estilos.texto import Texto as Texto



def link_icono(titulo: str, imagen: str, url: str ) -> rx.Component:
    # rx.link →  Para poder usar una url    
    return rx.link(
        # Para colocar el icono que corresponde a la url
            rx.image(
                src = imagen,
                # Texto que sale si no carga la imagen
                alt = titulo,
                style=escala.escala_icono,
                ),
        # Para poner el enlace donde ira la página web
        href=url,
        # Cada vez que pulsemos el botón se nos abrirá una nueva página
        is_external = True,
    )