# Targeted Practice Problems: Lessons 1–3 (Functions, Scope, Loops, Accumulators, & Conditionals)
# Write your code directly below each problem description.

"""
================================================================================
PROBLEM 1: Pure Processor Function (No Grocery Shopping / Scope Separation)
================================================================================
Goal: Enforce strict parameter usage and scope isolation ("The Cook" mental model).

Task:
Write a function named `calculate_fuel_efficiency(distance_miles, fuel_gallons)` that:
- Takes two arguments: distance_miles (float) and fuel_gallons (float).
- Returns the efficiency in Miles Per Gallon (MPG) rounded to 1 decimal place.
- IMPORTANT: Do NOT call `input()` inside the function, and do NOT use any global variables inside the function body!

Outside the function (Global Scope):
- Prompt the user for total distance traveled (miles) and fuel used (gallons).
- Call `calculate_fuel_efficiency(miles, gallons)` with the user inputs.
- Print a summary statement, e.g. "Your vehicle gets 24.5 MPG."
"""

# --- YOUR CODE FOR PROBLEM 1 HERE ---
def calculate_fuel_efficiency(distance_miles, fuel_gallons):
  mpg = float(distance_miles) / float(fuel_gallons)
  return mpg

mi = float(input('Enter total distance traveled (miles): '))
gal = float(input('Enter total fuel used (gallons): '))
trip_mpg = float(calculate_fuel_efficiency(mi, gal))

print(f'On this trip, your vehicle had an efficiency rate of {trip_mpg}')


"""
================================================================================
PROBLEM 2: While Loop to For Loop & Pure Function Refactoring
================================================================================
Goal: Practice using Pythonic `for` loops with `range()` instead of manual `while` counters,
and cleanly separate argument processing from tracking.

Task:
Write a function named `summarize_multiples(start_num, end_num, divisor)` that:
- Iterates from `start_num` through `end_num` (inclusive) using a Pythonic `for` loop and `range()`.
- Counts how many numbers in that range are evenly divisible by `divisor`.
- Prints each divisible number as it finds it.
- Returns the total count of divisible numbers found.

Outside the function:
- Ask the user for a start number, end number, and divisor.
- Call `summarize_multiples` with those values and store the returned count.
- Print the total count at the end (e.g. "Found 6 numbers divisible by 4.").
"""

# --- YOUR CODE FOR PROBLEM 2 HERE ---
def summarize_multiples(start_num, end_num, divisor):
  for num in range(start_num, end_num + 1):
    count += start_num
    tot_div = None
    if count % divisor == 0:
      tot_div += 1
      print(count)
      count += 1
    else:
      count += 1
  return tot_div

start = int(input('Please enter your start number: '))
end = int(input('Please enter your end number: '))
div = int(input('Please enter your divisor: '))
tot_count = summarize_multiples(start, end, div)

print(f'Found {tot_count} divisible by {div}.')


"""
================================================================================
PROBLEM 3: Correct Accumulator & Non-Zero Sentinel Initializer
================================================================================
Goal: Master accumulating values to calculate averages AFTER a loop finishes (rather than
compounding inside the loop), and use Sentinel value initialization (`None`) for min/max tracking.

Task:
Write a program that tracks high temperature readings for a week:
- Ask the user how many daily temperature readings they wish to enter (e.g., 5).
- Initialize `temp_sum = 0`, `lowest_temp = None`, and `highest_temp = None`.
- Use a `for` loop to prompt the user for each temperature reading.
- Inside the loop:
  * Add the reading to `temp_sum`.
  * Update `lowest_temp` and `highest_temp` using `None` checks (do NOT initialize lowest to 0!).
- AFTER the loop finishes:
  * Calculate `average_temp = temp_sum / count`.
  * Write a helper function `temp_advisory(temp)` that returns "Freezing" (< 32), "Mild" (32-75), or "Hot" (> 75).
  * Print the average temperature along with its advisory, as well as the highest and lowest temperatures recorded.
"""

# --- YOUR CODE FOR PROBLEM 3 HERE ---
readings = int(input('How many daily temperature readings do you wish to enter (e.g., 5)? '))
temp_sum = 0
lowest_temp = None
highest_temp = None
count = 0

for temp_sum in range(0, readings):
  reading = float(input('Enter reading: '))
  count += 1
  temp_sum += reading
  if reading < lowest_temp:
    lowest_temp = reading
  if reading > highest_temp:
    highest_temp = reading

average_temp = temp_sum / readings 

def temp_advisory(temp):
  if temp < 32:
    return 'Freezing'
  elif 32 <= temp <= 75:
    return 'Mild'
  else:
    return 'Hot'

advisory = temp_advisory(average_temp)

print(f'The average temperature is {average_temp} and {advisory}.\n The high temperature is {highest_temp} and the low temperature is {lowest_temp} from the readings.')

"""
================================================================================
PROBLEM 4: String Character Inspection & Guard Statements
================================================================================
Goal: Practice inspecting individual string characters without confusing whole-string methods
(e.g., `str.isdigit()`), and use clear `if/elif/else` returning.

Task:
Write a function named `analyze_username(username)` that validates a proposed username:
- Returns "Too Short" if username length is less than 5 characters.
- Returns "No Numbers" if the username contains zero numerical digits. (Loop through `username` character by character!).
- Returns "No Capitals" if the username contains zero uppercase letters.
- Returns "Valid" if it satisfies all three criteria (5+ chars, at least 1 digit, at least 1 uppercase letter).

Outside the function:
- Prompt the user to enter a username.
- Use a `while` loop that continues prompting the user until `analyze_username(user_input)` returns "Valid".
- Print "Username accepted!" once valid.
"""

# --- YOUR CODE FOR PROBLEM 4 HERE ---
def analyze_username(username):
  length = False
  has_digit = False
  has_capital = False
  if len(username) < 5:
    return 'Too short'
  else:
    length = True
  for char in username:
    if char.isdigit():
      has_digit = True
    else:
      return 'No numbers'
    if char.isupper():
      has_capital = True
    else:
      return 'No capitals'
  if length and has_capital and has_digit == True:
    return 'Valid'

u_name = input('Create a username containing at least 5 characters, one capital letter, and one number: ')
while analyze_username(u_name) != 'Valid':
  u_name = input('Please create a valid username with at least 5 characters, one capital letter, and one number: ')

print('Username accepted!')


"""
================================================================================
PROBLEM 5: Comprehensive Integration (Functions, Loop Control, & Accumulation)
================================================================================
Goal: Combine all core concepts from Lessons 1–3 into a unified script.

Task:
Write a mini-store inventory register system:
1. Write a function `calculate_discount_price(price, customer_type)`:
   - If `customer_type` is "VIP", apply a 20% discount (multiply price by 0.80).
   - If `customer_type` is "Member", apply a 10% discount (multiply price by 0.90).
   - Otherwise, return the original price.
   - Return the final discounted price rounded to 2 decimal places.

2. In the global code:
   - Prompt the user for customer type ("VIP", "Member", or "Standard").
   - Prompt the user for how many items they are purchasing.
   - Using a `for` loop, ask the user for the regular price of each item.
   - Use `calculate_discount_price()` inside the loop to get each item's final price.
   - Track `total_spent` and count how many items cost over $50 after discount.
   - At the end, display:
     * Total amount spent.
     * Average price per item.
     * Number of items that exceeded $50 after discount.
"""

# --- YOUR CODE FOR PROBLEM 5 HERE ---
def calculate_discount_price(price, customer_type):
  if customer_type == 'VIP':
    return round(price * .80, 2)
  elif customer_type == 'Member':
    return round(price * .90, 2)
  else:
    return price

c_type = input('Customer type (VIP, Member, Standard): ')
items = int(input('Enter number of items purchased: '))
total_spent = None
item = None
item_price_over = None
for item in range(0, items):
  item += 1
  item_price = float(input(f'Enter item {item} price: '))
  disc_item_price = calculate_discount_price(item_price, c_type)
  if disc_item_price > 50:
    item_price_over += 1
  total_spent += disc_item_price

avg_price_peritem = total_spent / items

print(f'You spent ${total_spent:.2f} at ${avg_price_peritem:.2f} per item and with {item_price_over} items over $50 after discount.')


"""
================================================================================
PROBLEM 6: Accumulator `0` vs. Sentinel `None` Guard Checks
================================================================================
Target Skill: Initialize totals to 0 and min/max sentinels to `None` (with `is None` guard checks).

Task:
Write a script that tracks rep counts across workout sets:
- Ask the user how many workout sets they completed (e.g., 4).
- Initialize `total_reps = 0`, `lowest_reps = None`, and `highest_reps = None`.
- Use a `for i in range(sets):` loop to prompt for reps completed in each set.
- Inside the loop:
  * Add reps to `total_reps`.
  * Update `lowest_reps` and `highest_reps` using `if lowest_reps is None or reps < lowest_reps:` checks.
- AFTER the loop finishes:
  * Calculate `average_reps = total_reps / sets`.
  * Print total reps, average reps per set (rounded to 1 decimal place), highest reps in a single set, and lowest reps in a single set.
"""

# --- YOUR CODE FOR PROBLEM 6 HERE ---
num_workout = int(input('How many workout sets have you completed? '))
total_reps = 0
lowest_reps = None
highest_reps = None
for i in range(num_workout):
  reps = int(input('Enter number of reps for workout: '))
  total_reps += reps
  if lowest_reps is None or reps < lowest_reps:
    lowest_reps = reps
  if highest_reps is None or reps > highest_reps:
    highest_reps = reps

average_reps = total_reps / num_workout
print(f'You completed {total_reps} reps across your workout with an average of {average_reps:.1f} reps per set. Your max reps was {highest_reps} and your low reps was {lowest_reps}.')

"""
================================================================================
PROBLEM 7: String Inspection Flags & Avoiding Premature Returns
================================================================================
Target Skill: Inspecting strings with boolean flags and returning status AFTER the loop completes.

Task:
Write a function named `validate_security_code(code_str)` that:
- Returns "Too Short" if `code_str` length is less than 6 characters.
- Uses a `for char in code_str:` loop to set boolean flags:
  * `has_special = True` if `char` is in `["!", "@", "#", "$"]`.
  * `has_digit = True` if `char.isdigit()`.
- AFTER the character inspection loop finishes:
  * Returns "Missing Special" if `has_special` is False.
  * Returns "Missing Digit" if `has_digit` is False.
  * Returns "Valid" if all criteria are satisfied.

Outside the function (Global Scope):
- Prompt the user to enter a security code.
- Use a `while` loop that continues prompting until `validate_security_code(user_code)` returns "Valid".
- Print "Security Code Accepted!" once valid.
"""

# --- YOUR CODE FOR PROBLEM 7 HERE ---
def validate_security_code(code_str):
  has_special = False
  has_digit = False
  length = False
  if len(code_str) >= 6:
    length = True
  for char in code_str:
    if char.isdigit():
      has_digit = True
    if char in ["!", "@", "#", "$"]:
      has_special = True
  if length is False:
    return 'Too Short'
  elif has_digit is False:
    return 'Missing Digit'
  elif has_special is False:
    return 'Missing Special'
  else:
    return 'Valid'

sc = input('Enter a security code that is at least 6 characters, has at least 1 number, and has at least 1 special character (!, @, #, $): ')
while validate_security_code(sc) != 'Valid':
  sc = input('Re-enter a security code that is at least 6 characters, has at least 1 number, and has at least 1 special character (!, @, #, $): ')

print('Security Code Accepted!')


"""
================================================================================
PROBLEM 8: Clean `for` Loop Indexing & Inclusive Range Bounds
================================================================================
Target Skill: Using inclusive `range(start, end + 1)` without manual counter increments or index shadowing.

Task:
Write a function named `sum_even_numbers(start_val, end_val)` that:
- Initializes `even_sum = 0` and `even_count = 0`.
- Iterates from `start_val` through `end_val` INCLUSIVE using `for num in range(start_val, end_val + 1):`.
- Inside the loop:
  * If `num` is even (`num % 2 == 0`), print `num`, add `num` to `even_sum`, and increment `even_count += 1`.
  * Do NOT manually increment `num` or add `num += 1` inside the loop!
- Returns a tuple `(even_sum, even_count)`.

Outside the function:
- Prompt the user for a starting number and an ending number.
- Call `sum_even_numbers(start_val, end_val)` and store the returned `total_sum, total_count`.
- Print: "Total sum of evens: X | Total count of evens: Y".
"""

# --- YOUR CODE FOR PROBLEM 8 HERE ---
def sum_even_numbers(start_val, end_val):
  even_sum = 0
  even_count = 0
  for num in range(start_val, end_val + 1):
    if num % 2 == 0:
      print(num)
      even_sum += num
      even_count += 1
  return (even_sum, even_count)

s = int(input('Enter a starting number: '))
e = int(input('Enter an ending number: '))
x, y = sum_even_numbers(s, e)
print(f'Total sum of evens: {x} | Total count of evens: {y}')



"""
================================================================================
PROBLEM 9: Speeding Evaluator & Post-Loop Statistics
================================================================================
Target Skill: Pure function classification, post-loop averages, and guarded min/max tracking.

Task:
1. Write a pure helper function `evaluate_speeding(speed, speed_limit)`:
   - Returns "Compliant" if speed <= speed_limit.
   - Returns "Minor Speeding" if speed is up to 15 mph over the limit.
   - Returns "Reckless" if speed is more than 15 mph over the limit.

2. In global scope:
   - Prompt the user for the posted speed limit (e.g. 55).
   - Prompt the user for how many cars were recorded by radar (e.g. 4).
   - Initialize `total_speed = 0`, `fastest_speed = None`, and `speeder_count = 0`.
   - Using a `for car_num in range(1, cars + 1):` loop:
     * Prompt for car speed.
     * Call `evaluate_speeding(car_speed, limit)` and print the car's evaluation.
     * Add `car_speed` to `total_speed`.
     * Update `fastest_speed` using a `None` guard check.
     * If evaluation is NOT "Compliant", increment `speeder_count += 1`.
   - AFTER the loop:
     * Compute `average_speed = total_speed / cars`.
     * Print average speed, fastest speed recorded, and total number of speeders.
"""

# --- YOUR CODE FOR PROBLEM 9 HERE ---
def evaluate_speeding(speed, speed_limit):
  if speed <= speed_limit:
    return 'Compliant'
  elif speed > speed_limit and speed <= speed_limit + 15:
    return 'Minor Speeding'
  else:
    return 'Reckless'

sl = int(input('Identify the speed limit: '))
cars = int(input('Identify how many cars were recorded by radar (e.g. 4): '))
total_speed = 0
speeder_count = 0
fastest_speed = None
for car_num in range(1, cars + 1):
  cs = float(input('Identify the car speed: '))
  if evaluate_speeding(cs, sl) != 'Compliant':
    speeder_count += 1
  total_speed += cs
  if fastest_speed is None or cs > fastest_speed:
    fastest_speed = cs

average_speed = total_speed / cars
print(f'The average speed was {average_speed}, the fastest speed was {fastest_speed:.1f}, and the total number of speeders was {speeder_count}')


"""
================================================================================
PROBLEM 10: PIN Security Validator & Bank Deposit Accumulator
================================================================================
Target Skill: Combining boolean flag string validation, global while loop, and deposit accumulator stats.

Task:
1. Write a function `is_valid_pin(pin_str)`:
   - Returns `False` if `len(pin_str) != 4`.
   - Uses a `for char in pin_str:` loop to verify that EVERY character is a digit. (If any char is NOT a digit, return `False`).
   - If length is 4 and all characters are digits, return `True`.

2. Global code:
   - Prompt user for 4-digit PIN in a `while` loop until `is_valid_pin(user_pin)` returns `True`.
   - Once valid, print "PIN Verified. Accessing Deposit System..."
   - Ask user how many checks they wish to deposit.
   - Initialize `total_deposited = 0`, `smallest_check = None`, and `large_check_count = 0`.
   - Using a `for check_num in range(1, total_checks + 1):` loop:
     * Prompt for check deposit amount.
     * Add amount to `total_deposited`.
     * Update `smallest_check` using a `None` guard check.
     * If check amount >= 1000, increment `large_check_count += 1`.
   - AFTER loop:
     * Compute `average_check = total_deposited / total_checks`.
     * Print total deposited amount, average check amount, smallest check deposited, and count of checks >= $1000.
"""

# --- YOUR CODE FOR PROBLEM 10 HERE ---
def is_valid_pin(pin_str):
  has_digits = 0
  length = False
  if len(pin_str) == 4:
    length = True
  for char in pin_str:
    if char.isdigit():
      has_digits += 1
  if length is False:
    return 'Need 4 Digits'
  elif has_digits != 4:
    return 'All must be Digits'
  else:
    return 'Valid'

pin = input('Enter a PIN that must be 4 digits: ')
while is_valid_pin(pin) != 'Valid':
  pin = input('Re-enter a PIN that must be 4 digits: ')
print('PIN Verified. Accessing Deposit System...')
float(total_deposited) = 0
float(smallest_check) = None
large_check_count = 0
for check_num in range(1, total_checks + 1):
  cda = float(input('Enter a check deposit ammount: '))
  total_deposited += cda
  if smallest_check is None or cda < smallest_check:
    smallest_check = cda
  if cda >= 1000:
    large_check_count += 1

print(f'The total deposited ammount is ${total_deposited:.2f}, the smallest check deposited is ${smallest_check:.2f}, and the count of checks greater than $1000 is {large_check_count}.')

