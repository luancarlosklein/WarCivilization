import random

class Goal():
    def __init__(self, np):
        self.mission = random.randint (1,6)
        self.type = random.randint (1,4)
        self.opponent = random.randint (1,100)%np +1
    
    def show (self):
        return 0

