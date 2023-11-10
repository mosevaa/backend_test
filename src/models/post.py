from typing import List
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ARRAY, Integer, ForeignKey, TIMESTAMP, func

from models.base import Base


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    theme: Mapped[str] = mapped_column(nullable=False)
    post_body: Mapped[str] = mapped_column(nullable=False)
    likes: Mapped[List[int]] = mapped_column(ARRAY(Integer), server_default="[]")
    author: Mapped[int] = mapped_column(ForeignKey("account.id"), nullable=False)
    date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False,
                                                 server_default=func.current_timestamp())
