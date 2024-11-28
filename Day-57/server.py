from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year = current_year)

@app.route('/guess/<name>')
def guess(name):
    
    agify_url = f"https://api.agify.io?name={name}"
    genderize_url = f"https://api.genderize.io?name={name}"
    
    age_response = requests.get(agify_url)
    gender_response = requests.get(genderize_url)
    
    genderize_data = gender_response.json()
    age_data = age_response.json()
    print(genderize_data)
    print(age_data)
    
    gender = genderize_data["gender"]
    age = age_data["age"]

    return render_template("guess.html", person_name = name, age = age, gender = gender)

@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts = all_posts)

if __name__ == "__main__":
    app.run(debug=True)