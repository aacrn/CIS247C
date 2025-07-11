#Aaron Truong
#Final Exam Question CIS 247 C

class Question:
    def __init__(self, question_text, options, answer_index):
        self.question_text = question_text
        self.options = options
        self.answer_index = answer_index

    def __str__(self):
        options_str = "\n".join([f"{i + 1}. {option}" for i, option in enumerate(self.options)])
        return f"{self.question_text}\n{options_str}"

    def check_answer(self, guess):
        return guess == self.answer_index + 1  # Convert to 1-based index for comparison    
    