from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from app.models import Task

client = TestClient(app)

token_header = {"x-token": "123456"}

# Recria o banco antes dos testes
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_criar_tarefa():
    response = client.post("/tasks/", json={
        "titulo": "Tarefa Teste",
        "descricao": "Testando criação"
    }, headers=token_header)
    assert response.status_code == 200
    assert response.json()["titulo"] == "Tarefa Teste"

def test_listar_tarefas():
    response = client.get("/tasks/", headers=token_header)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_filtrar_por_status():
    response = client.get("/tasks/?status=pendente", headers=token_header)
    assert response.status_code == 200

def test_alterar_status():
    # Cria uma tarefa
    post_response = client.post("/tasks/", json={
        "titulo": "Atualizar Status",
        "descricao": "Teste update"
    }, headers=token_header)
    task_id = post_response.json()["id"]

    patch_response = client.patch(f"/tasks/{task_id}", json={
        "status": "concluida"
    }, headers=token_header)

    assert patch_response.status_code == 200
    assert patch_response.json()["status"] == "concluida"

def test_deletar_tarefa():
    response = client.post("/tasks/", json={
        "titulo": "Tarefa para Deletar",
        "descricao": "Teste delete"
    }, headers=token_header)
    task_id = response.json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}", headers=token_header)
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Tarefa removida com sucesso"
