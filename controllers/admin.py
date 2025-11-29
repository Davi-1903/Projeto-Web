from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from models.sugestao import Sugestao
from models.resposta_adm import RespostaAdm
from models.historico_status import HistoricoStatus
from database import Session
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import selectinload


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/sugestoes', methods=['GET'])
@login_required
def listar_sugestoes():
    if current_user.tipo_usuario != 'admin':    
        flash('Você não tem permissão para acessar esta página', category='error')
        return redirect(url_for('sugestoes.listar'))
    
    with Session() as session:
        sugestoes = (
            session.query(Sugestao).options(
                selectinload(Sugestao.usuario),
                selectinload(Sugestao.respostas).selectinload(RespostaAdm.admin),
                selectinload(Sugestao.historico).selectinload(HistoricoStatus.admin)
            ).order_by(Sugestao.criado_em.desc()).all()
        )

    return render_template('admin/sugestoes.html', sugestoes=sugestoes)


@admin_bp.route('/sugestoes/<int:sugestao_id>/status', methods=['PATCH', 'POST'])
@login_required
def atualizar_status(sugestao_id: int):
    if current_user.tipo_usuario != 'admin':
        flash('Você não tem permissão para acessar esta página', category='error')
        return redirect(url_for('sugestoes.listar'))
    
    with Session() as session:
        try:
            sugestao = session.get(Sugestao, sugestao_id)
            
            if not sugestao:
                flash('Sugestão não encontrada', category='error')
                return redirect(url_for('admin.listar_sugestoes'))
            
            data = request.form
            novo_status = data.get('status')
            descricao_implementacao = data.get('descricao_implementacao', '').strip()
            
            status_validos = ['pendente', 'em_analise', 'aprovada', 'implementada', 'recusada']
            if novo_status not in status_validos:
                flash('Status inválido', category='error')
                return redirect(url_for('admin.listar_sugestoes'))
            
            if novo_status == 'implementada' and not descricao_implementacao:
                flash('Descrição da implementação é obrigatória', category='error')
                return redirect(url_for('admin.listar_sugestoes'))
            
            status_anterior = sugestao.status
            
            if status_anterior != novo_status:
                historico = HistoricoStatus(
                    sugestao_id=sugestao_id,
                    status_anterior=status_anterior,
                    status_novo=novo_status,
                    alterado_por=current_user.id
                )
                session.add(historico)
            
            sugestao.status = novo_status
            if novo_status == 'implementada':
                sugestao.descricao_implementacao = descricao_implementacao
            
            session.commit()
            flash(f'Status atualizado para: {novo_status}', category='success')
            
        except Exception as e:
            session.rollback()
            flash('Ocorreu um erro ao atualizar o status', category='error')
            print(f"Erro: {e}")
    
    return redirect(url_for('admin.listar_sugestoes'))


@admin_bp.route('/sugestoes/<int:sugestao_id>/resposta', methods=['POST'])
@login_required
def adicionar_resposta(sugestao_id: int):
    if current_user.tipo_usuario != 'admin':
        flash('Você não tem permissão para acessar esta página', category='error')
        return redirect(url_for('sugestoes.listar'))
    
    with Session() as session:
        try:
            sugestao = session.get(Sugestao, sugestao_id)
            
            if not sugestao:
                flash('Sugestão não encontrada', category='error')
                return redirect(url_for('admin.listar_sugestoes'))
            
            data = request.form
            resposta_texto = data.get('resposta', '').strip()
            
            if not resposta_texto:
                flash('A resposta não pode estar vazia', category='error')
                return redirect(url_for('admin.listar_sugestoes'))
            
            nova_resposta = RespostaAdm(
                sugestao_id=sugestao_id,
                admin_id=current_user.id,
                resposta=resposta_texto
            )
            
            session.add(nova_resposta)
            session.commit()
            
            flash('Resposta adicionada com sucesso', category='success')
            
        except Exception as erro:
            session.rollback()
            flash('Ocorreu um erro ao adicionar a resposta', category='error')
            print(f"Erro: {erro}")
    
    return redirect(url_for('admin.listar_sugestoes'))