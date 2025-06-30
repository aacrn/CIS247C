#Aaron Truong
#Homework 3 CIS 247 C

"""
Write a Python program that manages bowling scores. The program should allow the user to:
1. View all Scores: Display all recorded scores with their corresponding dates.
2. Add a Score: Input a new score along with the date (month and day). Ensure that scores are between 0 and 300, and that no scores exist for the same date.
3. Average Scores: Calculate and display the average of all recorded scores.
4. Number of 300s: Count and display how many times a perfect score of 300 has been recorded.
5. Quit: Exit the program.
"""

import os
def view_scores(filename):
    if not os.path.exists(filename):
        print("No scores available. Please add scores first.")
        return
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            month = parts[0]
            day = parts[1]
            scores = ', '.join(parts[2:])
            print(f"On {month} {day}, you scored {scores}")
def score_exists_for_date(filename, month, day):
    if not os.path.exists(filename):
        return False
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if parts[0] == month and parts[1] == day:
                return True
    return False

def add_score(filename):
    month = input("Enter the month: ")
    day = input("Enter the day (1-31): ")
    if not (1 <= int(day) <= 31):
        print("Invalid day. Please enter a day between 1 and 31.")
        return
    scores = input("Enter the scores (0-300) separated by spaces: ").split()
    for score in scores:
        if not (0 <= int(score) <= 300):
            print("Invalid score. Please enter scores between 0 and 300.")
            return
    if score_exists_for_date(filename, month, day):
        print("Scores for this date already exist.")
        return
    with open(filename, 'a') as file:
        file.write(f"{month} {day} {' '.join(scores)}\n")

    print("Scores added successfully.")

def average_scores(filename):
    if not os.path.exists(filename):
        print("No scores available to calculate average.")
        return
    total_score = 0
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            scores = list(map(int, parts[2:]))
            total_score += sum(scores)
            count += len(scores)
    if count == 0:
        print("No valid scores available to calculate average.")
        return
    average = total_score / count
    print(f"Average score: {average:.2f}")

def num_300s(filename):
    if not os.path.exists(filename):
        print("No scores available to count 300s.")
        return
    count_300s = 0
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            scores = list(map(int, parts[2:]))
            count_300s += scores.count(300)
    print(f"Number of 300s: {count_300s}")

def main():
    filename = "data\\scores.txt"
    while True:
        print("\nMenu:")
        print("1. View all Scores")
        print("2. Add a Score")
        print("3. Average Scores")
        print("4. Number of 300s")
        print("5. Quit")
        choice = input("Select an option (1-5): ")
        if choice == '1':
            view_scores(filename)
        elif choice == '2':
            add_score(filename)
        elif choice == '3':
            average_scores(filename)
        elif choice == '4':
            num_300s(filename)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

main()