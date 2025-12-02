from flask_login import UserMixin
from sqlalchemy import TIMESTAMP, Column, Enum, Integer, String, func
from sqlalchemy.orm import relationship
from database import Base, Session


class Usuario(Base, UserMixin):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    tipo_usuario = Column(Enum('aluno', 'funcionario', 'admin'), nullable=False)
    criado_em = Column(TIMESTAMP, server_default=func.current_timestamp())

    sugestoes = relationship('Sugestao', back_populates='usuario', cascade='all, delete')
    respostas_admin = relationship('RespostaAdm', back_populates='admin')
    historico_status = relationship('HistoricoStatus', back_populates='admin')

    @classmethod
    def get(cls, user_id: int) -> 'Usuario | None':
        with Session() as session:
            return session.get(cls, user_id)
