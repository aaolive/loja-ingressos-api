# Importe o tipo de dado DateTime e Date
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date 
from .database import Base
import datetime # Importe a biblioteca datetime

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)
    senha_hash = Column(String(255))
    ativo = Column(Boolean, default=True)



# Adicione o novo modelo para a tabela de eventos
class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), index=True)
    descricao = Column(String(255))
    data_inicio = Column(DateTime, default=datetime.datetime.utcnow)
    data_final = Column(DateTime, default=datetime.datetime.utcnow)
    observacoes = Column(String(255), nullable=True) # Este campo pode ser nulo

