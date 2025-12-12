# creates a dtring with tab character at the beginning
tabby_cat = "\tI'm tabbed in."
# Creates a string split into two lines using the new line escape character
persian_cat = "I'm split\non a line."
# Creates a string that includes a backslash
backslash_cat = "I'm \\ a \\ cat."

# A multiline string using triple quotes
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# Prints the string stored in the variable tabby_cat
print(tabby_cat)
# Prints the string stored in the persian_cat 
print(persian_cat)
# Prints the sting stored in the backslash_cat
print(backslash_cat)
# Prints the multiline string stored in fat_cat
print(fat_cat)

# Asks the user "How old are you?"
# end=' ' keeps the cursor on the same line after printing
print("How old are you?",  end=' ')
## Takes user input and stores it in the variable'age'
age = input()
# Asks the user "How tall are you?"
print("How tall are you?",  end=' ')
# Takes user input and stores it in 'height'
height = input()
# Asks the user "How much do you weigh?"
print("How much do you weigh?", end=' ')
# Takes user input abd stores it in 'weight'
weight = input()

# Displays all the collected information using an f-string
print(f"so, you're {age} old, {height} tall and {weight} heavy")


# Asks the user for their age and store the response in the variabe 'age'
age = input("How old are you? ")
# Asks the user for their height and store the response in the variable 'height'
height = input("How tall are you? ")
# Asks the user for their weight and store the response in the variabble 'weight'
weight = input("How much do you weigh? ") 

# Print a sentence that includes al the collected information using an f-string
print(f"so, you're {age} old, {height} tall and {weight} heavy")