from flask import Flask, jsonify, Blueprint, request
from flask_jwt import JWT, jwt_required, current_identity
from database import *
from os import getenv
from dotenv import load_dotenv

app = Flask(__name__)
app.config["SECRET_KEY"] = "723H623872H7S72jhsjd7887H"

@app.route('/')
def index():
    return "Hola"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    return f"Se conecta, el usuario es: {username} y su clave es {password}"

if __name__ == '__main__':
    load_dotenv()
    Base.metadata.create_all(engine)
    app.run(debug=True)