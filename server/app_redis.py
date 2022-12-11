# Obvioulsy we need to import this, look at the filename
import redis
# For app config parameters
from app_conf import *


# Instance of the RedisDB
rd = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DATABASE,
    username=REDIS_USERNAME,
    password=REDIS_PASSWORD
)

"""
                REDIS DATABASES

REDIS:0 (users)
{
    # hash
    'users': {
        'user1': 'password1(hashed)',
        'user2': 'password2(hashed)'
    },
    # hash
    'session_users': {
        'user1': 'user1_session_token(hashed)',
    }
    # set
    'session_tokens': (
        'user1_session_token(hashed)' -> EXPIRE 36000 secs
    )
}
REDIS:1 (songs)
{
    # hash
    'artist_name - song_name': {
        'duration': time_in_seconds
    }
}
REDIS:2 (artists)
{
    # set
    'artist_name': (
        'song_name'
    )
}
"""