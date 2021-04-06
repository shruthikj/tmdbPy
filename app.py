from flask import Flask, render_template, url_for, request, redirect, flash
import sqlite3
from flask_bootstrap import Bootstrap
from tmdbv3api import TMDb, Movie, Discover
from flask_cors import CORS, cross_origin
from forms import SignupForm, LoginForm
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
# from models import User

app = Flask(__name__)
app.config.from_pyfile('config.py')

CORS(app)
bootstrap = Bootstrap(app)

conn = sqlite3.connect('TMDB.db')
c = conn.cursor()

# TODO: DB setup

# login_manager = LoginManager(app)
# login_manager.login_view = "login"

# class TMDBMovies(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     viewed = db.Column(db.String(200))
#     searched = db.Column(db.String(200))
#     accessed_date = db.Column(db.DateTime, default=datetime.utcnow)

tmdb = TMDb()
tmdb.api_key = 'fcb5a65588c46fdc758a49ac9ce15525'
tmdb.language = 'en'
tmdb.debug = True
movies = Movie()
discover = Discover()

popular_movies = movies.popular()
    
new_releases = discover.discover_movies({
    'primary_release_date.gte': '2020-01-01',
    'primary_release_date.lte': '2020-12-30'
})
title = 'Home - Popular Movies'

@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('index.html',
                                title = title, 
                                popular = popular_movies,
                                new_releases = new_releases)

@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():
    
       
    if request.method == 'POST':
        print(request.form.get('searchMovie'))
        search_query = request.form.get('searchMovie')

        search = movies.search(search_query)
        similar = movies.similar(search[0].id)

        recommendations = movies.recommendations(movie_id = search[0].id)
        if search_query:
            return render_template('index.html', 
                                    search_movie = search, 
                                    similar = similar,
                                    title = title, 
                                    popular = popular_movies,
                                    new_releases = new_releases,
                                    recommendations = recommendations)
    else:     
        return render_template('index.html',
                                title = title, 
                                popular = popular_movies,
                                new_releases = new_releases)

# @app.route('/autosearch', methods=['POST', 'GET'])
# def autoSearch():
#         print("autosearchautosearchautosearchautosearchautosearch")
#         search_query = request.form.get('autosearch')

#         SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
#         json_url = os.path.join(SITE_ROOT, "data", "results.json")
#         json_data = json.loads(open(json_url).read())
#         print(search_query)
#         search = movies.search(search_query)
#         print(search_query)
#         filtered_dict = [v for v in json_data if search_query in v]	
#         print(filtered_dict)
        
#         resp = jsonify(filtered_dict)
#         resp.status_code = 200
#         return resp

@app.route("/movie/<int:id>")
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = movies.details(id)
    title = f'{movie.title}'
    # reviews = Review.query.filter_by(movie_id = id).all()
    return render_template('index.html',
                            id = id, 
                            title = title,
                            movie = movie,
                            )


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Standard `signup` form."""
    form = SignupForm()

    # if form.validate_on_submit():
    #     existing_user = User.query.filter_by(email=form.email.data).first()
    #     if existing_user is None:
    #         user = User(
    #             name=form.name.data,
    #             email=form.email.data,
    #         )
    #         user.set_password(form.password.data)
    #         db.session.add(user)
    #         db.session.commit()  # Create new user
    #         login_user(user)  # Log in as newly created user
    #         return redirect(url_for('homepage'))
    #     flash('A user already exists with that email address.')

    return render_template(
        'signup.html',
        title='Create an Account.',
        form=form,
        template='form-template',
        body="Sign up for a user account."
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    """Standard `login` form."""
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "login.html",
        form=form,
        template="form-template"
    )

if __name__ == "__main__":
    app.run(debug=True)
