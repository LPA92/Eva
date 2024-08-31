                    ####  meta  ####
# charset = Especifica la codificación de caracteres que se usa en la página
# name = Obligatorio sirve para identificar el tipo de metadato
# content = Obligatorio especifica el valor del metadato
# title = Especifica el título de la página web, máximo 50 caracteres
# description = Resumen de la página web, máximo 155 caracteres
# robots = Indica los motores de búqueda que hacer con la página
    # index = Indexar la página
    # noindex = No indexar la página
    # follow = Seguir los enlaces en la página
    # nofollow = No seguir los enlaces en la página
# Viewport = Controla como se muestra la página en los dispositivos móviles

# Para facebook -> van con property -> property = "og:title" , content = "Que es el marketing" 
# og:title = Indica el proposito del sitio
# og:description = Es la descripción del sitio
# og:type = Indica de qué trata el contenido en concreto
# og:url = Muestra la url de la página web
# og:image = Señala cuando una url contiene una imagen
# og:video = Para los videos
# Para Tuitwer -> van con name

# Importamos reflex
import reflex as rx

# Definimos el idioma por defecto
def lenguaje() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

# Meta común a todas las páginas. el _ significa modo privado
_meta = [
    {'chart_set': 'UTF-8'},
    {'name': 'author', 'content': 'Iñaki Loyola Bustamante'},
    {'name': 'description', 'content': 'Página web de la Procuradora Eva Maria Navarro Naranjo'},
    {'name': 'robots', 'content': 'index, follow'},
    {'name': 'viewport', 'content': '"width=device-width, initial-scale=1.0"'},
    ]

# Meta especifico para la página index, 
# facebook → og:
# twitter -> twitter:
indice_meta = [
    {'name': 'og:title', 'content': 'EVNN'},
    {'name': 'og:description','content': 'Hola, mi nombre es Eva Maria Navarro Naranjo.'},
    {'name': 'og:type', 'content': 'website'},
    ]
# Para incluir el meta común dentro de la página index
indice_meta.extend(_meta)
