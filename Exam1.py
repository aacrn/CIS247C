# Aaron Truong
# Exam 1 CIS 247 C

"""
Write a Python program that calculates a basketball player’s average scoring over a period of games.
"""

def get_score():
    while True:
        try:
            score = int(input("Enter the player's score for a game: "))
            if score < 0:
                print("Score cannot be negative. Please enter a valid score.")
            else:
                return score
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def perform_calculations(scores):
    if not scores:
        return 0, 0, 0
    average = sum(scores) / len(scores)
    high = max(scores)
    low = min(scores)
    return average, high, low

def main():
    try:
        num_games = int(input("How many games did the player play? "))
        scores = []
        for _ in range(num_games):
            score = get_score()
            scores.append(score)
        average, high, low = perform_calculations(scores)
        print("\n+----------------+-------+")
        print("|   Statistic    | Value |")
        print("+----------------+-------+")
        print(f"| Average score  | {average:5.2f} |")
        print(f"| High score     | {high:5} |")
        print(f"| Low score      | {low:5} |")
        print("+----------------+-------+")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

main()