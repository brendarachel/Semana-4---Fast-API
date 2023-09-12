from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("639ac80e-42ec-4030-bc6d-8f29c0dc8b14"), 
         first_name="Ana", 
         last_name="Maria", 
         email="maria@gmail.com", 
         role=[Role.role_1]
    ),
    User(
        id=UUID("581e999b-f8cb-4ab6-9beb-84b763d3ebf4"), 
         first_name="Cynthia", 
         last_name="Zanoni", 
         email="zanoni@gmail.com", 
         role=[Role.role_2]
    ),
    User(
        id=UUID("ee96ccab-0dfe-4b51-b35e-6f60e7dd7bd6"), 
         first_name="Camila", 
         last_name="Silva", 
         email="camila@gmail.com", 
         role=[Role.role_3]
    ),
]

@app.get("/")
async def root():
    return {"message": "Olá, WoMakers!"}

@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado!"}

@app.post("/api/users")
async def add_user(user: User):
    """
    Adiciona um usuário na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    """
    db.append(user)
    return {"id": user.id}

#EXERCÍCIO: crie uma função assíncrona de http put requests, 
# criando e passando a rota se necessário

@app.put("/api/users/{id}")
async def update_user(id: UUID, dados: User):
    """
    Atualiza um registro existente na base de dados.
    """
    for user in db:
        if user.id == id:
            user.first_name = dados.first_name
            user.last_name = dados.last_name
            user.email = dados.email
            user.role = dados.role
            return {"message": "Usuário atualizado com sucesso!"}
        
    raise HTTPException(
        status_code = 404,
        detail = f"Usuário com id {id} não encontrado!"
    )

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail = f"Usuário com id {id} não encontrado!"
    )

