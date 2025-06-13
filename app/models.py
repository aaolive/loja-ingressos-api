from sqlalchemy import Column, Integer, String, Boolean, Date
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)
    senha_hash = Column(String(255))
    ativo = Column(Boolean, default=True)

class Evento(Base):

    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    nome=Column(String(100))
    descricao = Column(String(100))
    data_inicial = Column(Date)
    data_final = Column(Date)