from fastapi import FastAPI
from app.presentation.routes import router

app = FastAPI(title="GazaCare + DigiEmu")

app.include_router(router)