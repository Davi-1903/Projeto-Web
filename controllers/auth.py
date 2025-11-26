from typing import Literal
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from database import Session
from models.usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash
from re import compile


auth_bp = Blueprint('auth', __name__)


def classify_user(email: str) -> Literal['aluno', 'funcionario', 'admin'] | None:
    re_aluno = compile(r'[\w\W]+@aluno\.com')
    re_funcionario = compile(r'[\w\W]+@funcionario\.com')
    re_admin = compile(r'[\w\W]+@admin\.com')

    if re_aluno.findall(email):
        return 'aluno'
    if re_funcionario.findall(email):
        return 'funcionario'
    if re_admin.findall(email):
        return 'admin'


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        with Session() as session:
            try:
                data = request.form

                user = session.query(Usuario).filter_by(email=data['email']).first()
                if user is None:
                    flash('Este email não está cadastrado', category='error')
                    return render_template('auth/login.html')
                
                if not check_password_hash(user.senha_hash, data['senha']): # type: ignore
                    flash('A senha está incorreta', category='error')
                    return render_template('auth/login.html')
                
                login_user(user)
                flash('Novo usuário registrado no sistema', category='success')
                return redirect(url_for('sugestoes.listar'))
            
            except:
                session.rollback()
                flash('Ocorreu um erro interno', category='error')
    
    return render_template('auth/login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        with Session() as session:
            try:
                data = request.form
                
                user = session.query(Usuario).filter_by(email=data['email']).first()
                if user:
                    flash('Este email já está cadastrado', category='error')
                    return render_template('auth/register.html')
                
                tipo_usuario = classify_user(data['email'])
                if tipo_usuario is None:
                    flash(f'O email {data["email"]} é inválido', category='error')
                    return render_template('auth/register.html')
                
                new_user = Usuario(
                    nome=data['name'],
                    email=data['email'],
                    senha_hash=generate_password_hash(data['senha']),
                    tipo_usuario=tipo_usuario
                )
                session.add(new_user)
                session.commit()
                login_user(new_user)
                flash('Novo usuário registrado no sistema', category='success')
                return redirect(url_for('sugestoes.listar'))
            
            except:
                session.rollback()
                flash('Ocorreu um erro interno', category='error')

    return render_template('auth/register.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
