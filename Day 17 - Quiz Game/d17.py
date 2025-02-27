from data import question_data
from question import Question
from quiz_brain import QuizBrain
from html import unescape

q_bank = []
for question in question_data:
    q_bank.append(
        Question(question['type'],
                 question['difficulty'],
                 question['category'],
                 unescape(question['question']),
                 question['correct_answer'],
                 question['incorrect_answers']))

quiz_brain = QuizBrain(q_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f'Your final score is: {quiz_brain.score}/{quiz_brain.question_number}')

