from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_ADDR: str = 'localhost'
    DB_PORT: int = 5432
    DB_USERNAME: str = "postgres"
    DB_PASSWORD: str = "blog_postgres"
    DB_NAME: str = "blog"

    SERVER_ADDR: str = "localhost"
    SERVER_PORT: int = 8000
    SERVER_TEST: bool = False


settings = Settings()
