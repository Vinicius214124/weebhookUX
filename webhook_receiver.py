from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receber_webhook():
    dados = request.json
    print("📩 Dados recebidos do Webhook:")
    print(dados)

    # Aqui você pode tratar os dados, salvar em um banco, etc.
    return jsonify({"mensagem": "Webhook recebido com sucesso"}), 200

if __name__ == '__main__':
    app.run(port=5000)
