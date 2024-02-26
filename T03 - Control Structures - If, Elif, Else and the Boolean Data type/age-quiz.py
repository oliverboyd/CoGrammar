import sys

print("Please insert your age: ")
age = input()
try: 
    age = int(age)
except ValueError:
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