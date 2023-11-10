from fastapi import APIRouter

router = APIRouter()


@router.post("/{post_id}", status_code=204)
async def add_like(post_id: int):
    pass


@router.delete("/{post_id}", status_code=204)
async def delete_like(post_id: int):
    pass
