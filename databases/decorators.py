def with_session(func):
    async def wrapper(session, *args, **kwargs):
        async with session() as s:
            return await func(s, *args, **kwargs)
    return wrapper
