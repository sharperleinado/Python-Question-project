class Question():

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check(self):

        if self.answer != "a" or self.answer != "b" or self.answer != "c":
            return f"{self.answer} is a wrong option input."
        #elif self.answer =! "b":
        #    return f"{self.answer} is a wrong option input."
        #elif self.answer =! "c":
        #    return f"{self.answer} is a wrong option input."
