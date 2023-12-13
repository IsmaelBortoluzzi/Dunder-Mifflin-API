from databases.sql_db import session
from databases.decorators import with_session
from sqlalchemy.future import select
from passlib.hash import pbkdf2_sha256 as sha256

from .models import User


@with_session(session)
async def user_exists(s, id=None, email=None):
    if id:
        exists_query = select(User).where(User.id == id).exists()
    elif email:
        exists_query = select(User).where(User.email == email).exists()
    else:
        raise ValueError('You must pass "id" or "email" parametar')

    query = await s.execute(select(User).where(exists_query))
    return query.first()


@with_session(session)
async def create_user(s, user):
    new_user = User(**user.dict())
    new_user.password = sha256.hash(user.password, rounds=3000, salt_size=16)

    s.add(new_user)
    await s.commit()
    await s.refresh(new_user)

    return new_user

