from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, Text, func
from sqlalchemy.orm import relationship
from database import Base


class RespostaAdm(Base):
    __tablename__ = 'respostas_adm'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sugestao_id = Column(Integer, ForeignKey('sugestoes.id'), nullable=False)
    admin_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    resposta = Column(Text, nullable=False)
    criado_em = Column(TIMESTAMP, server_default=func.current_timestamp())

    # Relacionamentos
    sugestao = relationship('Sugestao', back_populates='respostas')
    admin = relationship('Usuario', back_populates='respostas_admin')
