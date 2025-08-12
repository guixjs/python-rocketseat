from flask import Flask, request, jsonify
from database import db
from models.user import User
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = "uau"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

login_manager = LoginManager()



db.init_app(app)
login_manager.init_app(app)

# view é obrigatorio, é a rota que vai fazer a autenticacao
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)


@app.route("/login", methods=['POST'])
def login():
  data = request.json
  username = data.get('username')
  password = data.get('password')


  if username and password:
    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
      login_user(user)
      print(current_user.is_authenticated)
      return jsonify({
    "mensagem":"Login realizado"
  })


  return jsonify({
    "mensagem":"Credenciais inválidas"
  }), 400


@login_required # tipo um PreAuthorization no spring
@app.route("/logout", methods=['GET'])
def logout():
  logout_user()
  return jsonify({
    "mensagem":"Logout realizado com sucesso"
  })

@app.route("/new", methods=['POST'])
def create_user():
  data = request.json
  username = data.get('username')
  password = data.get('password')

  if username and password:
     user = User(username=username, password=password)
     db.session.add(user)
     db.session.commit()
     return jsonify({
    "mensagem":"Cadastro realizado com sucesso"
  })
  return jsonify({
    "mensagem":"Credenciais inválidas"
  }), 400



@app.route("/user/<int:id>", methods=['GET'])
@login_required
def read_user(id):
  user = User.query.get(id)

  if user:
    return jsonify({
    "username": user.username
  })
  

  return jsonify({
    "mensagem":"Usuário não encontrado"
  }), 404


@app.route("/user/<int:id>", methods=['PUT'])
@login_required
def update_user(id):
  user = User.query.get(id)
  data = request.json
  if user and data.get("password"):
    user.password = data.get("password")
    db.session.commit()
    return jsonify({
    "mensagem": f"O usuário {user.username} foi atualizado com sucesso"
  })
  

  return jsonify({
    "mensagem":"Usuário não encontrado"
  }), 404


@app.route("/user/<int:id>", methods=['DELETE'])
@login_required
def read_user(id):
  user = User.query.get(id)

  if user:
    if id == current_user.id:
      logout()
    db.session.delete(user)
    db.session.commit()
    return jsonify({
    "username": f"Usuário {user.id} deletado com sucesso"
  })
  

  return jsonify({
    "mensagem":"Usuário não deletado"
  }), 404

if __name__ == "__main__":
  app.run(debug=True)
  