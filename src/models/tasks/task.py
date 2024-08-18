from uuid import uuid4

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from common.db.postgres.base import PostgresBaseModel
from models.tasks.ext import TASKS_SCHEMA


class Task(PostgresBaseModel):
    __tablename__ = "task"
    __table_args__ = {
        "schema": TASKS_SCHEMA,
    }

    sid: Mapped[int] = mapped_column(UUID, primary_key=True, default=uuid4)
