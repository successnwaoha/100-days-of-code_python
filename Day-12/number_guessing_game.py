import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!!")
print("I'm thinkung of a number between 1 and 100")

number_to_choose = random.choice(range(1, 101))
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

print(number_to_choose)
end_game = False
while end_game == False:
    print(f"You have {attempts} attempts remaining to guess the number")
    user_guess = int(input("Make a guess: "))
    if user_guess == number_to_choose:
        print(f"You got it! The answer was {number_to_choose}.")
        end_game = True
    elif user_guess > number_to_choose:
        print("Too high. \nGuess again.")
        attempts -= 1
    elif user_guess < number_to_choose:
        print("Too low. \nGuess again.")
        attempts -= 1
    if attempts == 0:
        print("You have run out of chances, you lose")
        end_game = True