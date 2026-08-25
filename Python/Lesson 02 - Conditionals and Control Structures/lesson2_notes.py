# To learn coding, quantity creates quality: 
# Write code, even if it is bad: Don't spend hours trying to write the "perfect, cleanest" script on your first try or hesitate to write code because you might get an error.
# Fail fast and debug often: Churning out multiple small practice scripts, getting errors, fixing them, and playing around with the code is how concepts "click."
# Volume beats theory: Writing 10 buggy, simple scripts that you eventually fix will teach you far more than spending 3 hours reading slides trying to write 1 flawless script.
# Linux is an open source operating system with a powerful command line
# Git is a version control system
# Type casting is the process of manually converting a value from one data type to another. There are two types:
    # Implicit (Coercion): data conversions Python executes automatically
    # Explicit (Casting): Manually changing the type through functions like int(), float(), str(), or list()
# Type casting is important because it resolves type errors, fixes user inputs, saves memory, and ensures data integrity

# Write a script that asks a user for a number.  The script then checks the number and prints “positive,” “zero,” or “negative”
number = float(input('Provide a number:'))
if number > 0:
    print('Positive')
elif number < 0:
    print('Negative')
else:
    print ('Zero')

# REMEMBER Input() always returns a string and you don't need to use print() within an input() statement.

# Hands-On
# Exercise 1: Check if a Number is Positive. Goal: Write a Python Script that asks a user for an integer number, and then checks if the number is positive using an if statement.
number = int(input('Provide an integer (number):'))
if number > 0:
    print('Positive')
else:
    print('Not positive')

# Exercise 2: Even or Odd. Goal: Write a Python script that asks a user for an integer number. Check if the number is even or odd using if and else.
number = int(input('Provide an integer (number):'))
if number % 2 == 0:
    print('Even')
else:
    print('Odd')

# Exercise 3: Age Category. Goal: Write a python script that asks a user for their age, and then uses if, elif, and else to print the correct category for the person by based on their age.
age = int(input('Provide your age: '))
if age < 13:
    print('Child')
elif age >= 13 or age <= 19:
    print('Teenager')
elif age >= 20 or age <= 64:
    print('Adult')
else:
    print('Senior')

# Exercise 4: Compare Two Numbers. Goal: Write a Python Script that asks a user for two numbers. Compare the two numbers and print which is larger, or if they're equal.
num1 = int(input('Provide a number: '))
num2 = int(input('Provide another number: '))
if num1 == num2:
    print('The numbers are equal')
elif num1 > num2:
    print(f'{num1} is larger')
else:
    print(f'{num2} is larger')

# Exercise 5: Grade Converter. Goal: Write a Python Script that asks a user for a numeric grade, and then converts a numeric grade to a letter grade and prints the letter grade.
grade = float(input('Provide the course grade: '))
if grade >= 90:
    print(f'Your {grade} is an A')
elif grade >= 80:
    print(f'Your {grade} is a B')
elif grade >= 70:
    print(f'Your {grade} is a C')
elif grade >= 60:
    print(f'Your {grade} is a D')
else:
    print(f'Your {grade} is a F')

# Exercise 6: String Length Check. Goal: Write a Python Script that asks the user for an input string. Then check if a string has more than 10 characters. Print "Long string" if it is longer than 10 characters, print "Short string" if it is shorter.
inp = input('Provide an input: ')
if len(inp) > 10:
    print('Long string')
else:
    print('Short string')

# Exercise 7: Logical AND Operator. Goal: Write a Python script that asks the user for a number. Check if a number is between 10 and 20 (inclusive) using the and operator. Print "Number is in range" if it is in between 10 and 20. Otherwise it should print "Out of range."
number = int(input('Provide an integer (number):'))
if number >= 10 and number <= 20:
    print(f'{number} is in range')
else:
    print(f'{number} is out of range')

# Exercise 8: Logical OR Operator. Goal: Write a python script that checks if a character is a vowel using the or operator. Print "vowel" or "consonant" depending on the input.
char = input('Provide a letter: ')
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print('Vowel')
else:
    print('Consonant')

# Stretch: Exercise 9: Leap Year Checker. Goal: Write a Python Script that asks the user for the year. Determine if a year is a leap year. Print the result. Rules: Divisible by 4 AND not divisible by 100, OR Divisible by 400
yr = int(input('What is the year?: '))
if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
    print('Leap Year')
else:
    print('Non Leap Year')

# Stretch: Exercise 10: Nested Conditionals - BMI Calculator. Goal: Write a Python Script that asks the user for their weight in kilograms and their height in meters. Calculate BMI category using correct if-elif-else structure. BMI < 18.5: "Underweight", BMI 18.5-24.9: "Normal weight", BMI 25-29.9: "Overweight", BMI 30+: "Obese". Formula: BMI = weight (kg) / height (m)²
wt = float(input('What is your weight (kg)?: '))
ht = float(input('What is your height (m)?: '))
bmi = wt / ht ** 2
if bmi < 18.5:
    print('Underweight')
elif bmi < 25:
    print('Normal Weight')
elif bmi < 30:
    print('Overweight')
else:
    print('Obese')

# New datatype: Lists
# an_example_list = [1, 2, 3, “Hello”, “Goodbye”, 6.0]

# Example 1: Use a for loop to print the numbers from 1 to 10
num = range(1, 11)
for number in num:
    print(number)

# Example 2: Create a list.  Add an item to the end of the list.  Use a for loop to print each item in the list.
name = ['Jesse', 'Ryan']
name.append('Ferrelli')
for nam in name:
    print(nam)

# Example 3: Use a for loop to print all the even numbers between 20 and 50
number = range(22, 50, 2)
for num in number:
    print(num)

# Example 4: Create the list [10, 20, 30, 40, 50].  Find the average value of the list using a for loop.
my_list = [10, 20, 30, 40, 50]
total = 0
count = 0
for sum in my_list:
    total += sum
    count += 1
avg = total/count
print(avg)

# Example 5: Ask the user to input an even integer number.  If the user puts in an odd number, print “This is an odd number”, and then prompt the user for an even number.  Continue to do this until the user enters an even number.  **Assume the user will always input an integer value**
number = int(input('Provide an even number: '))
while number % 2 == 1:
    print('This is an odd number. ')
    number = int(input('Provide an even number: '))

# Example 6: Hard code a secret integer number between 1 and 100.  Ask the user to guess the integer.  If they are higher then the secret number, tell them they are higher.  If they are lower, tell them they are lower.  When they guess it correctly, congratulate them, and end the program. Bonus:  Display how many times the user guessed until they got it correct after they get it correct.
secret = 7
count = 1
guess = int(input('Guess my secret number: '))
while guess != secret:
    count += 1
    if guess > secret:
        print('You are too high!')
    else:
        print('You are too low!')
    guess = int(input('Guess my secret number: '))
print(f'You got my lucky number {secret}! It took you {count} times.')

# Exercise 11: Create and Print a List. Goal: Create a list of your favorite colors and print each color using a for loop.
fav_colors = ['blue', 'gold', 'red']
for fcolor in fav_colors:
    print(fcolor)

# Exercise 12: List Length. Goal: Create a list of numbers and print how many items are in the list.
num = [1, 2, 3, 4, 5]
count = 0
for number in num:
    count += 1
print(count)

# Exercise 13: Append to a List. Goal: Start with an empty list and add 5 different items to it using append().
my_list = []
for item in range(1, 6):
    my_list.append(item)
print(my_list)

# Exercise 14: Loop Through a Range. Goal: Use a for loop with range() to print numbers 1 through 10.
for item in range(1, 11):
    print(item)

# Exercise 15: Sum Numbers in a List. Goal: Calculate the sum of all numbers in a list using a for loop. numbers = [4, 7, 2, 9, 12]
numbers = [4, 7, 2, 9, 12]
tsum = 0
for num in numbers:
    tsum += num
print(tsum)

# Exercise 16: List Membership. Goal: Check if a fruit is in a list of available fruits. available_fruits = ["apple", "banana", "orange", "mango"] fruit = "banana"
available_fruits = ["apple", "banana", "orange", "mango"]
fruit = "banana"
if fruit in available_fruits:
    print('in stock')
else:
    print('out of stock')

# Exercise 17: Count Even Numbers. Goal: Count how many even numbers are in a list using a for loop. numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
    else:
        pass
print(f'There are {count} even numbers')

# Exercise 18: While Loop Countdown. Goal: Use a while loop to count down from 10 to 1. count = 10
count = 10
while count > 0:
    print(count)
    count -= 1

#Stretch: Exercise 19: While Loop with Condition. Goal: Use a while loop to keep doubling a number until it exceeds 100. number = 1
number = 1
while number <= 100:
    print(number)
    number *= 2

# Stretch: Exercise 20: Create a List with Range. Goal: Use range() to create a list of even numbers from 0 to 20.
my_list = []
my_list.extend(range(0, 22, 2))
print(my_list)

# Exercise 21: Build a List with Loop. Goal: Create a new list containing the squares of numbers 1 through 5.
my_list = []
for number in range(1,6):
    my_list.append(number ** 2)
print(my_list)

# Exercise 22: Count Vowels in String. Goal: Count how many vowels are in a string using a loop. text = "Hello World" vowels = "aeiouAEIOU"
text = "Hello World" 
vowels = "aeiouAEIOU"
count = 0
for letter in text:
    if letter in vowels:
        count += 1
print(count)

# Exercise 23: Find Maximum in List. Goal: Find the largest number in a list using a for loop. numbers = [23, 67, 12, 89, 45, 34]
numbers = [23, 67, 12, 89, 45, 34]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f'the maximum is {max_num}')

# Goal: Loop through a list and stop when you find the number 7. numbers = [2, 5, 7, 10, 15]
numbers = [2, 5, 7, 10, 15]
for num in numbers:
    if num == 7:
        print(num)
        break

# Exercise 25: Continue Statement. Goal: Print numbers 1 to 10 but skip multiples of 3 using continue.
for num in range(1,11):
    if num % 3 == 0:
        continue
    print(num)# Exercise 26: Nested Loops - Multiplication Table. Goal: Use nested for loops to create a 3x3 multiplication table.
for num1 in range(1,4):
    for num2 in range(1,4):
        print(num1 * num2)

# Exercise 26: Nested Loops - Multiplication Table. Goal: Use nested for loops to create a 3x3 multiplication table.
for num1 in range(1,4):
    for num2 in range(1,4):
        print(num1 * num2, end=" ")
    print()

# Exercise 27: While Loop with User Input Simulation. Goal: Use a while loop to add numbers to a list until the sum exceeds 50. numbers = [5, 10, 8, 15, 12, 7]
numbers = [5, 10, 8, 15, 12, 7]
my_list = []
sum = 0
index = 0
while sum <= 50 and index < len(numbers):
    num = numbers[index]
    sum += num
    my_list.append(num)
    index += 1
print(my_list)

# Exercise 28: Find Index of Item. Goal: Loop through a list to find the index position of a specific item. fruits = ["apple", "banana", "cherry", "date"] target = "cherry"
fruits = ["apple", "banana", "cherry", "date"] 
target = "cherry"
index = 0
while fruits[index] != target:
    index += 1
print(f'{target} is at index {index}')

# Stretch: Exercise 29: Reverse a List Manually. Goal: Create a new list that is the reverse of the original using a loop. original = [10, 20, 30, 40, 50]
original = [10, 20, 30, 40, 50]
index = 4
new = []
while index > -1:
    new.append(original[index])
    index -= 1
print(new)

# Stretch: Exercise 30: Stop After Printing Asterisks. Goal: Use nested loops to print asterisks in rows, but stop completely after printing exactly 10 asterisks total. The number of asterisks in row n should be n. Hint: You'll need to track the total count of asterisks printed and use break to exit both loops.
num_asterisks = 0
for row in range(1, 10):
    for star in range(row):
        print('*', end='')
        num_asterisks += 1
        if num_asterisks == 10:
            break
    if num_asterisks == 10:
        break
    print()
print()