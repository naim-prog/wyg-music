# For the app
from flask import Blueprint, render_template, request, send_file

# Blueprint for home
app_user = Blueprint(__name__, "app_user")


# User
@app_user.get("/user/")
def get_user():
    
    render_music_player=True

    # Se hace la request desde HTMX
    if request.headers.get('Hx-Request'):
        return render_template(
            "user.html",
            render_music_player=False
        )

    # Render hole page
    return render_template(
        "user.html",
        render_music_player=render_music_player
    )
        
