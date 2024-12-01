# Importamos reflex
import reflex as rx
# Importamos la libreria requests para realizar el post
import requests as rq
# Importamos las expresiones regulares
import re

import reflex.components.radix.primitives as rdxp

class LoginEstado(rx.State):
    # Definimos las variables a utilizar
    loader:bool = False
    correo:str
    contrasenya:str
    error = False
    response: dict = {}

    # Establecemos el método
    @rx.background
    async def loginService(self, data:dict):
        async with self:
            self.loader = True
            self.error = False
            # Guardamos la respuesta que nos de nuestro backend
            response = rq.post(
                'http://localhost:8080/auth/login',
                json = data,
                headers = { 'Content-Type':'application/json'}
            ),
            # Si la validación es correcta nos envia al acceso restringido y si no no te deja entrar
            if response.status_code == 200:
                self.response = response.json()
                self.loader = False
                return rx.redirect('/')
            else:
                self.loader = False
                self.error = True

    # Definimos los métodos para las validaciones

    # Correo electrónico invalido
    @rx.var
    def correo_invalido(self) -> bool:
        return not (
            re.match(
                r'[a-zA-Z0-9.%*+-]+@[a-z0-9.-]+\.[a-z]{2,3}$', self.correo
            )
        )

    # Correo electrónico vacio
    @rx.var
    def correo_vacio(self) -> bool:
        return not (self.correo.strip())

    # Contraseña vacia
    @rx.var
    def contrasenya_vacia(self) -> bool:
        return not (self.contrasenya.strip())
    
    @rx.var
    def contrasenya_invalida(self) -> bool:
        return not re.match(
            r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\[0-9])(?=.*[$@$!%*?&])[A-Za-z0-9\$@$!%*?&]{8,15}', self.contrasenya
        )

    # Para comprobar que todos los campos sean validos
    @rx.var
    def validacion(self) -> bool:
        return (
            self.correo_vacio
            or self.correo_invalido
            or self.contrasenya_vacia
            or self.contrasenya_invalida
        )
    