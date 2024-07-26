from flask import Blueprint, render_template, request
from database.models import User

user_route = Blueprint('user', __name__)

@user_route.route("/list")
def list_user():
    user_db = User.select()
    
    return render_template('table.html', user = user_db)

@user_route.route("/new")
def form_create():

    return render_template('form.html')

@user_route.route("/new", methods=["POST"])
def create_user():
    dados = request.json
    new_user = User.create(name = dados['nome'], cpf = dados['cpf'], email = dados['email'], birthday = dados['nascimento'])

    return render_template('item_user.html', u = new_user)

@user_route.route("/<int:id_user>/update")
def view_user(id_user):
    user = User.get_by_id(id_user)
    return render_template('form_edit.html', u = user)

@user_route.route("/<int:id_user>/update", methods=["PUT"])
def update_user(id_user):
    user = User.get_by_id(id_user)
    dados = request.json
    
    user.name = dados['nome']
    user.birthday = dados['nascimento']
    user.cpf = dados['cpf']
    user.email = dados['email']
    user.save()
    
    return render_template('item_user.html', u = user)

# @user_route.route("/delete")
# def alert_delete():
#     return render_template('item_user.html')

@user_route.route("/<int:id_user>/delete", methods=["DELETE"])
def delete_user(id_user):
    User.delete_by_id(id_user)
    return {'deletado': 'ok'}