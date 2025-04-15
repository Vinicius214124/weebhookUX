import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        data = request.json  # Recebe JSON do webhook

        # Exemplo de acesso aos dados recebidos
        nome = data.get("name")
        cpf = data.get("cpf")
        email = data.get("email")

        # Exibir no terminal do Render
        print(f"Nome: {nome}, CPF: {cpf}, Email: {email}")

        # Retorna o JSON recebido
        return jsonify(data), 200

    # Apenas para teste, informando que o webhook está ativo
    return jsonify({"mensagem": "Webhook ativo! Envie um POST com JSON para esta URL."}), 200

if __name__ == '__main__':
    # Usa a porta fornecida pelo Render ou padrão 5000 localmente
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
