# SQLAlchemy

Starter code for using SQLAlchemy in Python projects.

## Links

1. https://docs.sqlalchemy.org/
1. https://alembic.sqlalchemy.org/
1. https://github.com/absent1706/sqlalchemy-mixins
1. https://github.com/theskumar/python-dotenv

## Database Initialization

```shell
alembic -c app/migrations/alembic.ini revision --autogenerate
alembic -c app/migrations/alembic.ini upgrade head
```

## Notes

- Models must be discoverable by autogenerate - import the modules into `app.migrations.env`
