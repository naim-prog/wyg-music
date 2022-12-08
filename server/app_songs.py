# For the app
from flask import Blueprint, send_file, request, render_template, flash
# Global variables
from global_vars import *

# Blueprint for home
app_songs = Blueprint(__name__, "app_songs")


# Send music file
@app_songs.get("/songs/<string:song_name>")
def get_song(song_name):
    return send_file(f"{BASE_SERVER_DIRECTORY}/songs/{song_name}", mimetype="audio/mp3")


# Upload a song (GET PAGE)
@app_songs.get("/upload/")
def get_upload():

    # Request from HTMX
    if request.headers.get('Hx-Request'):
        return render_template(
            "upload.html",
            render_music_player=False
        )

    # Render hole page (and MusicPlayer)
    return render_template(
        "upload.html",
        render_music_player=True
    )
    

# Upload a song (POST PAGE)
@app_songs.post("/upload/")
def post_upload():

    # List of files uploaded
    file_list = request.files.get('song-files')

    # There is no song dropped but he push "upload" button
    if file_list == None:
        flash("You need to upload at least 1 song")
        return render_template(
            "upload.html",
            render_music_player=False
        )

    # If there are songs
    print(request.files.get('song-files'))