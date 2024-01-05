

# Updating some text using pycharm
print("hello world")

# Inheritence Demo In Python

class Animal:
    def __init__(self):
        self.Eyes = 2
    
    def breath(self):
        print("Inhaling and Exhaling")

class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.food = "water"
    
    def swim(self):
        print("I am swimming inside water")

nano = Fish()
print(nano.food)
nano.swim()
nano.breath()
