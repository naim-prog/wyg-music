# Obvioulsy we need to import this, look at the filename
import redis
# For app config parameters
from app_conf import *


# Instance of the RedisDB
rd = redis.Redis(
    host=REDIS_HOST, 
    port=REDIS_PORT, 
    db=REDIS_DATABASE, 
    password=REDIS_PASSWORD
)
