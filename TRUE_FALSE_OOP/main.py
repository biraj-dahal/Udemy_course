
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(each["question"], each["correct_answer"]) for each in question_data['results']]
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("Congratulations on completing the Quiz.")
print(f"Your Final Score was {quiz.score}/{quiz.question_number + 1}")

