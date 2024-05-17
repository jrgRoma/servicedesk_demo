from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/incidencia/{id}")
async def get_incidencia(id: int):
    incidencias = {
        1: {
            "id": 1,
            "titulo": "Incidencia sobre mermelada",
            "descripcion": "Se ha detectado un problema con la calidad de la mermelada en el lote 12345.",
            "estado": "Pendiente",
            "fecha": "2024-05-16"
        },
        2: {
            "id": 2,
            "titulo": "Incidencia sobre mermelada con moho",
            "descripcion": "Un cliente ha reportado que encontró moho en un frasco de mermelada.",
            "estado": "Cerrado",
            "fecha": "2024-05-17"
        },
        3: {
            "id": 3,
            "titulo": "Incidencia sobre tapa de mermelada",
            "descripcion": "Se ha informado que algunas tapas de los frascos de mermelada no cierran correctamente.",
            "estado": "Resuelto",
            "fecha": "2024-05-15"
        },
        4: {
            "id": 4,
            "titulo": "Incidencia sobre conexión a internet",
            "descripcion": "Se ha reportado una interrupción en el servicio de internet en la oficina principal.",
            "estado": "Pendiente",
            "fecha": "2024-05-16"
        }
    }

    return incidencias.get(id, {"error": "Incidencia no encontrada"})
