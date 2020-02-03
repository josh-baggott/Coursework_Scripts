import random

questions = {
    1: ["Question 1", "A: Answer A", "B: Answer B", "C: Answer C", "D: Answer D", "A"],
    2: ["Question 2", "A: Answer A", "B: Answer B", "C: Answer C", "D: Answer D", "B"],
    3: ["Question 3", "A: Answer A", "B: Answer B", "C: Answer C", "D: Answer D", "C"],
    4: ["Question 4", "A: Answer A", "B: Answer B", "C: Answer C", "D: Answer D", "D"],
    5: ["Question 5", "A: Answer A", "B: Answer B", "C: Answer C", "D: Answer D", "A"],
    6: ["Question 6", "A: Answer A", "B: Answer B", "C: Answer C", "D: Answer D", "B"],
    7: ["Question 7", "A: Answer A", "B: Answer B", "C: Answer C", "D: Answer D", "C"],
    8: ["Question 8", "A: Answer A", "B: Answer B", "C: Answer C", "D: Answer D", "D"],
    9: ["Question 9", "A: Answer A", "B: Answer B", "C: Answer C", "D: Answer D", "A"],
    10: ["Question 10", "A: Answer A", "B: Answer B", "C: Answer C", "D: Answer D", "B"]}


# functions


def generate_questions(quiz_length):
    question_list = []

    generated_numbers_list = generate_numbers(quiz_length)

    for number in generated_numbers_list:
        question_list.append(questions[number])

    return question_list


def generate_numbers(quiz_length):
    generated_numbers_list = []

    for i in range(0, quiz_length):
        number = random.randint(1, 10)

        while number in generated_numbers_list:
            number = random.randint(1, 10)

        generated_numbers_list.append(number)

    return generated_numbers_list


def display_questions(question_list):
    for i in range(0, len(question_list)):
        print("Question", str(i + 1))
        for j in range(1, 5):
            print(question_list[i][j])
        print("")


def mark_questions(user_answers, question_list):
    score = 0
    count = 0

    correct_answers = []
    incorrect_answers = []

    for answer in user_answers:
        if answer == question_list[count][5]:
            score += 1
            correct_answers.append(count + 1)
        else:
            incorrect_answers.append(count + 1)
        count += 1

    percentage = round((score / count) * 100, 2)

    return score, percentage, correct_answers, incorrect_answers


# main


if __name__ == "__main__":
    user_answers = []

    quiz_length = int(input("Enter Quiz Length: "))

    while quiz_length > 10:
        print("Too Large")
        quiz_length = int(input("Enter Quiz Length: "))

    question_list = generate_questions(quiz_length)

    display_questions(question_list)

    for question in question_list:
        user_answers.append(input("Enter Answer for Question " + str(question_list.index(question) + 1) + ": "))

    print("")

    score, percentage, correct_answers, incorrect_answers = mark_questions(user_answers, question_list)

    print("Score: " + str(score) + "/" + str(len(user_answers)))

    print("Percentage: " + str(percentage) + "%")

    print("")

    print("Questions Answered Correctly: " + str(correct_answers))
    print("Questions Answered Incorrectly: " + str(incorrect_answers))
