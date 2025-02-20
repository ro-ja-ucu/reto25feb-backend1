# Temp API

API REST en Python con FastAPI que permite convertir temperaturas en grados Celsius a grados Fahrenheit.

## Endpoints

- `GET /convertir?celsius={celsius}`:
    
    Recibe un parámetro `celsius` de tipo `Query` y retorna un JSON con la conversión a grados Fahrenheit.
    ```json
    {
        "fahrenheit": 32
    }
    ```