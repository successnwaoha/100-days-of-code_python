from flask import Flask
import random
app = Flask(__name__)

answer = random.randint(0, 9)
print(answer)

@app.route('/')
def display():
    return "<h1>Guess a number between 0 and 9</h1><img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExem5iMDgyc2NqazA2dnU5ODE4MnhseDBoc2NqejFkY2l4OWl4cWJweiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C23cMUqoZdqMg/giphy.gif'>"

@app.route('/<int:guess>')
def guess_number(guess):
    if guess > answer:
        return "<h1 style='color: purple'>Too high, try again!</h1><img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExem5iMDgyc2NqazA2dnU5ODE4MnhseDBoc2NqejFkY2l4OWl4cWJweiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C23cMUqoZdqMg/giphy.gif'>"
    elif guess < answer:
        return "<h1 style='color: red'>Too low, try again!</h1><img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExem5iMDgyc2NqazA2dnU5ODE4MnhseDBoc2NqejFkY2l4OWl4cWJweiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C23cMUqoZdqMg/giphy.gif'>"
    else:
        return "<h1 style='color: green'>You found me!!!</h1><img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExem5iMDgyc2NqazA2dnU5ODE4MnhseDBoc2NqejFkY2l4OWl4cWJweiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C23cMUqoZdqMg/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)