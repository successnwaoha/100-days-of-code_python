from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random


app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    
    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods = ["GET"])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(Cafe=random_cafe.to_dict())

@app.route("/all", methods = ["GET"])
def get_all_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    dictionary = []
    for item in all_cafes:
        cafe = item.to_dict()
        dictionary.append(cafe)
    return jsonify(Cafe=dictionary)

@app.route("/search")
def search_cafe():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry we don't have a cafe at that location."}), 404

@app.route("/add", methods = ["POST"])
def add_cafe():
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        seats = request.form.get("seats"),
        has_toilet = bool(request.form.get("toilet")),
        has_wifi = bool(request.form.get("wifi")),
        has_sockets = bool(request.form.get("sockets")),
        can_take_calls = bool(request.form.get("calls")),
        coffee_price = request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response = {"success":"Successfully added the new cafe."})

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record
@app.route("/update_price/<int:cafe_id>", methods = ["PATCH"])
def update_price(cafe_id):
    # result = db.session.execute(db.select(Cafe))
    new_price = request.args.get("new_price")
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response = {"success": "Successfully added the new price."}), 200
    else:
        return jsonify(response = {"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404
        
# HTTP DELETE - Delete Record
@app.route("/report_closed/<int:cafe_id>", methods = ["DELETE"])
def delete_cafe(cafe_id):
    # result = db.session.execute(db.select(Cafe))
    api_key = request.args.get("api_key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.get(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response = {"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(response = {"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(response = {"forbidden": "Sprry, that's not allowed. Make sure you have the correct api key."}), 403


if __name__ == '__main__':
    app.run(debug=True)



# "id": random_cafe.id,
# "name": random_cafe.name,
# "map_url": random_cafe.map_url,
# "img_url": random_cafe.img_url,
# "location": random_cafe.location,
# "seats": random_cafe.seats,

# #Put some properties in a sub category
# "amenities": 
# "has_toilet": random_cafe.has_toilet,
# "has_wifi": random_cafe.has_wifi,
# "has_sockets": random_cafe.has_sockets,
# "can_take_calls": random_cafe.can_take_calls,
# "coffee_price": random_cafe.coffee_price,
        