# For the app
from flask import Blueprint, render_template, request, send_file, render_template_string

# Blueprint for home
app_search = Blueprint(__name__, "app_search")


# User
@app_search.get("/search/")
def get_search():

    render_music_player=True

    # Se hace la request desde HTMX
    if request.headers.get('Hx-Request'):
        return render_template(
            "search.html",
            user_search = request.args.get('search'),
            render_music_player=False
        )

    # Render hole page
    return render_template(
        "search.html",
        user_search = request.args.get('search'),
        render_music_player=render_music_player
    )
        
