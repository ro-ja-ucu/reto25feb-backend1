# Reto UCU Febrero 2025 - Entregable 1 Backend

## Consigna

Se solicita desarrollar una API REST en Python que permita obtener consultar información sobre temperaturas promedio por año en varios países en grados Celsius, y actualizar estos registros con la información de temperaturas promedio en grados Fahrenheit por medio de una API externa.

Se provee un `docker-compose.yaml` que levanta una base de datos MySQL y una API externa que permite convertir de grados Celsius a grados Fahrenheit. 

## Instrucciones

1. Clonar el repositorio.
2. Copiar el archivo `.env.example` a `.env`.
3. Levantar los servicios con el comando `docker-compose up -d --build`.

## Descripción de Servicios

### Base de Datos

La base de datos cuenta con una tabla `temperatura` que tiene la siguiente estructura:

|temperatura|
|--------------|
|**PK** temperatura_paiscodigo|
|**PK** temperatura_anio|
|temperatura_celsius|
|temperatura_fahrenheit|

Por defecto, conexión a la base de datos se realiza con las siguientes credenciales:
- Usuario: `reto25`
- Contraseña: `pass25`
- Base de datos: `reto25`
- Puerto: `3306`

### API Externa

La API provista cuenta con un único endpoint `GET /convertir` que recibe el parámetro `celsius` de tipo `Query`  y retorna un JSON con la conversión a grados Fahrenheit.

```json
{
    "fahrenheit": 32
}
```

## Requerimientos

Se busca que usted desarrolle una API REST en Python con FastAPI exponiendo el endpoint `GET /temperatura/{código_país}/{año}`. Este endpoint deberá: 
- Retornar un JSON con el siguiente formato:
    ```json
    {
        "pais": "Uruguay",
        "año": 2020,
        "celsius": 25,
        "fahrenheit": 77
    }
    ```
- Obtener la información sobre nombre del país y temperatura en grados Celsius desde una base de datos MySQL mediante SQLModel.
- Obtener la información sobre temperatura en grados Fahrenheit desde la API externa.
- Almacenar la información de la temperatura en grados Fahrenheit en la base de datos.
