# For the hole app
from flask import Flask, render_template, send_file, request
# Secret key app
import secrets
# Global variables
from global_vars import *

# For blueprints
from app_home       import app_home
from app_user       import app_user
from app_songs      import app_songs
from app_search     import app_search

# Init of app
app = Flask(__name__)

# Secret key for sessions
app.secret_key = secrets.token_hex(32)

# Register diferents blueprints from files
app.register_blueprint(app_home)
app.register_blueprint(app_user)
app.register_blueprint(app_songs)
app.register_blueprint(app_search)


# Main app
if __name__ == "__main__":
    # Run the app
    app.run(host="0.0.0.0", debug=True)