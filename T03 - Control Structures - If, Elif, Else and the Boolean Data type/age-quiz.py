import sys

print("Please insert your age: ")
age = input()
try: # we try to convert the inputted string to an integer. If there are any errors then a ValueError is returned.
    age = int(age)
except ValueError: # in this case we return a printed error message and exit the program
    print("Please enter an integer value")
    sys.exit(0)
if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else: print("Age is but a number.")