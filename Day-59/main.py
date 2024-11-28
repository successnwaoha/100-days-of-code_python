from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/63572a2759fb4ea12ba3").json()

app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html", all_posts = posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)