from fastapi import APIRouter
from routers.account import router as account
from routers.post import router as post
from routers.like import router as like

router = APIRouter(prefix="/api")
router.include_router(account, prefix="/account", tags=["Account"])
router.include_router(post, prefix="/post", tags=["Post"])
router.include_router(like, prefix="/like", tags=["Like"])
