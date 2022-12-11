# For the app
from flask import Blueprint, render_template, request
# Redis Database
from app_redis import rd
# Functions
from app_functions import get_user_session

# Blueprint for home
app_home = Blueprint(__name__, "app_home")


# Home
@app_home.get("/")
def get_home():
    # Request from HTMX or not
    render_music_player = not request.headers.get('Hx-Request')

    # Render hole page (and MusicPlayer)
    return render_template(
        "home.html",
        render_music_player=render_music_player,
        user_in_session=get_user_session(request.cookies.get('session_token'))
    )
