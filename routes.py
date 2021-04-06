from flask import (
    Flask,
    url_for,
    render_template,
    redirect
)
from .forms import SignupForm


app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Standard `signup` form."""
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "signup.jinja2",
        form=form,
        template="form-template"
    )