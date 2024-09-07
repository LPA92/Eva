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
    # Verde para encabezado de tabla
    TABLA = '#006400'
    # Rojo Oscuro #D20103 -> Más oscuro #930405 -> Naranja #f54021 -> Amarillo #ffff9c
    CELDA = '#ffff9c'
    # Color azul
    BORDE = '#32a1ce'
    
    

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
    # Tabla color negro
    CELDA = '#000000'