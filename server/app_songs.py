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
    # Request from HTMX or not
    render_music_player = not request.headers.get('Hx-Request')


    # Render hole page (and MusicPlayer)
    return render_template(
        "upload.html",
        render_music_player=render_music_player
    )
    

# Upload a song (POST PAGE)
@app_songs.post("/upload/")
def post_upload():
    # Request from HTMX or not
    render_music_player = not request.headers.get('Hx-Request')

    # List of files uploaded
    file_list = request.files.getlist('song-files')

    """
    SONG TYPE OF NAME:
    Artist Name - Name of Song.mp3
    """

    # There is no song dropped but he push "upload" button
    if file_list == None:
        flash("You need to upload at least 1 song")
        return render_template(
            "upload.html",
            render_music_player=render_music_player
        )

    any_error_file = False
    list_error_names = []

    # Iterate through all the songs
    for file in file_list:
        # If name file is correct save the file
        if song_name_is_correct(file.filename):
            file.save(os.path.join(SONGS_DIRECTORY, new_song_name(file.filename)))
        else:
            any_error_file = True
            list_error_names.append(file.filename)

    # If there has been any error notificate
    if any_error_file:
        flash("There has been an error with the next song names")
        
        # The the song name that contain errors
        for song_name in list_error_names:
            flash(song_name)
        
        # Return the upload page to reupload the songs
        return render_template(
            "upload.html",
            render_music_player=render_music_player
        )
        
    # All songs uploaded correctly
    flash("All songs uploaded correctly")
    return render_template(
        "upload.html",
        render_music_player=render_music_player
    )




# ----------------------------- FUNCTIONS -----------------------------

def song_name_is_correct(song_name: str):
    
    # Is not an mp3 file
    if not song_name.endswith('.mp3'):
        return False
    
    # If the song doesn't have ' - ' there is no artist or song name
    if song_name.find(' - ') == -1:
        return False

    return True


def new_song_name(song_name: str):
    """
    If the artist is in the database
        set the artist name exactly the same
    if is not in the database
        add the artist in the database
    """
    return song_name