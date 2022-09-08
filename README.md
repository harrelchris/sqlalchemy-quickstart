# SQLAlchemy

Starter code for using SQLAlchemy in Python projects.

## Links

1. https://docs.sqlalchemy.org/
1. https://alembic.sqlalchemy.org/
1. https://github.com/absent1706/sqlalchemy-mixins
1. https://github.com/theskumar/python-dotenv

## Database Initialization

- Set `DATABASE_URL` environment variable.
- Models must be discoverable by autogenerate - import the modules into `app.migrations.env`

```shell
alembic -c app/migrations/alembic.ini revision --autogenerate
alembic -c app/migrations/alembic.ini upgrade head
```

## Development

```shell
pip install -r requirements.txt
pre-commit install
pre-commit run --all-files
pytest --cov=. --cov-report=html --html=.reports/pytest.html --self-contained-html
python -m app.main
```
