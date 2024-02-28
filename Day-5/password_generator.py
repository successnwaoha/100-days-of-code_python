import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
input_letters= int(input("How many letters would you like in your password?\n")) 
input_symbols = int(input(f"How many symbols would you like?\n"))
input_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, input_letters + 1):
    random_character = random.choice(letters)
    password_list += random_character

for char in range(1, input_symbols +1):
    random_character = random.choice(symbols)
    password_list += random_character

for char in range(1, input_numbers +1):
    random_character = random.choice(numbers)
    password_list += random_character

random.shuffle(password_list)
print(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your pass is: {password}")