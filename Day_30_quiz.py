import random

class FruitQuiz:

    def __init__(self):

        self.fruits={'apple':'red',
                     'orange':'orange',
                     'watermelom':'green', 'banana':'yellow'}
        
    def quiz(self):
        while (True):
                     
            fruit, color = random.choice(list(self.fruits.items()))

            print("what is the color of {}".format(fruit))
            user_answer = input()

            if(user_answer.lower() == color):
                    print("correct asnswer")
                
            else:
                    print("wrong answer")

            option = int(input("enter 0 , if you want to play agian otherwise enter 1: "))

            if (option):
                    break
                
print("welcome to fruit quiz ")
fq = FruitQuiz()
fq.quiz()
