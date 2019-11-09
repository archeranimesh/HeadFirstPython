from flask import session
from functools import wraps


def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "logged_in" in session:
            print("function name = ", func.__name__)
            return func(*args, **kwargs)
        return "You are NOT Logged in"

    return wrapper
