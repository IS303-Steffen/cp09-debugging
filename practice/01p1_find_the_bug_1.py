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


