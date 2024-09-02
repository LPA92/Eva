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

# Página de Inicio

imagen_inicio = '/svg/Logo_Procurador.svg'

# Meta común para la página inicio, 
# facebook → og:
# twitter -> twitter:
inicio_meta = [
    {'name': 'og:title', 'content': 'Pagina de Inicio'},
    {'name': 'og:description','content': 'Hola, soy Procuradora y mi nombre es Eva Maria Navarro Naranjo.'},
    {'name': 'og:type', 'content': 'website'},
    ]

# Para incluir el meta común dentro de la página index
inicio_meta.extend(_meta)

# Partidos Judiciales

imagen_partido = '/svg/NV_Partidos.svg'

# Meta común para la página de partidos judiciales, 
# facebook → og:
# twitter -> twitter:
partido_meta = [
    {'name': 'og:title', 'content': 'Pagina de Partidos Judiciales'},
    {'name': 'og:description','content': 'Esta es la distribución de los partidos judiciales en Gran Canaria.'},
    {'name': 'og:type', 'content': 'website'},
    ]

# Para incluir el meta común dentro de la página de partidos judiciales
partido_meta.extend(_meta)


# Servicios

imagen_servcio = '/svg/NV_Servicios.svg'

# Meta común para la página de Servicios de los Procuradores, 
# facebook → og:
# twitter -> twitter:
servicio_meta = [
    {'name': 'og:title', 'content': 'Servicios de los Procuradores'},
    {'name': 'og:description','content': 'Estos son los servicios que presta una Procuradora en el ámbito judicial.'},
    {'name': 'og:type', 'content': 'website'},
    ]

# Para incluir el meta común dentro de la página de servicios de los procuradores
servicio_meta.extend(_meta)

# Honorarios de los Procuradores

imagen_honorarios = '/svg/NV_Honorarios.svg'

# Meta común para la página de honorarios, 
# facebook → og:
# twitter -> twitter:
honorarios_meta = [
    {'name': 'og:title', 'content': 'Honorarios de los Procuradores'},
    {'name': 'og:description','content': 'Estos son los honorarios de los Procuradores en el ámbito judicial.'},
    {'name': 'og:type', 'content': 'website'},
    ]
# Para incluir el meta común dentro de la página de honorarios
honorarios_meta.extend(_meta)

# Web Externas

imagen_externo = '/svg/NV_Externas.svg'

# Meta común para las Web's externas
# facebook → og:
# twitter -> twitter:
externo_meta = [
    {'name': 'og:title', 'content': 'Webs Externas'},
    {'name': 'og:description','content': 'Webs externas que pueden ser de interés en el ámbito judicial.'},
    {'name': 'og:type', 'content': 'website'},
    ]
# Para incluir el meta común dentro de las Webs externas
externo_meta.extend(_meta)

# Area Privada

imagen_privado = '/svg/UE.svg'

# Meta común para el área privada
# facebook → og:
# twitter -> twitter:
privado_meta = [
    {'name': 'og:title', 'content': 'Area Privada'},
    {'name': 'og:description','content': 'Area Privada de la Procuradora Eva Navarro.'},
    {'name': 'og:type', 'content': 'website'},
    ]
# Para incluir el meta común dentro del área privada
privado_meta.extend(_meta)
