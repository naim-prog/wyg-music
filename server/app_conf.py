# Keep this file secure, here you will include all sensitive
# information about diferent configurations on your app

# --------------- APP ---------------

APP_HOST = "0.0.0.0"

APP_PORT = 80

# -------------- REDIS --------------

REDIS_HOST = "localhost"

REDIS_PORT = 6379

REDIS_DATABASE = 0

REDIS_USERNAME = "default"

REDIS_PASSWORD = ""

REDIS_ADMIN_USERNAME = "admin"

REDIS_ADMIN_PASSWORD = "secure-password-for-admin"

REDIS_USERS_DATABASE   = 0
REDIS_SONGS_DATABASE   = 1
REDIS_ARTISTS_DATABASE = 2

# 3 days of session expire time
REDIS_USER_SESSION_EXPIRE_TIME = 60 * 60 * 24 * 3