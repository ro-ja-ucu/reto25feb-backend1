from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
import requests

# Datos de la conexión
DATABASE_URL = "mysql+pymysql://root:pass25@localhost:3306/reto25"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

API_PARA_CONVERTIR_URL = "http://localhost:8088/convertir"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return {"message": "Hello from apiejercicio!"}

@app.get("/test-db")
def test_db(db=Depends(get_db)):
    result = db.execute(text("SELECT DATABASE();"))
    return {"database": result.scalar()}


@app.get("/temperatura/{codigo_pais}/{anio}")
def obtener_temperatura(codigo_pais: str, anio: int, db: Session = Depends(get_db)):

    query = text("""
        SELECT t.temperatura_celsius, t.temperatura_fahrenheit, p.pais_nombre 
        FROM temperatura t
        JOIN pais p ON t.temperatura_paiscodigo = p.pais_codigo
        WHERE t.temperatura_paiscodigo = :codigo_pais AND t.temperatura_anio = :anio
    """)

    result = db.execute(query, {"codigo_pais": codigo_pais, "anio": anio}).fetchone()

    if not result:
        raise HTTPException(status_code=404, detail="No se encontró información para ese país y año")

    celsius, fahrenheit, pais_nombre = result

    # Si ya no guardamos en la BD llamamos a la api externa
    if fahrenheit is None:
        response = requests.get(API_PARA_CONVERTIR_URL, params={"celsius": celsius})
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error al consultar la API externa")

        fahrenheit = response.json()["fahrenheit"]


        update_query = text("""
            UPDATE temperatura 
            SET temperatura_fahrenheit = :fahrenheit 
            WHERE temperatura_paiscodigo = :codigo_pais AND temperatura_anio = :anio
        """)
        db.execute(update_query, {"fahrenheit": fahrenheit, "codigo_pais": codigo_pais, "anio": anio})
        db.commit()


    return {
        "pais": pais_nombre,
        "año": anio,
        "celsius": celsius,
        "fahrenheit": fahrenheit
    }




