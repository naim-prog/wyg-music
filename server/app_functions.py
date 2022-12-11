# Here will go the functions that will be needed to run
# multiple times for many files

# Redis Database
from app_redis import rd


# Return the user how has this token
# or None if this token doesnt exist
def get_user_session(cookie_token):
    user_in_session = None

    # If this session_token exists get the user; if not None
    if cookie_token:
        user_in_session = rd.get(cookie_token).decode('utf-8')

    return user_in_session