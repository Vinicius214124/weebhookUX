from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Armazena o último JSON recebido
ultimo_json_recebido = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    global ultimo_json_recebido

    if request.method == 'POST':
        dados = request.json
        print("📩 Dados recebidos do Webhook:")
        print(dados)

        # Armazena os dados recebidos
        ultimo_json_recebido = dados

        return jsonify({"mensagem": "Webhook recebido com sucesso"}), 200

    else:
        # Exibe o último JSON recebido
        if ultimo_json_recebido:
            return jsonify(ultimo_json_recebido)
        else:
            return jsonify({
                "status": "aguardando",
                "mensagem": "Nenhum JSON recebido ainda."
            })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
