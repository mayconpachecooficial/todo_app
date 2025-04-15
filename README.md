# API de Gerenciamento de Tarefas (To-Do)

Esta é uma API RESTful construída com **FastAPI** e **SQLite** para gerenciar tarefas.

## Funcionalidades

- Criar tarefas
- Listar tarefas (com filtro por status e paginação)
- Atualizar apenas o status (pendente/concluída)
- Deletar tarefas
- Autenticação via token fake no header
- Testes automatizados com pytest
- Dockerfile para execução

## Requisitos

- Python 3.9+
- Docker(opcional)


## Como rodar localmente

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar a API
uvicorn app.main:app --reload
