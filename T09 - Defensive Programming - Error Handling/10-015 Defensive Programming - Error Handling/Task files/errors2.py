# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # added quotations for this is a string (syntax error)
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" # the f was missing from the beginning of the string causing a syntax error. Additionally, the mix up in variable names caused a logical error so I corrected this.

print(full_spec) # added brackets (syntax error)

