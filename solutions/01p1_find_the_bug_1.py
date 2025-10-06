from helper_functions import clear_screen
clear_screen()

# ==================
# DEBUGGING PRACTICE
# ==================


# 1. PRACTICE
# find the bug! What kind of bug is it?

def calculate_average(numbers):
    sum_numbers = 0
    for number in numbers:
        sum_numbers += number
    avg = sum_numbers / len(numbers)
    return avg

numbers_list = [10, 20, 30, 40, 50]


average = calculate_averge(numbers_list)
print(f"The average is: {average}")

# SOLUTION:
# The error is on line 27, the function name is misspelled.


