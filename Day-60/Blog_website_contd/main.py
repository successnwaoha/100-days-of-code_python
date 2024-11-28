from flask import Flask, render_template, request
import requests
import smtplib
import os

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

SENDER_EMAIL = os.getenv("sender_email")
RECEIVER_EMAIL = os.getenv("reveiver_email")
PASSWORD = os.getenv("password")

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",  methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        sender_name = data["name"]
        sender_email = data["email"]
        sender_phone_number = data["phone"]
        sender_message = data["message"]
        send_email(sender_name, sender_email, sender_phone_number, sender_message)
        return render_template("contact.html", msg_sent = True)
    return render_template("contact.html", msg_sent = False)

def send_email(name, email, phone_number, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone_number}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(SENDER_EMAIL, PASSWORD)
        connection.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, email_message)
    

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
