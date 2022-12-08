# For the app
from flask import Blueprint, render_template, request, flash
# For user login and register
from app_redis import rd


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
    # No music player (If is not logged we cannot let them reproduce songs)
    render_music_player = False

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
"""

# Login (POST PAGE)
@app_user.post("/login/")
def post_login():
    # No music player (If is not logged we cannot let them reproduce songs)
    render_music_player = False
    
    """
    form: {
        user: user,
        password: password
    }
    """

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
    if not rd.sismember('users', request.form.get('user')):
        flash("User or password dont match")
    """
    rd.sadd()