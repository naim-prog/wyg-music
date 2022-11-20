# For the hole app
from flask import Flask, render_template, send_file
# Secret key app
import secrets
# Global variables
from global_vars import *

app = Flask(__name__)

app.secret_key = secrets.token_hex(32)

# Home
@app.get("/")
def home():
    return render_template(
        "base.html"
    )


# Send music file
@app.get("/songs/<string:song_name>")
def get_song(song_name):
    return send_file(f"{BASE_SERVER_DIRECTORY}/songs/{song_name}", mimetype="audio/mp3")


if __name__ == "__main__":
    # Run the app
    app.run(host="0.0.0.0")