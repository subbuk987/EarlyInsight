from fastapi import FastAPI
import models
from database import engine,sessionlocal
from schemas import user

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get('/')
def test():
    return 'Hello World'

@app.post('/login')
def login(user_details : user):
    return user_details
