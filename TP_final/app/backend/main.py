from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# El modelo se carga UNA sola vez, al arrancar el servidor
RUTA_MODELO = Path(__file__).resolve().parent.parent / "modelo" / "modelo.joblib"
modelo = joblib.load(RUTA_MODELO)

app = FastAPI(title="API de pingüinos")

# CORS: permite que el frontend (otro origen) llame a la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Pinguino(BaseModel):
    bill_length_mm: float = Field(gt=0)
    bill_depth_mm: float = Field(gt=0)
    flipper_length_mm: float = Field(gt=0)
    body_mass_g: float = Field(gt=0)


@app.get("/health")
def health():
    return {"estado": "ok"}


@app.post("/predecir")
def predecir(datos: Pinguino):
    fila = pd.DataFrame([datos.model_dump()])
    especie = modelo.predict(fila)[0]
    probas = modelo.predict_proba(fila)[0]
    return {
        "especie": str(especie),
        "probabilidades": {
            str(clase): round(float(p), 3)
            for clase, p in zip(modelo.classes_, probas)
        },
    }