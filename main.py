from fastapi import FastAPI
from uuid import UUID, uuid4
from typing import List
from models import User, Gender, Role

app = FastAPI()

db: List[User]=[
    User(
        id=uuid4(),
        first_name="Praneeth", 
        last_name="Settipalli",
        gender = Gender.male,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Vinusha", 
        last_name="Settipalli",
        gender = Gender.female,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "User"}

@app.get("/api/v1/users")
async def fetch_users():
    return db
