# For the app
from flask import Blueprint, send_file
# Global variables
from global_vars import *

# Blueprint for home
app_songs = Blueprint(__name__, "app_songs")


# Send music file
@app_songs.get("/songs/<string:song_name>")
def get_song(song_name):
    return send_file(f"{BASE_SERVER_DIRECTORY}/songs/{song_name}", mimetype="audio/mp3")

