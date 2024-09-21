# Importamos reflex
import reflex as rx
# Importamos la librería enum de python
from enum import Enum


# Valores para las imagenes
class Imagen(Enum):
    I18 = '70em',
    I17 = '65em',
    I16 = '60em'
    I15 = '55em'
    I14 = '50em',
    I13 = '45em',
    I12 = '40em',
    I11 = '35em',
    I10 = '30em',
    I09 = '25em',
    I08 = '20em',
    I07 = '15em',
    I06 = '10em',
    I05 = '5em',
    I04 = '4em',
    I03 = '3em',
    I02 = '2em',
    I01 = '1em',
    I00 = '0px',
    IS1 = '18em',
    IS2 = '13em',
    IS3 = '8em',
    
# Valores para los textos
class Texto(Enum):
    T16 = '4.00em',
    T15 = '3.75em',
    T14 = '3.50em',
    T13 = '3.25em',
    T12 = '3.00em',
    T11 = '2.75em',
    T10 = '2.50em',
    T09 = '2.25em',
    T08 = '2.00em',
    T07 = '1.75em',
    T06 = '1.50em',
    T05 = '1.25em',
    T04 = '1.00em',
    T03 = '0.75em',
    T02 = '0.50em',
    T01 = '0.25em',
    T00 = '0.00em',
    
# Valores para la separaciones    
class Separacion(Enum):
    ZERO = '0',
    XXS = '1',
    XS = '2',
    S = '3',
    DF = '4',
    M = '5',
    L = '6',
    XL = '7',
    XXL = '8',
    VB = '9',
    
# Valores para las diferentes pantallas    
class Monitor(Enum):

    PQ = '60em',
    PM = '64em',
    PG = '80em',
    MG = '83em',
    EG = '120em',