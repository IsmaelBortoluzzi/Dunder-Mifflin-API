from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


SQL_DATABASE_URL = 'sqlite+aiosqlite:///db.db'

engine = create_async_engine(SQL_DATABASE_URL)

session = sessionmaker(
    engine,
    autocommit=False,
    expire_on_commit=False,
    future=True,
    class_=AsyncSession,
)

Base = declarative_base()
