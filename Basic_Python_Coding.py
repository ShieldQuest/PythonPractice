# Basic Python Coding
# print("Text") is used to show text on the screen
print("\n") # "\n" add a new line for better visual display 
print("Basic Python Coding")
print("\n")


# Lesson 1: Print statement
print("Lesson 1: Print statement")
print("Hello World!")
print("\n")


# Lesson 2: Simple Math
print("Lesson 2: Simple Math")
print(1+1, "= 1 + 1") # , is used to separate the two values 
print(1-1, "= 1 - 1") 
print(1*2, "= 1 * 2")
print(1/2, "= 1 / 2")
print("\n")


# Lesson 3: Assigning Values to Variables
# Variables are used to store values
print("Lesson 3: Assigning Values to Variables")
name = "ShieldQuest"
print(name, "= The variable is 'name' and the assigned value is 'ShieldQuest'")
pizza_slices = 8
print(pizza_slices, "= The variable is 'pizza_slices' and the assigned value is '8'")
pizza_slice = pizza_slices - 2
print(pizza_slice, "= The variable is 'pizza_slice' and the assigned value is 'pizza_slices - 2'")
print("\n")


# Lesson 4: Numbers, and Boolean
print("Lesson 4: Numbers, and Boolean")
age = 120 # Integer values are whole numbers
height = 7.3 # Float values are decimal numbers
is_coding_fun = True # Boolean values are True or False
print("my age could be", age, "years old and my height could be", height, "feet tall")
print("Is coding fun?", is_coding_fun)
print("\n")


# Lesson 5: Checking Data Types
print("Lesson 5: Checking Data Types")
print(type(name), " String values are text") # String 
print(type(age), " Integer values are whole numbers") # Integer
print(type(height), "Foat values are decimal numbers") # Float
print(type(is_coding_fun), " Boolean values are True or False") # Boolean
print("\n")



# Lesson 6: Conditional Statements
print("Lesson 6: Conditional Statements")
print("Using the Variable 'age' to check if I am an adult")
# if statements are used to check if a condition is true or false
if age >= 18: # >= is used to check if the value is greater than or equal to 18
    print("I am an adult")
else: # else is used to check if the condition is false
    print("I am not an adult")
print("\n")


# temperature check
temperature = 74 
print("the temperature is", temperature, "degrees")
if temperature >= 80:
    print("It's hot outside")
elif temperature >= 60: # elif is used to check if the condition is true
    print("It's warm outside")
else:
    print("It's cool outside")


# Examplpe of Pokemon Battle
pokemon = "Charmander"
print("\n",pokemon, "attack!")
if pokemon == "Pikachu":
    print("Electric shock activated")
elif pokemon == "Charmander":
    print("Fire blast engaged")
elif pokemon == "Squirtle":
    print("Water cannon ready")
else:
    print("Unknown Pokemon")
print("\n")



# Lesson 7: Loops
print("Lesson 7: Loops")
print("Using a 'for' loop to print numbers from 1 to 5")


# 'for i in' are used to repeat the code inside the loop
# 'i' is a variable that takes on the value of each number in the range
for i in range(1, 6): # range(1, 6) generates numbers from 1 to 5
    print("The count is:", i)
print("The loop has ended!\n")
print("Using a 'while' loop to print numbers from 1 to 5")
i = 1 # i is assigned the value of 1


while i <= 5: # while loop continues until it is equal to 5
    print("The count is:", i) 
    i += 1 # increment i by 1
print("The loop has ended!\n")




# Lesson 8: Lists
print("\nLesson 8: Lists")
print("Using a list to store multiple values")
groceries = ["milk", "eggs", "bread", "butter"] # List is a collection of items
print("My grocery list:", groceries)
print("The first item in the list is:", groceries[0]) # Indexing starts at 0
print("The second item in the list is:", groceries[1]) # 1 is the second item
print("The last item in the list is:", groceries[2]) # 2 is used to access the third item
print("The last item in the list is:", groceries[3]) # 3 is used to access the last item
print("\n")

print("You can check how many items are in the list by using the len() function")
print("The number of items in the grocery list is:", len(groceries)) # len() function returns the length of the list
print("\n")



# Lesson 8: Add, Remove, and/or Change Items in a List
print("\nLesson 8: Add, Remove, and/or Change Items in a List")

print("\nAdding items to the list using the append() function")
groceries.append("cheese") # append() function adds an item to the end of the list
print("My grocery list:", groceries)

print("\nRemoving items from the list using the remove() function")
groceries.remove("eggs") # remove() function removes the item from the list
print("My grocery list:", groceries)

print("\nChanging items in the list by using the index")
# Indexing is used to access the items in the list
# groceries[0] is used to access the first item in the list
# groceries[1] is used to access the second item in the list
# groceries[2] is used to access the third item in the list
# groceries[3] is used to access the last item in the list
# groceries[4] is used to access the fifth item in the list
groceries[0] = "almond milk" # changing the first item in the list
print("My grocery list:", groceries)

print("\nRemoving items from the list using the pop() function")
groceries.pop(3) # pop() function removes the item at the specified index
print("My grocery list:", groceries)

print("\nAdding more items to the list using the + operator")
# + operator is used to concatenate two lists
# groceries + ["apples", "cheese"] is used to add more items to the list
groceries += ["apples", "cheese"]
print("My grocery list:", groceries)

print("\nTotal number of items in the grocery list using the len() function")
# len() function returns the length of the list
print("I have a total of", len(groceries), "items in my grocery list")
print("\n")




