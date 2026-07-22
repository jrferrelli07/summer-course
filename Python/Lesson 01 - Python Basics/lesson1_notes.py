# Examples of primitive_datatypes
print("Examples of prmitive datatypes:", "\n")
integer = 5, 7, 9
flo = 1.6, 2.7, 3.9
string = "Yo", "Wazzup", "Gnarly"
boo = True
print(*integer)
print(*flo)
print(*string)
print(boo)

# Exercise 1: Correction to 10 + "15"
print(10 + int(15))

# Variables
my_var = int(5)
new_var = str("Hello")
third_var = float(7.2)
print(my_var + third_var)

# Exercise 2: A Pittsburgh pizza shop is having a two-for-one deal. You can get two small (12”) pizzas for $9.99. In contrast, a large pizza (17”) costs $9.99.  
# Which one is the better deal (yields more area)? What is your first intuition? 
# With a partner, write a plan on how to solve the problem
# Then write Python code in the interpreter to answer this question. Use variables to store data for later, Use 3.14 for pi, area = pi * radius ** 2
small_pizza = (3.14 * (24 / 2) ** 2) / 9.99
large_pizza = (3.14 * (17 / 2) ** 2) / 9.99
print("small", small_pizza)
print("large", large_pizza)
print("Small pizza is the better deal")

# The input() function waits for the user to type something and hit enter
# Always gives you a string back

# Exercise 3: Write a Python Script that:
# Asks the user for their name
# Asks the user for their favorite number
# Prints “Hello” and then their name
# Prints “Your favorite number is” and then their favorite number
# Prints “Your favorite number minus 10 is” their favorite number minus 10
usr_name = input('Please tell me your name:')
usr_num = input('Please tell me your favorite number:')
print("Hello", usr_name)
print("Your favorite number is", usr_num)
print("Your favorite number minus 10 is", int(usr_num) - 10)
print(f"Hello {usr_name}")

# Exercise 4: Pizza pizza
# Write a script that prompts the user for a diameter of the pizza and outputs the area
# Remember to convert from string to another datatype
# Stretch goal #1:  write a script that calculates the price per area.  The user should input the diameter and the cost.
# Stretch goal #2:  write a script that calculates the best deal.  
# The deal is 2 pizzas of one size compared to 1 pizza of another size.
# The user should input two diameters (one for the first deal, one for the second deal), and the two costs.
dia1 = input('Please enter the pizza size for option 1:')
p_area1 = 3.14 * ((int(dia1) * 2) / 2) ** 2
print(f'Pizza area for option 1 = {p_area1}')
price1 = input('Please enter the cost of the pizza for option 1:')
p_price1 = float(price1)/p_area1
print(f'The pizza price per area for option 1 is ${p_price1:.2}')
dia2 = input('Please enter the pizza size for option 2:')
p_area2 = 3.14 * (int(dia2) / 2) ** 2
print(f'Pizza area for option 2 = {p_area2}')
price2 = input('Please enter the cost of the pizza for option 2:')
p_price2 = float(price2)/p_area2
print(f'The pizza price per area for option 2 is ${p_price2:.2}')
if p_price1 > p_price2:
    print('Option 2 is the better deal')
else:
    print('Option 1 is the better deal')

# What is Python? Python is a programming language.
# What are some data types in Python? Integer, string, boolean, float
# How do we interactively run the Python Interpreter? Type python into the command line
# How do we run a python script? Type python followed by the path of the .py file
# What is the order of operations in Python? Same as math, PEMDAS
# What if expressions have the same precedence in PEMDAS? Evaluates left to right
# How do we get text input from a user? Use the input function
# What datatype does the input() function return? String
