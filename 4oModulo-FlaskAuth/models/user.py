from database import db
from flask_login import UserMixin

# heranca multipla, herda do db.Model e do UserMixin pra adicionar todos os metodos
class User(db.Model, UserMixin):
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(40), nullable=False, unique=True)
  password = db.Column(db.String(20), nullable=False)
