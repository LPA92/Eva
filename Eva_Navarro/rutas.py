# Para usarlo como numeral
from enum import Enum

# Clase donde se definen los diferentes enlaces que nos llevan a las diferentes páginas web que contiene nuestra web.
class Rutas(Enum):
    INDEX = '/'
    PARTIDOS = '/partidos' 
    SERVICIOS = '/servicios'
    EXTERNOS = '/externos'
    HONORARIOS = '/honorarios'
    PRIVADO = '/privado'
    ACCESO = '/acceso'
