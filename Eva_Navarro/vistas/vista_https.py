# Importamos reflex
import reflex as rx
# Importamos las urls
import Eva_Navarro.constantes as ctes
# Importamos las escalas
import Eva_Navarro.estilos.escalas as escala
# Importamos la rejilla
import Eva_Navarro.estilos.rejilla as rejilla

# Importamos los tamaños
from Eva_Navarro.estilos.texto import Texto as Tamanyo
# Importamos los espacios
from Eva_Navarro.estilos.generico import Espacio as Espacio




# Añadimos los componentes que se van a ver en la página principal
def vistahttps() -> rx.Component:
        # rx.grid = Posiciona los componentes en forma de rejilla
    return rx.grid(
        # ponemos todas las imagenes
            # 1.- Colegio de Abogados de Las Palmas
            rx.link(
                rx.image(
                    src="/svg/Abogados.svg",
                    style = escala.escala_https,
                ),
                href = ctes.CALPA_URL,
            ),
            # 2.- Colegio de Procuradores de Las Palmas
            rx.link(
                rx.image(
                    src="/svg/CProcuradores.svg",
                    style = escala.escala_https,
                ),
                href = ctes.CPLPA_URL,
            ),
            # 3.- Colegio General de Abogados de España
            rx.link(
                rx.image(
                    src="/svg/CGAbogados.svg",
                    style = escala.escala_https,
                ),
                href = ctes.CGAE_URL,
            ),
            # 4.- Colegio General de Procuradores de España
            rx.link(
                rx.image(
                    src="/svg/CGProcuradores.svg",
                    style = escala.escala_https,
                ),
                href = ctes.CGPE_URL,
            ),
            # 5.- Ayuntamiento de Las Palmas de Gran Canaria             
            rx.link(
                rx.image(
                    src="/svg/Ayto_LPA.svg",
                    style = escala.escala_https,
                ),
                href = ctes.AYTO_LPGC_URL,
            ),
            # 6.- Cabildo de Gran Canaria
            rx.link(
                rx.image(
                    src="/svg/Cabildo.svg",
                    style = escala.escala_https,
                ),
                href = ctes.CABILDO_GC_URL,
            ),
            # 7.- Consejo General del Poder Judicial
            rx.link(
                rx.image(
                    src="/svg/CGPJ.svg",
                    style = escala.escala_https,
                ),
                href = ctes.CGPJ_URL,
            ),
            # 8.- Direcciones de Juzgados y Tribunales de España
            rx.link(
                rx.image(
                    src="/svg/Tfnos.svg",
                    style = escala.escala_https,
                ),
                href = ctes.DIRECCIONES_URL,
            ),            
            # 9.- Cálculo de Intereses Generales
            rx.link(
                rx.image(
                    src="/svg/Interes_Gral.svg",
                    style = escala.escala_https,
                ),
                href = ctes.CALCULO_INTERESES_URL,
            ),
            # 10.- Tabla de Intereses legales
            rx.link(
                rx.image(
                    src="/svg/Tabla_Int_Leg.svg",
                    style = escala.escala_https,
                ),
                href = ctes.INTERESES_JUDICIALES_URL,
            ),
            # 11.- Centro de Documentación Judicial           
            rx.link(
                rx.image(
                    src="/svg/CENDOJ.svg",
                    style = escala.escala_https,
                ),
                href = ctes.CENDOJ_URL,
            ),              
            # 12.- Cálculo de la letra del DNI
            rx.link(
                rx.image(
                    src="/svg/Letra_DNI.svg",
                    style = escala.escala_https,
                ),
                href = ctes.LETRA_DNI_URL,
            ),
            # 13.- IPC
            rx.link(
                rx.image(
                    src="/svg/IPC.svg",
                    style = escala.escala_https,
                ),
                href = ctes.IPC_URL,
            ),
            style=rejilla.rejilla,
        )
