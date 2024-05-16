from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/incidencia")
async def get_incidencia():
    incidencia_mermelada = {
        "id": 1,
        "titulo": "Incidencia sobre mermelada",
        "descripcion": "Se ha detectado un problema con la calidad de la mermelada en el lote 12345.",
        "estado": "Pendiente",
        "fecha": "2024-05-16"
    }
    return incidencia_mermelada
