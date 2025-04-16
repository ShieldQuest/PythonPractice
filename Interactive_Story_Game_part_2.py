import time # This introduces a time delay in the program
# import time is a built-in Python module that provides various time-related functions
    # The time module allows you to work with time-related tasks
        # The time.sleep() function is used to pause the program for a specified number of seconds

# Let assign some Variables
    # Variables are used to store information
        # Lets make an interactive story about a dragon
name = "Bael" # Name of our dragon 
age = 15 # Age of our imaginary dragon
color = "red" # Color of our imaginary dragon


# Let's do an interactive story
print("\nI want you to meet my Dragon!") # \n is used to create a new line
time.sleep(1) # This will pause the program for 1 second
print("His name is", name) # name is a variable that stores the name of our dragon
time.sleep(1) # This will pause the program for 2 seconds
print("He is", age, "years old in dragon years and has", color, "scales.") # age and color are variables that store the age and color of our dragon
time.sleep(3) # This will pause the program for 3 seconds
print("He lives inside the cave behind me.")
time.sleep(1)


print("\nIs he friendly?", end='', flush=True) # end='' prevents a new line after the print statement
# flush=True forces the output to be printed immediately
    # without waiting for the buffer to fill
        # This is useful when you want to see the output right away
            # It adds some suspense
time.sleep(1)
print(".", end='', flush=True)
time.sleep(1)
print(".", end='', flush=True)
time.sleep(1)
print(".", end='', flush=True)
time.sleep(1)
print("Maybe.")
time.sleep(1) 


# Now let's make it fun and interactive!
print("\n")
your_name = input("What is your name, brave adventurer? ") # This will ask the user for their name
# The input function will wait for the user to type something and press Enter
    # The input will be stored in the variable your_name


time.sleep(1)
print("\nNice to meet you,", your_name,"!")
time.sleep(1)
print("I hope you like dragons!")
time.sleep(2)


# Let's pick a weapon
print("\nYou are about to embark on an epic quest!")
time.sleep(2)
print("You will need a weapon to protect yourself.")
time.sleep(2)
# Use """ to create a multi-line string
    # This is useful for long strings or when you want to format the string nicely
    # The triple quotes allow you to create a string that spans multiple lines
print("""
      \nChoose your weapon:
      1 - Sword and Shield
      2 - Magic Wand
      3 - Bow and Arrows
      """)
time.sleep(1)


# Get the user's choice
    # if/elif/else statements are used to make decisions in the program
        # The if statement checks if the condition is true
        # The elif statement checks if the previous condition was false and this condition is true
        # The else statement is executed if all previous conditions were false
weapon_choice = input("Enter the number of your choice: ")
if weapon_choice == "1": # == is used to compare two values
    # If the value of weapon_choice is equal to "1"
        # then the code inside this block will be executed
            # This is called a block of code
    weapon = "a shiny sword and strong shield"
elif weapon_choice == "2":
    weapon = "a magical wand with increadible powers"
elif weapon_choice == "3":
    weapon = "an elven bow and arrows with perfect aim"
else:
    weapon = "your bare hands" # If the user enters something other than 1, 2, or 3
# weapon will be which ever number the player chooses
time.sleep(1)

# Now let's see what the user chose
print("\nYou chose", end='', flush=True)
time.sleep(1)
print(".", end='', flush=True)
time.sleep(1)
print(".", end='', flush=True)
time.sleep(1)
print(".", end='', flush=True)
time.sleep(1)
print("", weapon + "!") # weapon is a variable that stores the weapon chosen by the user
# The + operator is used to concatenate (join) two strings together

# Now let's see if the dragon is friendly
time.sleep(3)
print("\nNow you are ready to face the Dragon!")
time.sleep(2)
print("Sorry!", end='', flush=True)
time.sleep(1)
print("I meant to say meet the dragon")
print("\n")

# To be continued

    
