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

titulo_inicio = 'Pagina de Inicio'
descripcion_inicio = 'Hola, soy Procuradora y mi nombre es Eva Maria Navarro Naranjo.'
imagen_inicio = '/svg/Logo_Procurador.svg'

# Meta común para la página inicio, 
# facebook → og:
# twitter -> twitter:
inicio_meta = [
    {'name': 'og:title', 'content': titulo_inicio},
    {'name': 'og:description','content': descripcion_inicio },
    {'name': 'og:type', 'content': 'website'},
    ]

# Para incluir el meta común dentro de la página index
inicio_meta.extend(_meta)

# Partidos Judiciales

titulo_partido = 'Pagina de Partidos Judiciales'
descripcion_partido = 'Esta es la distribución de los partidos judiciales en Gran Canaria.' 
imagen_partido = '/svg/NV_Partidos.svg'

# Meta común para la página de partidos judiciales, 
# facebook → og:
# twitter -> twitter:
partido_meta = [
    {'name': 'og:title', 'content': titulo_partido},
    {'name': 'og:description','content': descripcion_partido},
    {'name': 'og:type', 'content': 'website'},
    ]

# Para incluir el meta común dentro de la página de partidos judiciales
partido_meta.extend(_meta)


# Servicios

titulo_servicios = 'Pagina de Servicios de los Procuradores'
descripcion_servicios = 'Estos son los servicios que presta una Procuradora en el ámbito judicial.' 
imagen_servcio = '/svg/NV_Servicios.svg'

# Meta común para la página de Servicios de los Procuradores, 
# facebook → og:
# twitter -> twitter:
servicio_meta = [
    {'name': 'og:title', 'content': titulo_servicios},
    {'name': 'og:description','content': descripcion_servicios },
    {'name': 'og:type', 'content': 'website'},
    ]

# Para incluir el meta común dentro de la página de servicios de los procuradores
servicio_meta.extend(_meta)

# Honorarios de los Procuradores

titulo_honorarios = 'Pagina de Honorarios de los Procuradores'
descripcion_honorarios = 'Estos son los honorarios de los Procuradores en el ámbito judicial.'
imagen_honorarios = '/svg/NV_Honorarios.svg'

# Meta común para la página de honorarios, 
# facebook → og:
# twitter -> twitter:
honorarios_meta = [
    {'name': 'og:title', 'content': titulo_honorarios},
    {'name': 'og:description','content': descripcion_honorarios},
    {'name': 'og:type', 'content': 'website'},
    ]
# Para incluir el meta común dentro de la página de honorarios
honorarios_meta.extend(_meta)

# Web Externas

titulo_externo = 'Pagina de Webs Externas'
descripcion_externo = 'Webs externas que pueden ser de interés en el ámbito judicial.' 
imagen_externo = '/svg/NV_Externas.svg'

# Meta común para las Web's externas
# facebook → og:
# twitter -> twitter:
externo_meta = [
    {'name': 'og:title', 'content': titulo_externo},
    {'name': 'og:description','content': descripcion_externo },
    {'name': 'og:type', 'content': 'website'},
    ]
# Para incluir el meta común dentro de las Webs externas
externo_meta.extend(_meta)

# Area Privada

titulo_privado = 'Pagina de Area Privada'
descripcion_privado = 'Area Privada de la Procuradora Eva Navarro.'
imagen_privado = '/svg/UE.svg'

# Meta común para el área privada
# facebook → og:
# twitter -> twitter:
privado_meta = [
    {'name': 'og:title', 'content': titulo_privado},
    {'name': 'og:description','content': descripcion_privado},
    {'name': 'og:type', 'content': 'website'},
    ]
# Para incluir el meta común dentro del área privada
privado_meta.extend(_meta)
