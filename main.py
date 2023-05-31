from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

test = QuizBrain(question_bank)
test.next_question()