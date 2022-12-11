# For the app
from flask import Blueprint, render_template, request
# Functions
from app_functions import get_user_session

# Blueprint for home
app_search = Blueprint(__name__, "app_search")


# User
@app_search.get("/search/")
def get_search():
    # Request from HTMX or not
    render_music_player = not request.headers.get('Hx-Request')


    # Render hole page (and MusicPlayer)
    return render_template(
        "search.html",
        user_search = request.args.get('search'),
        render_music_player=render_music_player,
        user_in_session=get_user_session(request.cookies.get('session_token'))
    )
        