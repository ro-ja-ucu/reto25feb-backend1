from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Field, Session, select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import requests

# Datos de la conexión
DATABASE_URL = "mysql+pymysql://root:pass25@localhost:3306/reto25"
engine = create_engine(DATABASE_URL)

app = FastAPI()

API_PARA_CONVERTIR_URL = "http://localhost:8088/convertir"

class Pais(SQLModel, table=True):
    pais_codigo: str = Field(primary_key=True)
    pais_nombre: str

class Temperatura(SQLModel, table=True):
    temperatura_paiscodigo: str = Field(foreign_key="pais.pais_codigo", primary_key=True)
    temperatura_anio: int = Field(primary_key=True)
    temperatura_celsius: float
    temperatura_fahrenheit: float | None = None


def get_db():
    with Session(engine) as session:
        yield session


@app.get("/temperatura/{codigo_pais}/{anio}")
def obtener_temperatura(codigo_pais: str, anio: int, db: Session = Depends(get_db)):
    # Buscar en la BD la temperatura en Celsius
    stmt = select(Temperatura).where(
        (Temperatura.temperatura_paiscodigo == codigo_pais) &
        (Temperatura.temperatura_anio == anio)
    )
    temperatura = db.exec(stmt).first()

    if not temperatura:
        raise HTTPException(status_code=404, detail="No se encontró la temperatura para el país y año dados")

    stmt_pais = select(Pais.pais_nombre).where(Pais.pais_codigo == codigo_pais)
    pais = db.exec(stmt_pais).first()

    if not pais:
        raise HTTPException(status_code=404, detail="No se encontró el país en la base de datos")

    if temperatura.temperatura_fahrenheit is None:
        try:
            response = requests.get(API_PARA_CONVERTIR_URL, params={"celsius": temperatura.temperatura_celsius})
            response.raise_for_status()
            fahrenheit = response.json().get("fahrenheit")

            if fahrenheit is None:
                raise HTTPException(status_code=500, detail="Error en la respuesta de la API externa")

            temperatura.temperatura_fahrenheit = fahrenheit
            db.add(temperatura)
            db.commit()

        except requests.RequestException:
            raise HTTPException(status_code=500, detail="Error al consultar la API externa")

    return {
        "pais": pais,
        "año": anio,
        "celsius": temperatura.temperatura_celsius,
        "fahrenheit": temperatura.temperatura_fahrenheit
    }




