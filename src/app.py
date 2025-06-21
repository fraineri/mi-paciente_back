# app/main.py
from fastapi import FastAPI

# Crea una instancia de la aplicación FastAPI
app = FastAPI(
    title="Mi Microservicio",
    description="Un increíble microservicio creado con FastAPI.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    """
    Endpoint raíz que devuelve un saludo.
    """
    return {"message": "¡Hola, mundo desde FastAPI!"}


@app.get("/health")
def health_check():
    """
    Endpoint simple para verificar que el servicio está activo.
    """
    return {"status": "ok"}
