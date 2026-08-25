# Corrected Reference Solutions for Targeted Review Practice Problems 1–5
# Location: Python/Lesson 03 - Functions/targeted_review_solutions.py

"""
================================================================================
PROBLEM 1 SOLUTION: Pure Processor Function
================================================================================
Key Takeaway: Function receives local parameters, does math, and returns result.
Inputs and outputs stay in the global scope.
"""
def calculate_fuel_efficiency(distance_miles, fuel_gallons):
    mpg = distance_miles / fuel_gallons
    return round(mpg, 1)

# Global scope hand-off
mi = float(input('Enter total distance traveled (miles): '))
gal = float(input('Enter total fuel used (gallons): '))
trip_mpg = calculate_fuel_efficiency(mi, gal)

print(f'On this trip, your vehicle had an efficiency rate of {trip_mpg} MPG.')


"""
================================================================================
PROBLEM 2 SOLUTION: For Loop with range() & Divisor Counting
================================================================================
Key Takeaway: Initialize counter to 0 BEFORE the loop. `for num in range()`
automatically holds the current loop number—no manual `count += 1` needed!
"""
def summarize_multiples(start_num, end_num, divisor):
    tot_div = 0  # Initialize accumulator to 0 before loop
    for num in range(start_num, end_num + 1):  # +1 to include end_num
        if num % divisor == 0:
            tot_div += 1
            print(num)
    return tot_div

# Global scope
start = int(input('Please enter your start number: '))
end = int(input('Please enter your end number: '))
div = int(input('Please enter your divisor: '))

tot_count = summarize_multiples(start, end, div)
print(f'Found {tot_count} numbers divisible by {div}.')


"""
================================================================================
PROBLEM 3 SOLUTION: Post-Loop Accumulator & Sentinel Initializers
================================================================================
Key Takeaways:
1. Initialize counters/sums to 0 (`temp_sum = 0`).
2. Initialize min/max sentinels to `None` and check `if lowest_temp is None or reading < lowest_temp:`.
3. Compute average AFTER the loop finishes.
"""
def temp_advisory(temp):
    if temp < 32:
        return 'Freezing'
    elif 32 <= temp <= 75:
        return 'Mild'
    else:
        return 'Hot'

# Global scope setup
readings = int(input('How many daily temperature readings do you wish to enter (e.g., 5)? '))
temp_sum = 0
lowest_temp = None
highest_temp = None

for i in range(readings):  # Use clean index 'i' (do NOT reuse 'temp_sum' as index!)
    reading = float(input(f'Enter reading #{i + 1}: '))
    temp_sum += reading
    
    # Sentinel None checks
    if lowest_temp is None or reading < lowest_temp:
        lowest_temp = reading
    if highest_temp is None or reading > highest_temp:
        highest_temp = reading

# Calculate average AFTER loop
average_temp = temp_sum / readings
advisory = temp_advisory(average_temp)

print(f'The average temperature is {average_temp:.1f}°F ({advisory}).')
print(f'High: {highest_temp}°F | Low: {lowest_temp}°F')


"""
================================================================================
PROBLEM 4 SOLUTION: String Inspection & Global Validation Loop
================================================================================
Key Takeaways:
1. Inspect entire string with a `for char in username:` loop to set boolean flags (`has_digit`, `has_capital`).
2. Evaluate flags and return status AFTER the string loop completes (don't return inside loop!).
3. Global `while` loop continuously prompts until function returns "Valid".
"""
def analyze_username(username):
    if len(username) < 5:
        return 'Too short'
    
    has_digit = False
    has_capital = False
    for char in username:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_capital = True
            
    if not has_digit:
        return 'No numbers'
    if not has_capital:
        return 'No capitals'
    return 'Valid'

# Global loop
u_name = input('Create a username (5+ chars, 1 capital, 1 digit): ')
while analyze_username(u_name) != 'Valid':
    status = analyze_username(u_name)
    u_name = input(f'[{status}] Please enter a valid username: ')

print('Username accepted!')


"""
================================================================================
PROBLEM 5 SOLUTION: Comprehensive Store Inventory & Discount System
================================================================================
Key Takeaways:
1. Pure function `calculate_discount_price` computes rounded price.
2. Initialize totals (`total_spent = 0`) and counters (`item_price_over = 0`) to 0.
3. Use `for item_num in range(1, items + 1):` for clean 1-based item labels.
"""
def calculate_discount_price(price, customer_type):
    if customer_type == 'VIP':
        return round(price * 0.80, 2)
    elif customer_type == 'Member':
        return round(price * 0.90, 2)
    else:
        return price

# Global scope
c_type = input('Customer type (VIP, Member, Standard): ').strip()
items = int(input('Enter number of items purchased: '))

total_spent = 0        # Accumulator starts at 0
item_price_over = 0    # Counter starts at 0

for item_num in range(1, items + 1):
    item_price = float(input(f'Enter item {item_num} price: $'))
    disc_item_price = calculate_discount_price(item_price, c_type)
    
    total_spent += disc_item_price
    if disc_item_price > 50:
        item_price_over += 1

avg_price_per_item = total_spent / items

print(f'\nTotal spent: ${total_spent:.2f}')
print(f'Average price per item: ${avg_price_per_item:.2f}')
print(f'Items costing over $50 (after discount): {item_price_over}')
