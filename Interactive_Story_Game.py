# Let's play with variables!
name = "Bael" # Name of our imaginary dragon
age = 15 # Age of our imaginary dragon
color = "red" # Color of our imaginary dragon
is_friendly = "Maybe" # Is our imaginary dragon friendly?

# Let's print a story about our imaginary pet dragon
print("\nI want you to meet my Dragon!")
print("His name is", name)
print("He is", age, "years old in dragon years and has", color, "scales.")
print("He lives inside the cave behind me.")
print("\nIs he friendly?...", is_friendly)

# Now let's make it fun and interactive!
print("\n")
your_name = input("What is your name, brave adventurer? ")
print("\nNice to meet you,", your_name,"!")
print("I hope you like dragons!")

# Let's pick a weapon
print("\nYou are about to embark on an epic quest!")
print("You will need a weapon to protect yourself.")
# Use """ to create a multi-line string
print("""
      \nChoose your weapon:
      1 - Sword and Shield
      2 - Magic Wand
      3 - Bow and Arrows
      """)
# Get the user's choice
weapon_choice = input("Enter the number of your choice: ")
if weapon_choice == "1":
    weapon = "a shiny sword and strong shield"
elif weapon_choice == "2":
    weapon = "a magical wand with increadible powers"
elif weapon_choice == "3":
    weapon = "an elven bow and arrows with perfect aim"
else:
    weapon = "your bare hands."

print("\nYou chose", weapon + "!")
print("\nNow you are ready to face the dragon!")
print("Sorry! I meant to say meet the dragon")
print("\n")


    
