from fastapi import APIRouter, Depends

from models.account import Account
from db import get_database, Session

router = APIRouter()

@router.get("/")
async def get_users(db: Session = Depends(get_database)):
    query = db.query(Account).all()
    return []
