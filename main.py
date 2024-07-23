from flask import Flask
from configuration import init

app = Flask(__name__)

init(app)

app.run(debug=True)
