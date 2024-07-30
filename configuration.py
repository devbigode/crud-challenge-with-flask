from routes.login import login_route
from routes.user import user_route
from routes.home import home_route
from database.customers import db
from database.models import User, Worker

def init(app):
    config_routes(app)
    config_db()

def config_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(login_route)
    app.register_blueprint(user_route, url_prefix='/user')

def config_db():
    db.connect()
    db.create_tables([User, Worker])