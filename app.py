from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receber_webhook():
    dados = request.json
    print("📩 Dados recebidos do Webhook:")
    print(dados)
    return jsonify({"mensagem": "Webhook recebido com sucesso"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Porta que o Render fornece
    app.run(host='0.0.0.0', port=port)        # Deixa o app acessível publicamente
