from sqlalchemy.orm import Session
from . import models, schemas

# Função para obter um usuário pelo ID
def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

# Função para obter um usuário pelo email
def get_usuario_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

# Função para obter uma lista de usuários
def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

# Função para criar um novo usuário
def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    # Em um projeto real, aqui você faria o hash da senha
    senha_hash_ficticia = usuario.senha + "notreallyhashed"
    
    db_usuario = models.Usuario(
        email=usuario.email, nome=usuario.nome, senha_hash=senha_hash_ficticia
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

# Função para atualizar um usuário (exemplo simples)
def update_usuario(db: Session, usuario_id: int, usuario_update: schemas.UsuarioCreate):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario:
        db_usuario.nome = usuario_update.nome
        db_usuario.email = usuario_update.email
        # Atualizar senha se fornecida
        if usuario_update.senha:
            db_usuario.senha_hash = usuario_update.senha + "notreallyhashed"
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

# Função para deletar um usuário
def delete_usuario(db: Session, usuario_id: int):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario


# -------------------Funcoes crud para o evento -------------------

# def get_evento(db: Session, evento_id: int):
#     return db.query(models.Evento).filter(models.Evento.id == evento_id).first()

# def get_eventos(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Evento).offset(skip).limit(limit).all()

# def create_evento(db: Session, evento: schemas.Evento):
#     db_evento = models.Evento(
#         nome=evento.nome,
#         descricao=evento.descricao,
#         data_inicial=evento.data_inicial,
#         data_final=evento.data_final,
#         duracao=evento.duracao,
#         observacoes=evento.observacoes
#     )
#     db.add(db_evento)
#     db.commit()
#     db.refresh(db_evento)
#     return db_evento

# def update_evento(db: Session, evento_id: int, evento_update: schemas.Evento):
#     db_evento = get_evento(db, evento_id)
#     if db_evento:
#         db_evento.nome = evento_update.nome
#         db_evento.descricao = evento_update.descricao
#         db_evento.data_inicial = evento_update.data_inicial
#         db_evento.data_final = evento_update.data_final
#         db_evento.duracao = evento_update.duracao
#         db_evento.observacoes = evento_update.observacoes
#         db.commit()
#         db.refresh(db_evento)
#     return db_evento

# def delete_evento(db: Session, evento_id: int):
#     db_evento = get_evento(db, evento_id)
#     if db_evento:
#         db.delete(db_evento)
#         db.commit()
#     return db_evento

# --- INÍCIO DA MODIFICAÇÃO ---

# Função para obter um evento pelo ID
def get_evento(db: Session, evento_id: int):
    return db.query(models.Evento).filter(models.Evento.id == evento_id).first()

# Função para obter uma lista de eventos
def get_eventos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Evento).offset(skip).limit(limit).all()

# Função para criar um novo evento
def create_evento(db: Session, evento: schemas.EventoCreate):
    db_evento = models.Evento(**evento.dict())
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento

# Função para atualizar um evento
def update_evento(db: Session, evento_id: int, evento_update: schemas.EventoCreate):
    db_evento = get_evento(db, evento_id)
    if db_evento:
        # Pega o dicionário de dados do schema de atualização
        update_data = evento_update.dict(exclude_unset=True)
        # Itera sobre os dados e atualiza os campos do objeto do banco
        for key, value in update_data.items():
            setattr(db_evento, key, value)
        db.commit()
        db.refresh(db_evento)
    return db_evento

# Função para deletar um evento
def delete_evento(db: Session, evento_id: int):
    db_evento = get_evento(db, evento_id)
    if db_evento:
        db.delete(db_evento)
        db.commit()
    return db_evento

# --- FIM DA MODIFICAÇÃO ---