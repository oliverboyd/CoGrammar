# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # brackets were missing which caused a syntax error.
print ("\n") # indent removed and brackets added which caused syntax error

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # removed "years old" as it produced a logical error. Removed indent to avoid syntax error.
age = int(age_Str) # removed indent to avoid syntax error.
print("I'm " + str(age) + " years old.") # converted to string again to avoid syntax error when concatenating. Removed indent to avoid syntax error. Also added spaces to avoid logical error.

# Variables declaring additional years and printing the total years of age
years_from_now = "3.5" # corrected from 3 to 3.5 since we're looking 3 years and 6 months in the future - logical error. Removed indent to avoid syntax error.
total_years = age + float(years_from_now) # converted years_from_now from string to float. Removed indent to avoid syntax error.

print ("The total number of years:" + str(total_years)) # added brackets to avoid syntax error. Fixed variable name (logical error) and converted variable to string (syntax error)

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = int(total_years * 12) # fixed variable name (logical error)
print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # added brackets (syntax error) and converted variable to string (syntax error)

#HINT, 330 months is the correct answer

