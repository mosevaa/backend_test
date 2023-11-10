import uvicorn
from settings import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.initdb import initdb
from routers import router

app = FastAPI(debug=settings.SERVER_TEST)
app.include_router(router)

origins = [

]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

initdb()
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.SERVER_ADDR,
        port=settings.SERVER_PORT,
        reload=settings.SERVER_TEST
    )
