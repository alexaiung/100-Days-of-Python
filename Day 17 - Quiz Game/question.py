class Question:
    def __init__(self, type, difficulty, category, question, correct_answer, incorrect_answers):
        self.type = type
        self.difficulty = difficulty
        self.category = category
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
