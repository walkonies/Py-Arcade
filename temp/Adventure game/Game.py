class Game:
    def __init__(self, nme):
        self.name = nme
        self.question = []
        self.answers = []
        self.choice = 0
        self.belt = []
        self.money = 10
        self.items = 0

    def getQuestions(self, index):
        return self.question[index]
    def getAwnsers(self, index):
        return [self.answers[index*2], self.answers[(index*2)+1]]
    def getBelt(self):
        return self.belt
    def addItem(self, item):
        self.belt.append(item)
    def removeItem(self, item):
        self.belt.remove(item)
    def getName(self):
        return self.name
    def addMoney(self, num):
        self.money += num
    def getMoney(self):
        return self.money
