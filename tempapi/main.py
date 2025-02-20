from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/convert/ctof")
def celsius_to_fahrenheit(
    celsius: float = Query(..., description="Temperatura en grados Celsius")
):
    return {"fahrenheit": (celsius * (9.0 / 5.0)) + 32.0}