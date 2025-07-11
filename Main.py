#Aaron Truong
#Final Exam CIS 247 C

from Question import Question

def main():
    questions = [
        Question(
            "Which planet is known as the 'Red Planet'?",
            ["Earth", "Venus", "Mars", "Jupiter", "Saturn"],
            2
        ),
        Question(
            "How far is the Earth from the Sun?",
            ["10 million miles", "93 million miles", "4.2 light years", "2 AU", "1 inches"],
            1
        ),
        Question(
            "Which planet is the coldest?",
            ["Uranus", "Mercury", "Earth", "Mars", "Neptune"],
            0
        ),
        Question(
            "Which planet is the hottest?",
            ["Earth", "Mars", "Venus", "Saturn", "Neptune"],
            2
        )
    ]

    score1 = 0
    score2 = 0

    for idx, q in enumerate(questions, 1):
        print(f"\nQuestion {idx}:")
        print(q)
        try:
            guess1 = int(input("Player 1, enter your answer (1-5): "))
            guess2 = int(input("Player 2, enter your answer (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        correct1 = q.check_answer(guess1)
        correct2 = q.check_answer(guess2)

        print(f"Player 1 {'correct!' if correct1 else 'incorrect.'}")
        print(f"Player 2 {'correct!' if correct2 else 'incorrect.'}")

        if correct1:
            score1 += 1
        if correct2:
            score2 += 1

    print("\nFinal Scores:")
    print(f"Player 1: {score1}")
    print(f"Player 2: {score2}")

main()

