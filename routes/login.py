from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user
from database.models import Worker

login_route = Blueprint('login', __name__)

@login_route.route('/login', methods=['GET', 'POST'])
def login(): 
    
    if request.method == 'POST':
        u = request.form['email']
        p = request.form['password']
        
        user = Worker.get_or_none(Worker.email == u)

        if user and user.password == p:
            login_user(user)
            flash("Login bem-sucedido!", "success")
            return redirect(url_for('home.home'))
        elif user:
            flash("Senha incorreta.","danger")
        else:
            flash("Usuário não encontrado!","danger")
    return render_template('login.html')

@login_route.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.login'))