from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import Address, User, engine

# Create
with Session(engine) as session:
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )

    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )

    patrick = User(name="patrick", fullname="Patrick Star")

    session.add_all([spongebob, sandy, patrick])
    session.commit()

# Read
with Session(engine) as session:
    stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
    for user in session.scalars(stmt):
        print(user)
