from flask import Flask
from .routes import init_app

def create_app():
    app = Flask(__name__)
    
    init_app(app)

    return app