# fuentes de google font -> https://fonts.google.com

# enum = define un conjunto de nombres descriptivos vinculados a valores constantes
from enum import Enum

# Clase de fuente a usar
class Fuente(Enum):
    DEFECTO = 'Poppins'	# Fuente por defecto
    TITULO = ' Roboto'	# Fuente para el título
    LOGO = 'Comfortaa'	# Fuente para el logo

# Anchura de la fuente
class Trazo(Enum):
    NORMAL = '300'		# Letra normal
    NEGRITA = '500'		# Letra negrita
