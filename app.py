from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

tarefas = []
agentes = []


def proximo_id(lista):
    if not lista:
        return 1
    return max(item["id"] for item in lista) + 1


@app.route("/")
def inicio():
    return jsonify({
        "sistema": "Silver V1",
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


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.get_json(silent=True) or {}

    nome = dados.get("nome")

    if not nome:
        return jsonify({
            "erro": "O campo 'nome' é obrigatório."
        }), 400

    tarefa = {
        "id": proximo_id(tarefas),
        "nome": nome,
        "status": "pendente",
        "criada_em": datetime.now().isoformat()
    }

    tarefas.append(tarefa)

    return jsonify(tarefa), 201


@app.route("/tarefas/<int:tarefa_id>/concluir", methods=["POST"])
def concluir_tarefa(tarefa_id):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["status"] = "concluida"
            tarefa["concluida_em"] = datetime.now().isoformat()
            return jsonify(tarefa)

    return jsonify({
        "erro": "Tarefa não encontrada."
    }), 404


@app.route("/agentes", methods=["GET"])
def listar_agentes():
    return jsonify(agentes)


@app.route("/agentes", methods=["POST"])
def criar_agente():
    dados = request.get_json(silent=True) or {}

    nome = dados.get("nome")

    if not nome:
        return jsonify({
            "erro": "O campo 'nome' é obrigatório."
        }), 400

    agente = {
        "id": proximo_id(agentes),
        "nome": nome,
        "status": "ativo",
        "criado_em": datetime.now().isoformat()
    }

    agentes.append(agente)

    return jsonify(agente), 201


if __name__ == "__main__":
    app.run()
