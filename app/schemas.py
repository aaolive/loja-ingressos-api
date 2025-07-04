# from pydantic import BaseModel, EmailStr, field_validator
# from typing import Optional
# from datetime import date, datetime


# # Schema base para o usuário, com os campos que são comuns
# # tanto na criação quanto na leitura.
# class UsuarioBase(BaseModel):
#     nome: str
#     email: EmailStr


# # Schema para a criação de um novo usuário.
# # Herda de UsuarioBase e adiciona o campo de senha.
# class UsuarioCreate(UsuarioBase):
#     senha: str


# # Schema para a leitura de um usuário.
# # Inclui os campos do banco de dados que queremos retornar na API.
# # `orm_mode = True` permite que o Pydantic leia os dados diretamente
# # de um objeto ORM do SQLAlchemy.
# class Usuario(UsuarioBase):
#     id: int
#     ativo: bool

#     class Config:
#         orm_mode = True


# # schema para evento
# class Evento(BaseModel):
#     nome: str
#     descricao: str
#     data_inicial: date
#     data_final: date
#     duracao: str
#     observacoes: str

#     @field_validator('data_inicial', 'data_final', mode='before')
#     def parse_date(cls, value):
#         return datetime.strptime(value, "%d-%m-%Y").date()  # Adapte o formato conforme necessário
    

#     class Config:
#         orm_mode = True


from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime # Importe date e datetime

# ... (schemas de Usuario permanecem os mesmos) ...

class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    senha: str

class Usuario(UsuarioBase):
    id: int
    ativo: bool

    class Config:
        orm_mode = True

# --- INÍCIO DA MODIFICAÇÃO ---

# Schema base para o evento
class EventoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    data_inicio: datetime
    data_final: datetime
    observacoes: Optional[str] = None

# Schema para a criação de um evento
class EventoCreate(EventoBase):
    pass # Não precisa de campos adicionais para a criação

# Schema para a leitura/retorno de um evento da API
class Evento(EventoBase):
    id: int

    class Config:
        orm_mode = True

# --- FIM DA MODIFICAÇÃO ---