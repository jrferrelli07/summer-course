# Problem 1: Print the numbers from 1 to 100.  If the number is divisible by 3, print “Fizz” instead of the number.  If it is divisible by 5, print “Buzz” instead of the number.  If it is divisible by both, print “FizzBuzz” instead of the number.
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3 == 0:
        print('Fizz')
    else:
        print(num)

# Problem 2: Ask the user for “rock”, “paper”, or “scissors”.  Randomly assign the computer’s choice of “rock”, “paper”, or “scissors”. Display whether the user won, lost, or tied.
import random
i = input('Rock, Paper, or Scissors? ').lower()
c = ['rock', 'paper', 'scissors']
ai = random.choice(c)
if i == ai:
    print('Tie!')
elif (i == 'rock' and ai == 'scissors') or (i == 'scissors' and ai == 'paper') or (i == 'paper' and ai == 'rock'):
    print('You Win!')
else:
    print('You Lose!')

# Problem 3: Create a guessing game.  Randomly assign a number from 1 to 100 (using the random module).  Ask the user to guess the number.  If the user guesses higher, display “Too high”.  If the user guesses lower, display “Too low”.  Congratulate the user when they guess the correct number.  Continually ask the user until they get the number correct. Bonus:  Display to the user how many times they guessed.
import random
r = random.randint(1, 100)
c = 0
while True:
    i = int(input('Guess my number '))
    c += 1

    if i > r:
        print('Too High')
    elif i < r:
        print('Too Low')
    else:
        print(f'You Win! Congrats! It only took you {c} times!')
        break

# Problem 4: Write a program to help you track your student’s grades.  Ask the user how many students are in the class.  For each student, ask their name and their grade.  Display the class average.  Display the highest grade in the class. Display the lowest grade in the class. Bonus:  Display who got the highest grade in the class.
# Student input/variable
s = int(input('How many students are in the class? '))
# Name list
nl = []
# Grade list
gl = []
for ng in range(s):
    n = input("Enter the student's name")
    g = float(input("Enter the student's grade"))
    # Create a name and grade list. Index will link them together
    nl.append(n)
    gl.append(g)
# Find max and min grades
max_grade = max(gl)
min_grade = min(gl)
# Find indexes of max and min grades
max_index = gl.index(max_grade)
min_index = gl.index(min_grade)
# Find names matching the indexes
top_grade = nl[max_index]
low_grade = nl[min_index]
class_average = sum(gl) / s
print(f'The class GPA was {class_average:.2f}.')
print(f'The highest grade was {max_grade} achieved by {top_grade}.')
print(f'The lowest grade was {min_grade} achieved by {low_grade}.')

# What are some built-in Python functions that we have learned about? Min, max, sum, random
# What do these functions do: random.randint(a,b), random.choice(seq), random.random()? randint produces a random integer between a and b. choice(seq) produces a random list item. random() produces a random float between 0.0 and 1.0.
# Write a Python Script that randomly generates an integer from 0 to 100. If the integer is less than 50, state “The number is less than 50”. If the number is 50, state “The number is 50”. If the number is greater than 50, state “The number is greater than 50” *Display the number to check your code*
import random
n = random.randint(0,100)
if n < 50:
    print(f'{n} is less than 50.')
elif n == 50:
    print(f'{n} is 50.')
else:
    print(f'{n} is greater than 50.')

# Write a Python script that: name_list = [“John”, “Rachel”, “Sam”, “Carlos”, “Jane”] Randomly picks a name from the list. Print the name.
import random
nl = ['John', 'Rachel', 'Sam', 'Carlos', 'Jane']
c = random.choice(nl)
print(c)

# What do these functions do: math.dist(p, q), math.pi, math.degrees(x)? math.dist() returns the distance between two points as a sequence of coordinates. math.pi returns pi. math.degrees converts an angle from degrees to radians.
# You want to build a circular patio for your home.  Write a program that prompts the user for the diameter of their patio (in feet).  With the diameter, calculate the total area of the patio.  Print the total area of the patio. Print the number of bricks you suggest the user buys for their project. (Bricks are 4” x 6”). Use math.pi
import math
dia = float(input('Enter the diameter of your patio in feet. '))
patio_area = ((dia / 2) ** 2) * math.pi
print(f'The area of your circular patio is {patio_area} feet.')
patio_area_inches = patio_area * (12 ** 2)
brick_area = 4 * 6
bricks_req = math.ceil(patio_area_inches / brick_area)
print(f'You will require {bricks_req} bricks to complete the project.')

# Exercise 1: Write a python function that calculates and returns the area of a rectangle using two integer inputs from the user! Outside of the function call, print the area.
def rec_area():
    ht = int(input('What is your height of the rectangle in inches? '))
    lg = int(input('What is your length of the rectangle in inches? '))
    area =  ht * lg
    return area
print(rec_area())

# Exercise 2: Write a function called tip() that has two parameters named total and percentage. This function should return the amount you should tip given a total and the percentage you want to tip.  Print the amount returned outside of the function call. tip(10, 25) = 2.5
def tip():
    tot = float(input('Enter bill total: '))
    per = float(input('Enter desired tip percentage: '))
    tip_total = tot * (per / 100)
    return tip_total
print(f'Your total tip is ${tip():,.2f}')

# Exercise 2 corrected: Write a function called tip() that has two parameters named total and percentage. This function should return the amount you should tip given a total and the percentage you want to tip.  Print the amount returned outside of the function call. tip(10, 25) = 2.5
def tip(tot, per):
    tip_total = tot * (per / 100)
    return tip_total
result = tip(10,25)
print(f'Your total tip is ${result:,.2f}')

# Exercise 3: Write a function that takes a numerical input from the user, cubes that number, and then returns the result.  Print the result outside of the function call.
inp = float(input('Enter a number: '))
def cube(num):
    result = num ** 3
    return result
print(cube(inp))

# Exercise 4: Write a function that is called “has_more_characters”.  This function should accept two strings as arguments, and will return the string that has more characters.  Outside of the function call, print the string with more characters.
def has_more_characters():
    s1 = len(input('Enter string 1: '))
    s2 = len(input('Enter string 2: '))
    if s1 > s2:
        result = 'String 1'
    elif s2 > s1:
        result = 'String 2'
    else:
        result = 'Both strings are equal'
    return result
print(has_more_characters())

# Exercise 5: Write a function that is called “count_char_x”.  This function should accept two inputs, a word and a character.  The function will return how many instances of the character are in the word.
def count_char_x(wd, char):
    result = wd.count(char)
    return result
str1 = input('Enter a word: ')
str2 = input('Enter a character: ')
instances = count_char_x(str1, str2)
print(f'The letter {str2} appears {instances} times within {str1}.')

# What did you learn? I learned how to use built in functions (libraries) within python to expedite the coding used. I also learned how to define my own functions. I noticed I need to take more time in reading the question and exactly executing as requested. I also need to ensure I profread my result before submission.