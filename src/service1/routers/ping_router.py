from fastapi import APIRouter
from service1.modules import ping_responder

router = APIRouter()


@router.get("/ping")
def get_ping():
    return ping_responder.ping()
