#!/usr/bin/env python3
"""
AI2C Python Lesson 5 — Task 2: Analyze File Numbers (No min/max built-ins)

Instructions:
1. Initialize variables:
   - 'total_sum' to 0 (to calculate the average)
   - 'count' to 0
   - 'min_val' to None (we will set this to the first number we read)
   - 'max_val' to None
2. Open 'numbers.txt' in read mode ('r') using a 'with open()' block.
3. Loop through each line in the file.
4. Clean the line (remove whitespace/newlines) and convert it to an integer.
5. In the loop, update your statistics for each number:
   - Add to 'total_sum' and increment 'count'.
   - If 'min_val' and 'max_val' are None, initialize them to this first number.
   - Otherwise, compare the number: if it is smaller than 'min_val', update 'min_val'. If larger than 'max_val', update 'max_val'.
6. After the loop, calculate the average (total_sum / count).
7. Print the min, max, and average.
"""

# TODO: Step 1 — Initialize tracking variables


# TODO: Step 2 — Open "numbers.txt" in read mode


# TODO: Step 3 — Loop through lines, convert to integers, and update min/max/sum/count manually


# TODO: Step 4 — Calculate average and print results (min, max, average)

