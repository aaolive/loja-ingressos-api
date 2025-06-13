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