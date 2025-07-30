class fruit:

    def __init__(self, name, color):
        self.name = name
        self.color = color
    def intro(self):
            print("hello, i am", self.name)
apple = fruit('Apple','Red')

apple.intro()