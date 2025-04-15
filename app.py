from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receber_webhook():
    dados = request.json
    print("📩 Dados recebidos do Webhook:")
    print(dados)

    return jsonify({"mensagem": "Webhook recebido com sucesso"}), 200
