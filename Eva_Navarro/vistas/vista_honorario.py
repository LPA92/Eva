# Importamos reflex
import reflex as rx
# Importamos los estilos
import Eva_Navarro.estilos.generico as comun

# Importamos la plantilla del texto 
from Eva_Navarro.componentes.titulo import honorarios as titulo


# Añadimos los componentes que se van a ver en la página principal
def vistahonorario() -> rx.Component:
    return rx.box(
        # hstack = Posiciona los componentes de forma horizontal
        # Creamos una caja flexible parea alterar sus dimnensiones y llenar el espacio disponible
        rx.flex(
            # vstack = Posiciona los componentes de forma vertical
            rx.vstack(
                titulo(
                    'Con fecha 4 de mayo de 2022 se publica el Real Decreto 307/2022, de 3 de mayo, por el que se modifica el Real Decreto 1373/2003, de 7 de noviembre, por el que se aprueba el arancel de derechos de los procuradores de los tribunales.',
                ),
                rx.spacer(),
                titulo(
                    'Real Decreto 307/2022, de 3 de mayo BOE nº 106 de 4 de mayo de 2022.',
                ),
                # rx.spacer(),
                rx.spacer(),
                titulo(
                    'Con fecha 1 de abril de 2010 se publica el Real Decreto-ley 5/2010, de 31 de marzo, por el que se amplía la vigencia de determinadas medidas económicas de carácter temporal, quedando modificado el Arancel de derechos de los procuradores de los Tribunales.',
                ),
                rx.spacer(),
                # rx.spacer(),
                titulo(
                    'Real Decreto-ley 5/2010, de 31 de marzo BOE nº 79 de 1 de abril de 2010.',
                ),
                rx.spacer(),
                # rx.spacer(),
                titulo(
                    'Con fecha 28 de Enero de 2006 se publica la modificación al Arancel de derechos de los Procuradores de los Tribunales, por la que se establece una regulación unitaria de los derechos a percibir por los procuradores de los tribunales en los juicios concursales.',
                ),
                # rx.spacer(),
                rx.spacer(),
                titulo(
                    'R.D. 1/2006, de 13 de Enero B.O.E. nº 24 de 28 de Enero de 2006. Mediante el Real Decreto 1373/2003, de 7 de noviembre se aprobó el vigente arancel de derechos de los procuradores de los tribunales, en cuyo capítulo I, sección 3.ª, se regulan los derechos a percibir en los juicios concursales,y concretamente en la suspensión de pagos, quitas y esperas y en las quiebras y concursos de acreedores.',
                ),
                rx.spacer(),
                # rx.spacer(),
                titulo(
                    'Con fecha 20 de Noviembre de 2003 se publica el Arancel de derechos de los Procuradores de los Tribunales.',
                ),
                rx.spacer(),
                # rx.spacer(),
                titulo(
                    'R.D. 1373/2003 de 7 de Noviembre BOE nº 278 de 20 de Noviembre de 2003.',
                ),
            ),
        ),
        style = comun.Flexible,
        width ='100%',
    ),