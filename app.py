from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json  # recebe o JSON enviado pelo webhook

    # Exemplo de como acessar os dados:
    tags = data.get("tags", [])
    nome = data.get("name")
    cpf = data.get("cpf")
    email = data.get("email")
    telefone = data.get("phone")
    affiliate = data.get("affiliate")
    transaction_id = data.get("transaction_id")
    transaction_value = data.get("transaction_value")
    ip_address = data.get("ip_address")
    user_agent = data.get("user_agent")
    creation_date = data.get("creation_date")
    withdrawal_date = data.get("withdrawal_date")

    # Exibir no terminal
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"E-mail: {email}")
    print(f"Telefone: {telefone}")
    print(f"Afiliado: {affiliate}")
    print(f"ID Transação: {transaction_id}")
    print(f"Valor Transação: {transaction_value}")
    print(f"IP: {ip_address}")
    print(f"User Agent: {user_agent}")
    print(f"Data Criação: {creation_date}")
    print(f"Data Retirada: {withdrawal_date}")
    print(f"Tags: {tags}")

    # Pode retornar uma resposta JSON se necessário
    return jsonify({"status": "Recebido com sucesso", "dados": data}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
