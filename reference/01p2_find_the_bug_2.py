import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# ==================
# DEBUGGING PRACTICE
# ==================

# 1. PRACTICE
# find the bug! What kind of bug is this?
# note this one is harder. You might find referencing what was printed out 
# useful.

def calculate_average(numbers):
    sum_numbers = 0
    for number in numbers:
        sum_numbers += number
    avg = sum_numbers / len(numbers)
    return avg

numbers_lists = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 10], [11, 12, 13], [14], [15, 16, 17, 18, 19, 20], [21, 22], [23, 24, 25], [26, 27, 28, 29, 30], [31, 32, 33], [34, 35, 36, 37], [], [38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]]

for numbers in numbers_lists:
    average = calculate_average(numbers)
    print(f"The average of {numbers} is: {average}")

# SOLUTION:
# The error is caused by one of the list of numbers being empty,
# so it is dividing by zero
    

