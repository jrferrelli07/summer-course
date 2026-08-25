# Problem 1 – Temperature Advisor: Ask the user for the current temperature. Print "Wear a coat" if it's below 40, "Bring a jacket" if it's 40–65, and "Enjoy the weather!" if it's above 65. Stretch goal: Also ask whether it's raining (yes/no) and adjust the advice accordingly — e.g., "Bring an umbrella" gets appended to any message when it's raining.
c_temp = float(input('What is the current temperature? '))
c_cond = input('Is it currently raining (yes/no)? ').lower().strip()
def weather(temp,cond):
    if temp < 40:
        advice = 'Wear a coat. '
    elif temp >= 40 and c_temp <= 65:
        advice = 'Bring a jacket. '
    else:
        advice = 'Enjoy the weather! '
    if cond == 'yes':
        rain = 'Bring an umbrella.'
    else:
        rain = ''
    return advice + rain
print(weather(c_temp, c_cond))

# Problem 2 – FizzBuzz with a Twist: Loop through the numbers 1 to 30. Print "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for multiples of both, and the number itself otherwise. Stretch goal: Wrap the logic in a function fizzbuzz(start, end) so the user can choose the range, and count how many "FizzBuzz" lines were printed, reporting the total at the end.
def fizzbuzz(start, end):
    count = 0
    current_num = start
    while current_num <= end:
        if current_num % 3 == 0 and current_num % 5 == 0:
            print('FizzBuzz')
            count += 1
        elif count % 5 == 0:
            print('Buzz')
        elif count % 3 == 0:
            print('Fizz')
        else:
            print(current_num)

        current_num += 1
    return count

rng_choice = input('Do you wish to create your own range (yes/no)? ').lower().strip()
if rng_choice in ['yes', 'y']:
    rng = int(input('Enter your range number: '))
else:
    rng = 30
total = fizzbuzz(1, rng)
print(f'\nTotal FizzBuzz lines printed: {total}.')

# Problem 3 – Password Checker: Write a function check_password(password) that returns "Weak" if the password is shorter than 8 characters, "Medium" if it's 8+ characters, and "Strong" if it's 8+ characters and contains at least one digit. (Looping through the characters to check for a digit is a nice loop exercise.) Stretch goal: Add a requirement for at least one uppercase letter for "Strong", and keep prompting the user in a while loop until they enter a strong password.
def check_pass(password):
    if len(password) < 8:
        return "Weak"
        
    has_digit = False
    has_capital = False
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_capital = True
            
    if has_digit and has_capital:
        return "Strong"
    else:
        return "Medium"

u_pass = input('Provide a password (8+ chars, 1 digit, 1 capital): ')

while check_pass(u_pass) != "Strong":
    print(f"Current strength: {check_pass(u_pass)}")
    u_pass = input('Try again. Provide a stronger password: ')

print("Success! Your password is Strong.")

# Problem 4 – Grade Calculator: Write a function letter_grade(score) that converts a numeric score to a letter grade (A/B/C/D/F). Then ask the user how many test scores they want to enter, loop that many times collecting scores, and print each score with its letter grade. Stretch goal: Compute and display the class average and its letter grade, and report the highest and lowest scores — without using max() or min(), so students practice tracking values inside a loop.
def letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

c_min = None
c_max = None
c_sum = 0
c_count = 0
c_total = int(input('Enter the number of test scores: '))
while c_count < c_total:
    c_score = int(input('Enter score'))
    c_grade = letter_grade(c_score)
    c_count += 1
    c_sum += c_score
    if c_min is None or c_score < c_min:
        c_min = c_score
    if c_max is None or c_score > c_max:
        c_max = c_score
    print(f'Score {c_score}, Grade {c_grade}')

c_avg = c_sum / c_count
c_avggrade = letter_grade(c_avg)
Print(f'There were {c_count} tests with a test average of {c_avg} {c_avggrade}, a high score of {c_max}, and a low score of {c_min}.')
    