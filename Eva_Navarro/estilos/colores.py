# enum = define un conjunto de nombres descriptivos vinculados a valores constantes
from enum import Enum

# Colores principales
class Color(Enum):
    # Azul
    PRIMARIO ='#14A1F0'
    # Azul oscuro
    SECUNDARIO = '#087ec4'
    # Azul muy muy oscuro
    FONDO = '#0C151D'
    # Azul oscuro tirando a grisáceo
    CONTENIDO = '#171F26'

# Colores para los textos
class TextoColor(Enum):
    # Cabecera - Título - Muy blanco
    CABEZA = '#F1F2F4'
    # Cuerpo - Más grisáceo
    CUERPO = '#C3C7CB'
    # Pie - Gris más oscuro
    PIE = '#A3ABB2'
    # Navegación - Amarillo
    NAV = '#D8FF00'