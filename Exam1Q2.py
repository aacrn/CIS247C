#Aaron Truong
# Exam 1 CIS 247 C

"""
Write a Python program that simulates the flipping of a coin. 
"""

import random

def flip_coin():
    return random.choice(['Heads', 'Tails'])

def get_user_choice():
    while True:
        choice = input("Choose Heads or Tails (H/T): ").strip().upper()
        if choice in ['H', 'T']:
            return 'Heads' if choice == 'H' else 'Tails'
        else:
            print("Invalid input. Please enter 'H' for Heads or 'T' for Tails.")

def main():
    results = []
    correct_count = 0
    for i in range(8):
        user_choice = get_user_choice()
        coin_result = flip_coin()
        if user_choice == coin_result:
            correct_count += 1
            results.append('Y')
        else:
            results.append('N')
    print("Throw      Correct\n")
    for idx, correct in enumerate(results, 1):
        print(f"{idx:<10}{correct}\n")
    print(f"Display % Correct  {correct_count / 8 * 100:.1f}%")

main()