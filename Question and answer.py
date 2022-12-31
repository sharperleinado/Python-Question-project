from question_model import Question

question_prompt = ["1. How many colours has a rainbow?" + "\n (a) 5 (b) 7 (c) 10 ",
"\n 2. How many letters are there in a rainbow?" + "\n (a) 6 (b) 9 (c) 7 ",
"\n 3. What is colour has an orange?" + "\n (a) Yellow (b) Blue (c) Green ",
"\n 4. Which is the bravest of the animals?" + "\n (a) Donkey (b) Monkey (c) Lion ",
"\n 5. Which of the countries is in West Africa?" + "\n (a) Angola (b) Rwanda (c) Nigeria "]

questions = [Question(question_prompt[0], "b"),
              Question(question_prompt[1], "c"),
              Question(question_prompt[2], "a"),
              Question(question_prompt[3], "c"),
              Question(question_prompt[4], "c")]

def run_check(questions):
    score = 0
    for question in questions:
        answer = input(question.question)
        if answer == question.answer:
            score += 1
                    
    print("You got " + str(score) + "/" + str(len(question_prompt)) + " correct")


run_check(questions)


question_box = ["1. How many planets are there in the solar system?\n(a) 12\n(b) 7\n(c) 9\n\n",
                "2. How many colours are there in a rainbow?\n(a) 4\n(b) 5\n(c) 7\n\n",
                "3. Which of these planets is the coldest?\n(a) Mars\n(b) Venus\n(c) Pluto\n\n",
                "4. Which of these planets is the hottest?\n(a) Jupiter\n(b) Mecury\n(c) Earth\n\n ",
                "5. Which of these animals is the fastest?\n(a) Zebra\n(b) Tiger\n(c) Cheetah\n\n"]

question = [Question(question_box[0], "a"),
            Question(question_box[1], "c"),
            Question(question_box[2], "c"),
            Question(question_box[3], "b"),
            Question(question_box[4], "c")]

