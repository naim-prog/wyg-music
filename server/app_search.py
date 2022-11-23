# For the app
from flask import Blueprint, render_template, request, send_file, render_template_string

# Blueprint for home
app_search = Blueprint(__name__, "app_search")


# User
@app_search.get("/search/")
def get_search():
    print(request.args.get('search'))
    # Render only body container
    if request.headers.get('Ajax-Render'):
        return render_template_string(
            open("templates/search").read(),
            user_search = request.args.get('search')
        )

    print("render")
    # Render hole page
    return render_template(
        "search.html",
        user_search = request.args.get('search')
    )
        
