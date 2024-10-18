import requests
from app.models import get_user_data

def process_chat(data):
    user = data.get('user')
    message = data.get('message')
    
    # Busca dados do usuário
    user_data = get_user_data(user)
    
    # Lógica do chat baseada no tipo de usuário
    response = generate_response(user_data, message)
    
    # Envia para WebHook
    send_to_webhook(user, message, response)
    
    return {"user": user, "response": response}

def send_to_webhook(user, message, response):
    WEBHOOK_URL = 'https://example.com/webhook'
    requests.post(WEBHOOK_URL, json={"user": user, "message": message, "response": response})
