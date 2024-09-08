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
# note this one is harder. You might find referencing what was printed out useful.

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



