from databases.sql_db import session
from databases.decorators import with_session
from sqlalchemy.future import select
import datetime
from .models import User


@with_session(session)
async def user_exists(s, id=None, email=None):
    if id:
        exists_query = select(User).where(User.id == id).exists()
    elif email:
        exists_query = select(User).where(User.email == email).exists()
    else:
        raise ValueError('You must pass "id" or "email" parameter')

    query = await s.execute(select(User).where(exists_query))
    return query.first()


@with_session(session)
async def get_user(s, id=None, email=None):
    if id:
        query = select(User).where(User.id == id)
    elif email:
        query = select(User).where(User.email == email)
    else:
        raise ValueError('You must pass "id" or "email" parameter')

    query = await s.execute(query)
    return query.scalars().first()


@with_session(session)
async def create_user(s, user):
    new_user = User(**user.dict())
    new_user.set_password(user.password) 

    s.add(new_user)
    await s.commit()
    await s.refresh(new_user)

    return new_user


@with_session(session)
async def update_user(s, id=None, user=None):
    if not id or not user:
        raise ValueError('You must pass "id" and "user" parameter')
    
    current_user = await get_user(id=id)

    if user.full_name:
        current_user.full_name = user.full_name
    if user.email:
        current_user.email = user.email
    if user.password:
        current_user.set_password(user.password)

    current_user.update_date = datetime.datetime.now()

    await s.flush()
    await s.commit()

    return current_user


