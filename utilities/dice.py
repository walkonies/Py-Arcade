from random import choice

class Die:
	sides = 6
	def __init__(self):
		self.reset()
	def reset(self):
		self.current_val = 0
		self.times_rolled = 0
		self.history = []
	def getVal(self):
		return self.current_val
	def roll(self):
		if self.current_val:
			self.history.append(self.current_val)
		num = choice(self.getPossibleVals())
		self.current_val = num
		self.times_rolled += 1
	def getPossibleVals(self):
		vals = [i for i in range(1,self.sides+1)]
		return vals
	def getCount(self):
		count = {num : 0 for num in self.getPossibleVals()}
		for elem in self.history:
			count[elem]+=1
		return count
	def getDistribution(self):
		count = self.getCount()
		d = {key : f'{round(elem / len(self.history)*100)}%' for key, elem in count.items()}
		return d
	def setSides(self, num):
		self.sides = num
		self.reset()

class Dice:
	def __init__(self, num):
		self.num_dice = num if num > 1 else 1
		self.dice = []
		self.reset()
	def reset(self):
		self.dice = [Die() for _ in range(self.num_dice)]
	def roll(self):
		for die in self.dice:
			die.roll()
	def getTotal(self):
		total = sum(self.getDice())
		return total
	def addDie(self):
		self.dice.append(Die())
		self.num_dice += 1
	def getDice(self):
		dice = [d.getVal() for d in self.dice]
		return dice
	def getCount(self):
		counts = [d.getCount() for d in self.dice]
		return counts
	def getDistribution(self):
		dists = [d.getDistribution() for d in self.dice]
		return dists
	def getHistory(self):
		history = [d.history for d in self.dice]
	def setSides(self, num):
		for d in self.dice:
			d.setSides(num)

def main():
	d = Dice(2)
	d.setSides(6)
	for i in range(10000):
		d.roll()
	print(d.getCount())
	print(d.getDistribution())
	for i in range(3):
		d.roll()
		print(d.getDice(), '->', d.getTotal())
		
if __name__ == '__main__':
	main()