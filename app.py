from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dados = request.json
        print("📩 Dados recebidos do Webhook:")
        print(dados)
        return jsonify({"mensagem": "Webhook recebido com sucesso"}), 200
    else:
        return "<h1>👋 Webhook ativo!</h1><p>Envie um POST para esta URL com um JSON válido.</p>"
