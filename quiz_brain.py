
class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list

    def still_has_questions(self):
        length = len(self.questions_list)
        return self.question_number < length

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {question.text} (True/False): ")

