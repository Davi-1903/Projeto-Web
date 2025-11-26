from sqlalchemy import TIMESTAMP, Column, Enum, ForeignKey, Integer, func
from sqlalchemy.orm import relationship
from database import Base


class HistoricoStatus(Base):
    __tablename__ = 'historico_status'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sugestao_id = Column(Integer, ForeignKey('sugestoes.id'), nullable=False)
    status_anterior = Column(Enum('pendente', 'em_analise', 'aprovada', 'implementada', 'recusada'))
    status_novo = Column(Enum('pendente', 'em_analise', 'aprovada', 'implementada', 'recusada'))
    alterado_por = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    data_mudanca = Column(TIMESTAMP, server_default=func.current_timestamp())

    # Relacionamentos
    sugestao = relationship('Sugestao', back_populates='historico')
    admin = relationship('Usuario', back_populates='historico_status')