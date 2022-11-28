# For the app
from flask import Blueprint, render_template, request, send_file

# Blueprint for home
app_home = Blueprint(__name__, "app_home")


# Home
@app_home.get("/")
def get_home():
    
    render_music_player=True

    # Request from HTMX
    if request.headers.get('Hx-Request'):
        return render_template(
            "home.html",
            render_music_player=False
        )

    # Render hole page
    return render_template(
        "home.html",
        render_music_player=render_music_player
    )
