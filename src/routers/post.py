from fastapi import APIRouter

router = APIRouter()


@router.get("/all")
async def get_all_posts():
    pass


@router.get("/{post_id}")
async def get_post_by_id(post_id: int):
    pass


@router.post("/", status_code=204)
async def create_post():
    pass


@router.put("/{post_id}", status_code=204)
async def update_post(post_id: int):
    pass


@router.delete("/{post_id}", status_code=204)
async def delete_post(post_id: int):
    pass
