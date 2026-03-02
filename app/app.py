import os
import json
import sqlite3
from datetime import datetime

from flask import Flask, jsonify, request
from services.groq_services import get_groq_client
from dotenv import load_dotenv
import holidays

# =====================
# Configuração inicial
# =====================
load_dotenv()

app = Flask("OndeEstacionar")

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "data",
    "estacionamentos.db"
)

client = get_groq_client()

br_holidays = holidays.Brazil(state="BA")


# =====================
# Banco de dados
# =====================
def get_db():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


# =====================
# Rotas API
# =====================
@app.route("/estacionamentos")
def listar_estacionamentos():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estacionamentos")
    dados = cursor.fetchall()
    conn.close()
    return jsonify(dados)


@app.route("/locais")
def get_locais():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, lat, lng, tipo FROM locais")
    rows = cursor.fetchall()
    conn.close()

    return jsonify([
        {"nome": r[0], "lat": r[1], "lng": r[2], "tipo": r[3]}
        for r in rows
    ])


@app.route("/predict")
def predict_vagas():
    lat = request.args.get("lat")
    lng = request.args.get("lng")
    local = request.args.get("local")

    hora = request.args.get("hora", datetime.now().hour, type=int)
    data = request.args.get("data", datetime.now().date().isoformat())

    prompt = f"""
Você é um especialista em trânsito urbano de Salvador, Bahia.
Analise o local: "{local}" (Coordenadas: {lat}, {lng}).
Horário solicitado: {hora}:00h.
Data solicitada: {data}.

REGRAS DE ANÁLISE:
1. Se o nome contiver "Zona Azul", considere horário comercial (08h às 18h).
2. Se for Orla (Barra, Rio Vermelho, Itapuã), lotação aumenta após 17h e fins de semana.
3. Centro e Comércio: pico em horário comercial.

RETORNE ESTRITAMENTE UM JSON com:
- prediction
- percentage
- justificativa
"""

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )

        return json.loads(completion.choices[0].message.content)

    except Exception as e:
        return jsonify({
            "prediction": "Indisponível",
            "percentage": 50,
            "justificativa": "Erro ao processar a previsão."
        })