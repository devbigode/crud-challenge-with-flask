from flask import Flask
from flask_login import LoginManager
from configuration import init
from database.models import Worker
from dotenv import load_dotenv
import os

load_dotenv()

key_login = os.getenv('KEY_LOGIN')

app = Flask(__name__)

app.secret_key = "key_login"

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return Worker.get_or_none(Worker.id == id)

init(app)

if __name__ == "__main__":
    app.run(debug=True)
    