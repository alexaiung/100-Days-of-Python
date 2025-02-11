print("Welcome to the tip calculator!")
bill = ""
tip_percentage = ""
n_people = ""

# This checking is needed to avoid errors; it has to be done in each
# variable, checking if it corresponds to the needs of the variable
while not bill.isdecimal():
    bill = input("What was the total bill? ")
    if not bill.isdecimal():
        print("Invalid answer, try again.")

# The only difference here is that we cannot accept other options of percentage
while not tip_percentage in ["10", "12", "15"]:
    tip_percentage = input("How much tip would you like to give? 10, 12, or 15? ")
    if not tip_percentage in ["10", "12", "15"]:
        print("Invalid answer, try again.")

while not n_people.isdecimal():
    n_people = input("How many people to split the bill? ")
    if not n_people.isdecimal():
        print("Invalid answer, try again.")

tip = int(bill) * (int(tip_percentage) / 100) / int(n_people)
print(f"Each person should pay: ${tip:.2f}")