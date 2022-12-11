# For the app
from flask import Blueprint, render_template, request, flash, redirect, make_response
# For user login and register
from app_redis import rd
# For session tokens
import secrets
# Hashing passwords
from hashlib import sha512
# To select Redis Database
from app_conf import REDIS_USERS_DATABASE, REDIS_USER_SESSION_EXPIRE_TIME
# Functions
from app_functions import get_user_session

# Blueprint for home
app_user = Blueprint(__name__, "app_user")


# User profile
@app_user.get("/user/<string:user>/")
def get_user(user):
    # Request from HTMX or not
    render_music_player = not request.headers.get('Hx-Request')

    # Render hole page
    return render_template(
        "user.html",
        render_music_player=render_music_player,
        user_in_session=get_user_session(request.cookies.get('session_token'))
    )


# Login (GET PAGE)
@app_user.get("/login/")
def get_login():
    # Request from HTMX or not
    render_music_player = not request.headers.get('Hx-Request')

    # If has cookies redirect home
    if request.cookies.get('session_token'):
        return redirect("/")

    # Render login page
    return render_template(
        "login.html",
        render_music_player=render_music_player
    )


"""
THIS IS HELPFULL FOR LOGIN AND REGISTER
SADD 	    Adds the item to the set
SMEMBERS 	Returns the entire set of items
SISMEMBER 	Checks if an item is in the set
SREM 	    Removes the item from the set, if it exists
HMGET       Get the value of a dictionary
HSET        Set the value for a key in a dictionary
"""

# Login (POST PAGE)
@app_user.post("/login/")
def post_login():
    # Request from HTMX or not
    render_music_player = not request.headers.get('Hx-Request')

    # One or both fields are empty
    if not request.form.get('user') or not request.form.get('password'):
        flash("Please fill user and password fields to succesfully login")
        # Render login page
        return render_template(
            "login.html",
            render_music_player=render_music_player
        )

    # User doesnt exist on the database
    rd.select(REDIS_USERS_DATABASE)
    if not rd.hexists('users', request.form.get('user')):
        flash("User or password dont match")
        return redirect("/login/")

    # Password dont correspond with the one that the user has
    rd.select(REDIS_USERS_DATABASE)
    if rd.hmget('users', request.form.get('user'))[0].decode('utf-8') != sha512(request.form.get('password').encode('utf-8')).hexdigest():
        flash("User or password dont match")
        return redirect("/login/")

    # New token for the user session
    user_session_token = secrets.token_urlsafe(64)

    # We make sure this token doesnt exist
    rd.select(REDIS_USERS_DATABASE)
    while rd.exists(user_session_token):
        user_session_token = secrets.token_urlsafe(64)

    # Set key and expiricy
    rd.set(user_session_token, request.form.get('user'), ex=REDIS_USER_SESSION_EXPIRE_TIME)

    # Response with the cookie to the client
    response = make_response(
        render_template(
            "home.html",
            render_music_player=render_music_player,
            user_in_session=request.form.get('user')
        )
    )

    response.set_cookie(
        key='session_token',
        value=user_session_token,
        max_age=REDIS_USER_SESSION_EXPIRE_TIME,
        expires=REDIS_USER_SESSION_EXPIRE_TIME,
        samesite='Lax'
    )
    
    flash("Successfully login")
    return response

    