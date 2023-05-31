
class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list

    def next_question(self):
        index = self.question_number
        question = self.questions_list[index]
        index += 1
        answer = input(f"Q.{index}: {question.text} (True/False): ")

