from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

tarefas = []
agentes = []

@app.route("/")
def inicio():
    return jsonify({
        "sistema": "Silver",
        "status": "ONLINE",
        "hora": datetime.now().isoformat(),
        "tarefas": len(tarefas),
        "agentes": len(agentes)
    })

@app.route("/status")
def status():
    return jsonify({
        "status": "ONLINE",
        "tarefas": len(tarefas),
        "agentes": len(agentes)
    })

if __name__ == "__main__":
    app.run()
