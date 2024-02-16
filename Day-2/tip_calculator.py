print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would u like to give? 10, 12, 15? "))
number_of_people = int(input("How many people to split the bill? "))
tip_percentage = tip / 100
percentage = (bill * tip_percentage)
total_bill = bill + percentage
bill_per_person = total_bill / number_of_people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")