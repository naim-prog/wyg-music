# Obvioulsy we need to import this, look at the filename
import redis
# For app config parameters
from app_conf import *
# Hash the admin password
from hashlib import sha512

# Instance of the RedisDB
rd = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DATABASE,
    username=REDIS_USERNAME,
    password=REDIS_PASSWORD
)

def init_redis_server():
    # If first time, add admin user and password
    rd.hsetnx('users', REDIS_ADMIN_USERNAME, sha512(REDIS_ADMIN_PASSWORD.encode('utf-8')).hexdigest())

"""
                REDIS DATABASES

REDIS:0 (users)
{
    # hash
    'users': {
        'user1': 'password1(hashed)',
        'user2': 'password2(hashed)'
    },
    # key
    'user_session': 'user_session_token' -> expire seconds
    
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