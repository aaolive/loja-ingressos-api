from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco de dados SQLite.
# O arquivo do banco de dados será criado na raiz do projeto como "cadastro.db".
SQLALCHEMY_DATABASE_URL = "sqlite:///./cadastro.db"

# Cria a engine do SQLAlchemy.
# O argumento `connect_args` é necessário apenas para o SQLite para permitir
# o uso da mesma conexão em diferentes threads.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria uma fábrica de sessões (SessionLocal) que será usada para criar
# sessões de banco de dados para cada requisição.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria uma classe base para nossos modelos ORM.
Base = declarative_base()