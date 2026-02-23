from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import sqlite3
import json
from groq import Groq
from dotenv import load_dotenv
from fastapi import FastAPI
from datetime import datetime
import holidays

load_dotenv()

app = FastAPI()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
br_holidays = holidays.Brazil()
DB_PATH = "data/estacionamentos.db"

@app.get("/locais")
async def get_locais():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT nome, lat, lng, tipo FROM locais")
    rows = cursor.fetchall()
    conn.close()
    return [{"nome": r[0], "lat": r[1], "lng": r[2], "tipo": r[3]} for r in rows]

@app.get("/predict")
async def predict_vagas(lat: float, lng: float, local: str, hora: int = None, data: str = None):
    if hora is None:
        hora = datetime.now().hour
    if data is None:
        data = datetime.now().date().isoformat()

    prompt = f"""
    Você é um especialista em trânsito urbano de Salvador, Bahia.
    Analise o local: "{local}" (Coordenadas: {lat}, {lng}).
    Horário solicitado: {hora}:00h.
    Data solicitada: {data}.

    REGRAS DE ANÁLISE:
    1. Se o nome contiver "Zona Azul", considere a rotatividade e o horário comercial de Salvador (08h às 18h).
    2. Considere a localização: Se for Orla (Barra, Rio Vermelho, Itapuã), a lotação aumenta após às 17h e fins de semana.
    3. Se for Comércio ou Centro, a lotação é máxima em horário comercial e baixa à noite.

    RETORNE ESTRITAMENTE UM JSON com:
    - "prediction": (Livre, Moderado ou Lotado)
    - "percentage": (Inteiro de 0 a 100, onde 100% é fácil de estacionar)
    - "justificativa": (Uma frase curta explicando o motivo baseado no contexto local)
    """

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"} 
        )
        
        resposta_ia = json.loads(completion.choices[0].message.content)
        return resposta_ia

    except Exception as e:
        print(f"Erro na IA: {e}")
        return {
            "prediction": "Indisponível",
            "percentage": 50,
            "justificativa": "Não foi possível analisar o tráfego em tempo real."
        }

frontend_path = os.path.join(os.path.dirname(__file__), "frontend")

#INDEX
@app.get("/")
async def read_index():
    return FileResponse(os.path.join(frontend_path, "index.html"))

@app.get("/sw.js")
async def get_sw():
    return FileResponse(os.path.join(frontend_path, "sw.js"))

@app.get("/manifest.json")
async def get_manifest():
    return FileResponse(os.path.join(frontend_path, "manifest.json"))

app.mount("/", StaticFiles(directory=frontend_path), name="static")