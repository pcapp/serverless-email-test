from fastapi import FastAPI
from api import mail


app = FastAPI()
app.include_router(mail.router)
