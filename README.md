# 🔐 API de Cadastro e Login com Flask + SQLite

Este é um projeto simples de uma API REST desenvolvida com **Flask** para fins de aprendizado. Ele permite o **cadastro de usuários com nome, e-mail e senha**, além de um sistema de **login seguro com senha criptografada**.

---

## 🚀 Tecnologias utilizadas

- Python 3.x
- Flask
- SQLite
- Flask-CORS
- Werkzeug (para criptografia de senhas)

---

## 📦 Funcionalidades

- ✅ Cadastro de usuário (`POST /cadastra`)
- ✅ Login de usuário (`POST /login`)
- ✅ Criptografia de senha com `generate_password_hash`
- ✅ Validação básica de campos obrigatórios
- ✅ Banco de dados local SQLite
- ✅ Suporte a CORS para testes com frontend

---

## 📁 Estrutura do banco de dados

Tabela `dados`:

| Campo  | Tipo     | Descrição              |
|--------|----------|------------------------|
| id     | INTEGER  | ID único (auto)        |
| nome   | TEXT     | Nome do usuário        |
| email  | TEXT     | E-mail (único)         |
| senha  | TEXT     | Senha criptografada    |

---

## 📨 Endpoints

### ➕ POST `/cadastra`

Cadastra um novo usuário.

#### 📤 Requisição (JSON):
```json
{
  "nome": "João",
  "email": "joao@email.com",
  "senha": "senha123"
}
