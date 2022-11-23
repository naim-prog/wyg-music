# For the app
from flask import Blueprint, render_template, request, send_file

# Blueprint for home
app_home = Blueprint(__name__, "app_home")


# Home
@app_home.get("/")
def home():
    
    # Render only body container
    if request.headers.get('Ajax-Render'):
        return send_file(
            "templates/home"
        )

    # Render hole page
    return render_template(
        "home.html"
    )
