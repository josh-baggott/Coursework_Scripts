# imports
import json
import random


# classes
class Question:

    def __init__(self):
        self.question_json = self.open_questions()

        self.question = None
        self.answer_A = None
        self.answer_B = None
        self.answer_C = None
        self.answer_D = None
        self.correct_answer = None

    # functions

    def validate_input(quiz_length):
        try:
            int(quiz_length)
        except ValueError:
            raise ValueError("Input Must be an Integer")

        if int(quiz_length) > 4:
            raise ValueError("Value Too Large")
        if int(quiz_length) <= 0:
            raise ValueError("Value Too Small")

        return int(quiz_length)

    def open_questions(self):
        """
        This function opens the .json file into a dictionary containg all of the possible questions that can be used in the quiz

        :return: A dictionary containing all of the questions
        """
        with open("Questions_JSON.json") as json_file:
            self.question_json = json.load(json_file)

        return self.question_json

    def configure_questions(self, question, number):
        """
        This function configures the attributes of each question object based on the number which has been passed into the function from the list of random numbers

        :param question:
        :param number:
        :return: The question once its attributes have been configured
        """
        question.question = self.question_json[number][0]
        question.answer_A = self.question_json[number][1]
        question.answer_B = self.question_json[number][2]
        question.answer_C = self.question_json[number][3]
        question.answer_D = self.question_json[number][4]
        question.correct_answer = self.question_json[number][5]

        return question

    def display_questions(self, question, count):
        """
        This function takes each question and prints each attribute in turn

        :param question: The question whose attributes are to be printed
        :param count: The question number
        :return: N/A
        """

        print("Question " + str(count + 1) + ":")
        print(question.question)
        print(question.answer_A)
        print(question.answer_B)
        print(question.answer_C)
        print(question.answer_D)
        print("")

    def mark_questions(self, user_inputs, correct_answers):
        """
        This function takes the user inputs and compares them to the correct answer attribute in each of the question objects.

        :param user_inputs: A list of answers that have been given by the user.
        :param question_list: A list of question objects which have been selected based on the list of randomly generated numbers.
        :return:    score: The number of questions that the user answered correctly.
                    percentage: The percentage score from the quiz, calculated from the length of the quiz and the user score.
                    correct_questions: A list containing the questions from the quiz that the user answered correctly.
                    incorrect_questions: A list containing the questions from the quiz that the user answered incorrectly.
                    incorrect_questions_corrections: A list containing the correct answers to the questions in the list incorrect_questions.

        """

        score = 0
        count = 0

        correct_questions = []
        incorrect_questions = []
        incorrect_questions_corrections = []

        for answer in user_inputs:
            if answer == correct_answers[count]:
                score += 1
                correct_questions.append(count + 1)
            else:
                incorrect_questions.append(count + 1)
                incorrect_questions_corrections.append(correct_answers[count])
            count += 1

        percentage = round((score / count) * 100, 2)

        return score, percentage, correct_questions, incorrect_questions, incorrect_questions_corrections,


# global functions

def generate_numbers(quiz_length):
    """
    This function generates a list of random numbers all of which are unique. The length of this list is the length of the quiz which the user has specified.

    :param quiz_length: The length of the quiz/length of the list
    :return: A list of unique random numbers
    """

    generated_numbers_list = []

    for i in range(0, quiz_length):
        number = random.randint(1, 92)

        while number in generated_numbers_list:
            number = random.randint(1, 92)

        generated_numbers_list.append(number)

    return generated_numbers_list


# main
if __name__ == "__main__":
    quiz_length = Question.validate_input(input("Enter Quiz Length: "))

    question_list = []

    for i in range(0, quiz_length):
        question_list.append(Question())

    generated_numbers_list = generate_numbers(quiz_length)

    count = 0

    for question in question_list:
        question.display_questions(question.configure_questions(question, str(generated_numbers_list[count])), count)

        count += 1

    user_inputs = []

    count = 1

    for question in question_list:
        user_inputs.append(input("Enter Answer for Question " + str(question_list.index(question) + 1) + ":"))
        count += 1

    previous_score = 0
    previous_percentage = 0

    correct_answers = []

    for question in question_list:
        correct_answers.append(question.correct_answer)

    print(correct_answers)

    score, percentage, correct_questions, incorrect_questions, incorrect_questions_corrections, = question.mark_questions(user_inputs, correct_answers)

    print("Score: " + str(score) + "/" + str(len(user_inputs)))

    print("Percentage: " + str(percentage) + "%")

    print("")

    print("Questions Answered Correctly: " + str(correct_questions))
    print("Questions Answered Incorrectly: " + str(incorrect_questions))

    count = 0

    for incorrect in incorrect_questions:
        print("Correct Answer for Question " + str(incorrect_questions[incorrect - 1]) + ": " + str(incorrect_questions_corrections[count]))
        count += 1
