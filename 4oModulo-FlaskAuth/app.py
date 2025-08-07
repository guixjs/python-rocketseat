from flask import Flask
from database import db
from models.user import User
app = Flask(__name__)
app.config['SECRET_KEY'] = "uau"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db.init_app(app)


@app.route("/")
def hello():
  return "Teste"

if __name__ == "__main__":
  app.run(debug=True)
  