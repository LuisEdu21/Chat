from flask import Blueprint, request, jsonify

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    user = data.get('user', 'guest')

    # Resposta simples de exemplo
    response = f"Olá, {user}! Você disse: {message}"
    return jsonify({"user": user, "response": response})
