# Loja de Ingressos API

Esta API fornece endpoints para gerenciar usuários em uma loja de ingressos online.  Ela é construída com FastAPI e SQLAlchemy, utilizando um banco de dados relacional.

## Funcionalidades

* **Gerenciamento de Usuários:**
    * Criar novos usuários
    * Listar usuários
    * Obter detalhes de um usuário específico
    * Atualizar informações de um usuário
    * Deletar um usuário

## Tecnologias Utilizadas

* **FastAPI:** Framework web de alta performance para construir APIs com Python.
* **SQLAlchemy:**  ORM (Object-Relational Mapper) para Python que facilita a interação com o banco de dados.
* **Python:** Linguagem de programação principal.

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/aaolive/loja-ingressos-api.git
```

2. Navegue até o diretório do projeto:

```bash
cd loja-ingressos-api
```

3. Crie um ambiente virtual (recomendado):

```bash
python3 -m venv .venv
```

4. Ative o ambiente virtual:

```bash
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate  # Windows
```

5. Instale as dependências:

```bash
pip install -r requirements.txt
```

6. Bando de dados já configurado para usar sqlite:

O banco de dados já está configurado para usar sqlite. Você pode acessar o arquivo de configuração do banco de dados em `app/database.py`.

7. Inicie o servidor de desenvolvimento:

```bash
uvicorn app.main:app --reload
```

## Endpoints

| Método | Rota                | Descrição                                      |
|--------|---------------------|-----------------------------------------------|
| POST   | `/usuarios/`        | Cria um novo usuário.                         |
| GET    | `/usuarios/`        | Lista todos os usuários.                      |
| GET    | `/usuarios/{id}`    | Retorna os detalhes de um usuário específico. |
| PUT    | `/usuarios/{id}`    | Atualiza um usuário existente.                |
| DELETE | `/usuarios/{id}`    | Deleta um usuário.                            |


## Próximos Passos

* Implementar endpoints para gerenciamento de eventos.
* Implementar endpoints para gerenciamento de ingressos.
* Implementar endpoints para compra de ingressos.
* Adicionar autenticação e autorização.
* Implementar testes unitários e de integração.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.


## Licença

[MIT](LICENSE)
