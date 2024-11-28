from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

API_KEY = "b15fac16da9ce3025d16fa5453127d46"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

# CREATE DB

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies_database.db"
db = SQLAlchemy(model_class = Base)
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=True)
    ranking: Mapped[str] = mapped_column(Float, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=True)
    
class RateMovieForm(FlaskForm):
    rating = StringField("Your rating out of 10 e.g 7.5")
    review = StringField("Your review")
    submit = SubmitField("Done")
    
class FindMovieForm(FlaskForm):
    title = StringField("Movie Tile", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

with app.app_context():
    db.create_all()


# # CREATE TABLE
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Stu Shepard, a publicist, finds himself in a nightmarish situation when he answers a ringing phone at a phone booth. The mysterious caller threatens to shoot him if he cuts the call.",
#     rating=7.3,
#     ranking=10,
#     review="My favorite movie test text",
#     img_url="https://cdn11.bigcommerce.com/s-yshlhd/images/stencil/1280x1280/products/7969/158980/full.phonebooth-16598__96641.1556888804.jpg?c=2?imbypass=on"
# )

# second_movie = Movie(
#     title="Naruto",
#     year=2007,
#     description="Naruto is a Japanese manga series written and illustrated by Masashi Kishimoto. It tells the story of Naruto Uzumaki, a young ninja who seeks recognition from his peers and dreams of becoming the Hokage, the leader of his village.",
#     rating=9.3,
#     ranking=1,
#     review="My favorite movie test text",
#     img_url="https://cdn.staticneo.com/w/naruto/Nprofile2.jpg"
# )

# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    
    return render_template("index.html", movies = all_movies)


@app.route('/edit', methods = ["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route('/delete')
def delete_movie():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods = ["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={
                                "api_key": API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)

@app.route('/find')
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key":API_KEY, "language":"en-US"})
        data = response.json()
        new_movie = Movie(
            title = data["title"],
            year = data["release_date"].split("-")[0],
            img_url = f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description = data["overview"],
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
    