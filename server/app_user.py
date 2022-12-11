# For the app
from flask import Blueprint, render_template, request, flash
# For user login and register
from app_redis import rd
# For session tokens
import secrets
# Hashing passwords
from hashlib import sha512

# Blueprint for home
app_user = Blueprint(__name__, "app_user")


# User profile
@app_user.get("/user/")
def get_user():
    # Request from HTMX or not
    render_music_player = not request.headers.get('Hx-Request')

    # Render hole page
    return render_template(
        "user.html",
        render_music_player=render_music_player
    )


# Login (GET PAGE)
@app_user.get("/login/")
def get_login():
    # Request from HTMX or not
    render_music_player = not request.headers.get('Hx-Request')

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
    """
    if not rd.hmget('users', request.form.get('user')):
        flash("User or password dont match")
    """

    # Password dont correspond with the one that the user has
    """
    if rd.hmget('users', request.form.get('user')) != hash_password(request.form.get('password')):
        flash("User or password dont match")
    """

    # New token for the 
    user_session_token = secrets.token_urlsafe(64)
    """
    add session_users(user, user_session_token)
    add session_tokens(user_session_token, expire=1day)
    """

    flash("Successfully login")
    return render_template(
        "home.html",
        render_music_player=render_music_player,
        user_in_session="user"
    )

    