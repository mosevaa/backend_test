from db.session import engine
from settings import settings
import models


def initdb():
    models.base.Base.metadata.create_all(engine)
