# Strings Practical Exercise #1 – Username Validator: A website needs a function validate_username(username) that returns True if the username is valid and False otherwise. A valid username must:Be between 5 and 15 characters long, Contain only letters, digits, or underscores, Start with a letter, Not end with an underscore, Contain at least one digit. 
# Test cases: 
#   validate_username("coder_42") → True
#   validate_username("2cool") → False
#   validate_username("hi") → False
#   validate_username("python_dev_") → False, validate_username("justletters") → False

def validate_username(username):
    if len(username) < 5 or len(username) > 15:
        return False
        
    if not username[0].isalpha():
        return False

    if username[-1] == '_':
        return False

    if not all(char.isalnum() or char == '_' for char in username):
        return False

    if not any(char.isdigit() for char in username):
        return False

    return True

# Strings Practical Exercise #2 – Secret Message Decoder: Spies encode messages with the following scheme: Every word is reversed, The whole message is lowercase, The character # is used instead of spaces, Any digit in the message is junk and should be removed, Write a function decode(message) that returns the original message with the first letter of the sentence capitalized. Example: decode("eht7#terces#3edoc#si#nohtyp9") → "The secret code is python“. Hint: requires .split(), .join(), slicing, and iteration
def decode(message):
    # Step 1: Remove all junk digits from the message
    clean_message = "".join(char for char in message if not char.isdigit())
    
    # Step 2: Split the message into words using the '#' character
    words = clean_message.split("#")
    
    # Step 3: Reverse each individual word using slicing [::-1]
    reversed_words = [word[::-1] for word in words]
    
    # Step 4: Join the reversed words back together with a space
    decoded_sentence = " ".join(reversed_words)
    
    # Step 5: Capitalize only the first letter of the sentence
    return decoded_sentence.capitalize()

# Functions with default parameters practical exercise: Write curve_grades(scores, bonus=5, max_score=100) that takes a list of scores and returns a new list where each score gets the bonus added, but no score exceed# s max_score.
def curve_grades(scores, bonus=5, max_score=100):
    curve = []
    for num in scores:
        adjusted = num + bonus
        if adjusted >= max_score:
            curve.append(max_score)
        else:
            curve.append(adjusted)
    return curve

num_grades = int(input('How many grades will you be recording? '))
grades = []
for i in range(num_grades):
    grade = float(input(f'Enter grade {i + 1}: '))
    grades.append(grade)
grade_curve = int(input('What is your curve structure? '))
max_grade = int(input('What is the max score? '))
print(f'Curved grades output: {curve_grades(grades, grade_curve, max_grade)}')

# Functions with multiple returns practical: Requires: enumerate() — nothing else fancy An airline boards passengers in the order they appear in the list. Seat numbers start at 1, not 0. passengers = ["Lopez", "Chen", "Okafor", "Smith", "Patel"] Write a function print_boarding_list(passengers) that prints each passenger with their seat number: Seat 1: Lopez Seat 2: Chen Seat 3: Okafor Seat 4: Smith Seat 5: Patel You must use the enumerate() function!
def print_boarding_list(passengers):
    for i, passenger in enumerate(passengers, start=1):
        print(f'Seat {i}: {passenger}')

passengers = ["Lopez", "Chen", "Okafor", "Smith", "Patel"]

print_boarding_list(passengers)