from fastapi import FastAPI
from service1.routers import ping_router

app = FastAPI()
app.include_router(ping_router.router)