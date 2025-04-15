from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dados = request.json
        print("📩 Dados recebidos do Webhook:")
        print(dados)
        return jsonify({"mensagem": "Webhook recebido com sucesso"}), 200
    else:
        return "<h1>👋 Webhook ativo!</h1><p>Envie um POST com JSON para esta URL.</p>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
