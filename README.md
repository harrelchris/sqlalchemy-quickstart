# SQLAlchemy Quickstart

Get started with SQLAlchemy and Alembic

## Alembic init

1. Create Alembic files

    ```shell
    alembic init alembic
    ```

1. Update `alembic/env.py`

    ```python
    from app import database, settings
    
    ...
    
    config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
    
    ...
    
    target_metadata = database.Base.metadata
    ```

1. Create migration

    ```shell
    alembic revision --autogenerate -m "Autogenerate"
    ```

1. Apply migration

    ```shell
    alembic upgrade head
    ```

## Development

All models must be imported into `app/database.py` for autogenerate to work.

## Usage

```shell
bash scripts/init.sh
bash scripts/run.sh
```
