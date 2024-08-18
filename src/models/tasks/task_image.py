from uuid import uuid4

from sqlalchemy import ForeignKey, String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from common.db.postgres.base import PostgresBaseModel
from models.tasks.ext import TASKS_SCHEMA


class TaskImage(PostgresBaseModel):
    __tablename__ = "task_image"
    __table_args__ = {
        "schema": TASKS_SCHEMA,
    }

    sid: Mapped[int] = mapped_column(UUID, primary_key=True, default=uuid4)
    path: Mapped[str] = mapped_column(String)

    task: Mapped[UUID | None] = mapped_column(
        ForeignKey(f"{TASKS_SCHEMA}.task.sid", ondelete="CASCADE"), index=True
    )
