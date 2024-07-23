from flask import Blueprint, render_template, request
from database.models import User

user_route = Blueprint('user', __name__)

@user_route.route("/<int:user_id>")
def dashboard():
    return {"id":"Ok"}

@user_route.route("/list")
def list_user():
    user_db = User.select()
    
    return render_template('table.html', user = user_db)

@user_route.route("/view")
def view_user():
    # Modal com as info do usuário
    return render_template('item_user.html')

@user_route.route("/new")
def form_create():

    return render_template('form.html')

@user_route.route("/new", methods=["POST"])
def create_user():
    dados = request.json
    new_user = User.create(name = dados['nome'], cpf = dados['cpf'], email = dados['email'], birthday = dados['nascimento'])

    return render_template('item_user.html', u = new_user)

@user_route.route("/update")
def form_edit():
    # Renderizar um formulário de criação de usuário
    return render_template('edit_user.html')

@user_route.route("/update", methods=["PUT"])
def update_user():
    # Criar usuário
    return {'alterado': 'ok'}

@user_route.route("/delete")
def alert_delete():
    # Modal com as info do usuário
    return render_template('item_user.html')

@user_route.route("/delete", methods=["DELETE"])
def delete_user():
    # Criar usuário
    return {'deletado': 'ok'}