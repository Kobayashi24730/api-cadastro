from flask import Flask, request, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

banco = "dados.db"

def inicializarbanco():
    conn = sqlite3.connect(banco)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT UNIQUE,
        senha TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

inicializarbanco()

@app.route("/cadastra", methods=["POST"])
def cadastra():
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senha")
    
    if not nome or not email or not senha:
        return jsonify({"Erro": "Preencha todos os campos"}), 400
    
    senha_hash = generate_password_hash(senha)
    
    try:
        conn = sqlite3.connect(banco)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dados (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha_hash))
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError as ex:
        return jsonify({"Erro": "Email já cadastrado"}), 400
    except Exception as ex:
        return jsonify({"Erro": f"Erro ao cadastrar: {str(ex)}"}), 400
        
    return jsonify({"Status": "OK", "Mensagem": "Dados cadastrados com sucesso!","nome": nome})
    
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    senha = data.get("senha")
    
    if not email or not senha:
        return jsonify({"Erro": "Preencha email e senha"}), 400
    
    conn = sqlite3.connect(banco)
    cursor = conn.cursor()
    cursor.execute("SELECT nome,senha FROM dados WHERE email = ?", (email,))
    res = cursor.fetchone()
    conn.close()
    
    if res and check_password_hash(res[0], senha):
        return jsonify({"Status": "OK", "Mensagem": "Login bem sucedido","nome": res[0]})
    else:
        return jsonify({"Erro": "Login fracassado"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
