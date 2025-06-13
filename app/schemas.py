from pydantic import BaseModel, EmailStr
from typing import Optional

# Schema base para o usuário, com os campos que são comuns
# tanto na criação quanto na leitura.
class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr

# Schema para a criação de um novo usuário.
# Herda de UsuarioBase e adiciona o campo de senha.
class UsuarioCreate(UsuarioBase):
    senha: str

# Schema para a leitura de um usuário.
# Inclui os campos do banco de dados que queremos retornar na API.
# `orm_mode = True` permite que o Pydantic leia os dados diretamente
# de um objeto ORM do SQLAlchemy.
class Usuario(UsuarioBase):
    id: int
    ativo: bool

    class Config:
        orm_mode = True