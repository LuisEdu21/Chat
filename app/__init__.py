from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Registra as rotas
    from app.routes import chat_bp
    app.register_blueprint(chat_bp)
    
    return app
