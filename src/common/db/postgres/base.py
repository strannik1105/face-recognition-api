from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import as_declarative

from common.utils.case_converter import CaseConverter


@as_declarative()
class PostgresBaseModel:
    __tablename__ = CaseConverter.to_snake_case(__name__)

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_`%(constraint_name)s`",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )
