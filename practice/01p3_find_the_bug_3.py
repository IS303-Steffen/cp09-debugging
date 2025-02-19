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
# What is wrong with this code?
# This code is supposed to calculate the total scores of Team A and Team B
# and show who won.

# For example, if one team has scores of [1, 2, 3] their
# total score should be 6.

'''
Before starting, think:
    given team_a_scores and team_b_scores,
    who should win? What should the total scores be?
'''

# Scores for each member of Team A and Team B
team_a_scores = [85, 90, 78, 92, 85]
team_b_scores = [80, 85, 88, 86, 90]

# Function to calculate total score of a team
def calculate_total_score(scores):
    total_score = 0
    for score in scores:
        total_score += score
    return score

# Function to determine the winning team
def determine_winner(team_a_total, team_b_total):
    if team_a_total >= team_b_total:
        print("Team A wins!")
    elif team_b_total < team_a_total:
        print("Team B wins!")
    else:
        print("It's a tie!")

# Calculate total scores for each team
team_a_total = calculate_total_score(team_a_scores)
team_b_total = calculate_total_score(team_b_scores)

# Print the total scores (with the logical error present)
print(f"Team A Total Score: {team_a_total}")
print(f"Team B Total Score: {team_b_total}")

# Determine and print the winner
determine_winner(team_a_total, team_b_total)

