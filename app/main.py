from fastapi import FastAPI
from app.database import engine, Base
from app.models import user # import models
from app.routes import auth
from app.models import ticket 
from app.routes import tickets
from app.routes import admin

Base.metadata.create_all(bind=engine) # create tables


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Ticket System API Running 🚀"}


app.include_router(auth.router)


app.include_router(tickets.router)


app.include_router(admin.router)

