# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

# find the bug!

def calculate_average(numbers):
    sum_numbers = 0
    for number in numbers:
        sum_numbers += number
    avg = sum_numbers / len(numbers)
    return avg

numbers_list = [10, 20, 30, 40, 50]


average = calculate_averge(numbers_list)
print(f"The average is: {average}")

# The error is on line 27, the function name is misspelled.


