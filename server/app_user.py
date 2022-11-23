# For the app
from flask import Blueprint, render_template, request, send_file

# Blueprint for home
app_user = Blueprint(__name__, "app_user")


# User
@app_user.get("/user/")
def get_user():
    
    # Render only body container
    if request.headers.get('Ajax-Render'):
        return send_file(
            "templates/user"
        )

    # Render hole page
    return render_template(
        "user.html"
    )
        
