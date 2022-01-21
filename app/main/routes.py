from crypt import methods
from app.main import blueprint
from app.main.forms import TestForm
from flask import render_template, request

@blueprint.route('/')
def index():
    return render_template("main/index.html", greeting="Welcome to flask project template")

@blueprint.route('/test')
def test():
    return "We can return strings."

@blueprint.route('/post-test', methods=["GET", "POST"])
def form_test():
    if request.method == "GET":
        context = {
            "message": "You sent a GET!",
            "suggestion": "Try sending a POST...", 
            "method": request.method
        }
        return render_template("main/post-test.html", **context)
    elif request.method == "POST": # This could just be an else because only GET and POST are allowed
        context = {
            "message": "You sent a POST!",
            "suggestion": "Try sending a GET...", 
            "method": request.method
        }
        return render_template("main/post-test.html", **context)


@blueprint.route('/form-test', methods=["GET", "POST"])
def post_test():
    form = TestForm()
    if form.validate_on_submit():
        return render_template("main/form-test-success.html", name=form.name.data)
    else:
        return render_template("main/form-test.html", form=form)