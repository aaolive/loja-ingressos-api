from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import SessionLocal, engine

# Cria as tabelas no banco de dados (se não existirem)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Função de dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Endpoints da API ---

@app.post("/usuarios/", response_model=schemas.Usuario)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario_by_email(db, email=usuario.email)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return crud.create_usuario(db=db, usuario=usuario)

@app.get("/usuarios/", response_model=List[schemas.Usuario])
def read_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    usuarios = crud.get_usuarios(db, skip=skip, limit=limit)
    return usuarios

@app.get("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_usuario

@app.put("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def update_usuario(usuario_id: int, usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud.update_usuario(db, usuario_id=usuario_id, usuario_update=usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_usuario

@app.delete("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.delete_usuario(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_usuario


# -- Endpoints para eventos --

# @app.get("/eventos/", response_model=List[schemas.Evento])
# def read_eventos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     eventos = crud.get_eventos(db, skip=skip, limit=limit)
#     return eventos

# @app.get("/eventos/{evento_id}", response_model=schemas.Evento)
# def read_evento(evento_id: int, db: Session = Depends(get_db)):
#     db_evento = crud.get_evento(db, evento_id=evento_id)
#     if db_evento is None:
#         raise HTTPException(status_code=404, detail="Evento não encontrado")
#     return db_evento

# @app.post("/eventos/", response_model=schemas.Evento)
# def create_evento(evento: schemas.Evento, db: Session = Depends(get_db)):
#     db_evento = crud.create_evento(db, evento)
#     return db_evento

# @app.put("/eventos/{evento_id}", response_model=schemas.Evento)
# def update_evento(evento_id: int, evento: schemas.Evento, db: Session = Depends(get_db)):
#     db_evento = crud.update_evento(db, evento_id=evento_id, evento_update=evento)
#     if db_evento is None:
#         raise HTTPException(status_code=404, detail="Evento não encontrado")
#     return db_evento

# @app.delete("/eventos/{evento_id}", response_model=schemas.Evento)
# def delete_evento(evento_id: int, db: Session = Depends(get_db)):
#     db_evento = crud.delete_evento(db, evento_id=evento_id)
#     if db_evento is None:
#         raise HTTPException(status_code=404, detail="Evento não encontrado")
#     return db_evento


# --- INÍCIO DA MODIFICAÇÃO ---
# --- Endpoints da API para Eventos ---

@app.post("/eventos/", response_model=schemas.Evento)
def create_evento(evento: schemas.EventoCreate, db: Session = Depends(get_db)):
    return crud.create_evento(db=db, evento=evento)

@app.get("/eventos/", response_model=List[schemas.Evento])
def read_eventos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    eventos = crud.get_eventos(db, skip=skip, limit=limit)
    return eventos

@app.get("/eventos/{evento_id}", response_model=schemas.Evento)
def read_evento(evento_id: int, db: Session = Depends(get_db)):
    db_evento = crud.get_evento(db, evento_id=evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return db_evento

@app.put("/eventos/{evento_id}", response_model=schemas.Evento)
def update_evento(evento_id: int, evento: schemas.EventoCreate, db: Session = Depends(get_db)):
    db_evento = crud.update_evento(db, evento_id=evento_id, evento_update=evento)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return db_evento

@app.delete("/eventos/{evento_id}", response_model=schemas.Evento)
def delete_evento(evento_id: int, db: Session = Depends(get_db)):
    db_evento = crud.delete_evento(db, evento_id=evento_id)
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return db_evento

# --- FIM DA MODIFICAÇÃO ---