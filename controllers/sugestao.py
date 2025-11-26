from flask import Blueprint, flash, render_template, request
from flask_login import current_user, login_required
from models.sugestao import Sugestao
from database import Session


sugestoes_bp = Blueprint('sugestoes', __name__, url_prefix='/sugestoes')


@sugestoes_bp.route('/', methods=['GET'])
@login_required
def listar():
    with Session() as session:
        sugestoes = session.query(Sugestao).all()
    return render_template('sugestoes/sugestoes.html', sugestoes=sugestoes)


@sugestoes_bp.route('/', methods=['POST'])
@login_required
def criar():
    with Session() as session:
        try:
            data = request.form

            nova_sugestao = Sugestao(
                titulo=data['titulo'],
                descricao=data['descricao'],
                usuario_id=current_user.id
            )
            session.add(nova_sugestao)
            session.commit()
            flash('Nova sugestão criada', category='success')

        except:
            session.rollback()
            flash('Ocorreu um erro interno', category='error')

    return render_template('sugestoes/sugestoes.html', sugestoes=[])
