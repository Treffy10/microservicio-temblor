from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Microservicio de Proyección de Temblor activo"}

# Endpoint para obtener la proyección de temblor según ciudad y fecha
@app.get("/proyeccion_temblor")
async def obtener_proyeccion_temblor(ciudad: str, fecha: str):          
    """
    Devuelve una proyección de temblor simulada para la ciudad y fecha dadas.
    """
    # ==== Simulación de proyección de temblor ====
    proyecciones = [
        "Baja probabilidad de temblor",
        "Probabilidad moderada de temblor",
        "Alta probabilidad de temblor"
    ]
    proyeccion = proyecciones[(hash(ciudad + fecha) % len(proyecciones))]

    return {
        "proyeccion_temblor": proyeccion
    }