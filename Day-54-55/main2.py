####Day 55

from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route('/treasure')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1><p>This is a paragraph.</p><img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExem5iMDgyc2NqazA2dnU5ODE4MnhseDBoc2NqejFkY2l4OWl4cWJweiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C23cMUqoZdqMg/giphy.gif">'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return"Bye"
    
    
if __name__ == "__main__":
    app.run(debug=True)