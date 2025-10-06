from helper_functions import clear_screen
clear_screen()

# ===========
# ERROR TYPES
# ===========

'''
OVERVIEW
--------

There are 3 types of errors to know about, Syntax, Runtime, and Logical errors.

This is a largely conceptual chapter, but I also include some practice
examples to try and find errors in existing code.

'''


# =============
# SYNTAX ERRORS
# =============

'''
syntax error: you typed something that doesn't follow the rules of the
programming language.

Think of it like making a grammatical error in English, like not ending a
sentence with a period. When you break the syntax rules of python, it doesn't
know how to run your code.
'''

# 1. SYNTAX ERROR EXAMPLE
# Example: What is the syntax error here?
# Answer: missing a colon
if 5 > 2
    print("Five is greater than two!")

# 2. SYNTAX ERROR EXAMPLE
# Example: What is the syntax error here?
# Answer: invalid variable name (starts with a number)
1_variable = 2

# 3. SYNTAX ERROR EXAMPLE
# Example: What is the syntax error here?
# Answer: Forgot to end the quotes
if 5 > 2:
    print("Five is greater than two!)


'''
HOW TO FIX SYNTAX ERRORS
------------------------

1. Python checks for syntax errors before running, so if you try to run it and
   it doesn't work, that's your first clue

2. look for red squigglies

3. When running your code, look for the line number where the error occured
   when your program crashes. Look at that line of code and try to see what is
   happening. You can also search the internet for the error or ask an AI.
'''
 
# ==============
# RUNTIME ERRORS
# ==============

'''
Runtime error: syntax is correct, but when running the program tries to do an
illegal / impossible operation.

A SYNTAX error happens when Python can't understand what you are saying.
A RUNTIME error happens when Python understands what you are saying, but runs
into trouble when following your instructions.

Examples:
    - Dividing something by 0
    - referencing a function or variable that doesn't exist
      (but the syntax of the function or variable is valid)
    - Trying to convert an input into something invalid
      (e.g. trying to turn "asdf" into an int)
    - Trying to reference or pull data from a file that doesn't exist
    - Trying to store an extremely large value in a variable and your
      computer doesn't have enough memory to store it.

Think of it like trying to bake a cake. The recipe was written perfectly,
but when following it you realize your oven isn't actually big enough and can't
get hot enough to handle cooking the cake.
'''
# 4. RUNTIME ERROR EXAMPLE
# Example: What causes a runtime error here?
# Answer: Function prin doesn't exist.
prin("Hello, World!")

# 5. RUNTIME ERROR EXAMPLE
# Example: What causes the runtime error here?
# Answer: dividing by zero
result = 100 / 0

# 6. RUNTIME ERROR EXAMPLE
# Example: What could cause a runtime error here?
# Answer: If you provide improper input for int.
user_input = int(input("Enter a valid number please: "))


'''
HOW TO FIX RUNTIME ERRORS
-------------------------

1. Sometimes, you can see yellow squigglies (but this is usually just for
   NameErrors. Most runtime errors won't have yellow lines.)    

2. test multiple inputs
    0's, negative numbers, strings if they're expecting a number,
    using gigantic numbers, etc.

3. Have one person write code, have another person test it TRYING to break it.

4. Exception handling. This is the next chapter we'll go over.
'''

# ==============
# LOGICAL ERRORS
# ==============

'''
Logical Error: The program runs, no syntax or runtime errors, but doesn't do
what you intended it to do. Most insidious error. Hard to catch.

Think of giving your friend directions to reach your house. Except at one turn,
you told them to go left instead of right. The instructions were clearly stated
and understood, but they don't actually lead your friend to your house.
    
'''
# 7. LOGICAL ERROR EXAMPLE
# Example: Is there a logical error here?
# Answer: Assuming we want to actually calulate the average, yes.
def calculate_average(a, b):
    return (a + b) / a 

print(calculate_average(20, 22))

# 8. LOGICAL ERROR EXAMPLE
# Example: Is this likely a logical error?
# Answer: Yes, we want to check whether somehting isn't 5, so there isn't
#         alignment in the logic of the if statement and what prints.
x = 5
if x != 5:
    print("x is 5")


'''
HOW TO FIX LOGICAL ERRORS
-------------------------

1. Create test cases.
    E.g. for that first example, calculate manually what the average of 20 and
    22 should be, then compare it to what your program outputs

2. Print out the variables at different points in your program.
    If you realize something is wrong, but don't know exactly where it is going
    wrong, try printing out the variable that is messed up every time you do
    something to it.

3. Use debugger to watch the variables that aren't working as you think they should.
    Slowly step through your program and find out the exact moment when
    something occurs with a variable that you didn't expect.
'''
