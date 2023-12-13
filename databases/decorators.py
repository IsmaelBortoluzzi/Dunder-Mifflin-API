from functools import wraps


def with_session(session_maker):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            async with session_maker() as session:
                return await func(session, *args, **kwargs)
        return wrapper
    return decorator

