from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool, sql

from common.db.postgres import PostgresBaseModel, PostgresDBSchemas
from common.config.config import Config


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
alembic_config = context.config
app_config = Config.get_instance()

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if alembic_config.config_file_name is not None:
    fileConfig(alembic_config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = PostgresBaseModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_url() -> str:
    user = app_config.POSTGRES_USER
    password = app_config.POSTGRES_PASSWORD
    host = app_config.POSTGRES_HOST
    port = app_config.POSTGRES_PORT
    db = app_config.POSTGRES_DB
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return url


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        version_table="alembic_version",
        version_table_schema="public",
        compare_type=True,
        include_schemas=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = alembic_config.get_section(alembic_config.config_ini_section)
    if configuration is None:
        configuration = {}

    if not alembic_config.get_main_option("sqlalchemy.url", None):
        configuration["sqlalchemy.url"] = get_url()

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table="alembic_version",
            version_table_schema="public",
            compare_type=True,
            include_schemas=True,
        )

        for schema in PostgresDBSchemas:
            connection.execute(sql.text(f"CREATE SCHEMA IF NOT EXISTS {schema.value}"))

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
