import reflex as rx

config = rx.Config(
    app_name="Eva_Navarro",
    # Lista de orígenes que pueden conectarse a la API de backend.
    cors_allowed_origins=[
        "http://localhost:3000",
        
    ]    
)