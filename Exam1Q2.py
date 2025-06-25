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
            results.append((i + 1, 'Y'))
        else:
            results.append((i + 1, 'N'))
    print("\n+-------+--------+")
    print("| Throw | Correct|")
    print("+-------+--------+")
    for throw, correct in results:
        print(f"| {throw:<5} | {correct:<6} |")
    print("+-------+--------+")
    print(f"Display % Correct  {correct_count / 8 * 100:.1f}%")

main()