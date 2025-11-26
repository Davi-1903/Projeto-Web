from sqlalchemy import TIMESTAMP, Column, Enum, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import relationship
from database import Base


class Sugestao(Base):
    __tablename__ = 'sugestoes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    titulo = Column(String(200), nullable=False)
    descricao = Column(Text, nullable=False)
    status = Column(Enum('pendente', 'em_analise', 'aprovada', 'implementada', 'recusada'), server_default='pendente')
    descricao_implementacao = Column(Text, nullable=True)
    criado_em = Column(TIMESTAMP, server_default=func.current_timestamp())
    atualizado_em = Column(
        TIMESTAMP,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp()
    )

    # Relacionamentos
    usuario = relationship('Usuario', back_populates='sugestões')
    respostas = relationship('RespostaAdm', back_populates='sugestao', cascade='all, delete')
    historico = relationship('HistoricoStatus', back_populates='sugestao', cascade='all, delete')
