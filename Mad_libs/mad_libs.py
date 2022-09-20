import os
from time import sleep
directory = os.path.join(os.getcwd(),os.path.dirname(__file__))

'''
  Comments:
    Dictionary = no repeat questions // change to array?
    Can get answers as getting questions
    Can rewrite as getting answers
    INEFFICIENT
'''


def play(mad_lib):
	questions = GetQ(mad_lib)
	answers = GetA(questions)
	text = mad_lib
	for i in range(len(mad_lib)):
		if mad_lib[i] == '<':
			start = i + 1
		if mad_lib[i] == '>':
			end = i
			q = mad_lib[start:end]
			text = text[:text.find('<')] + answers[q] + mad_lib[end + 1:]
	print('\nGenerating story...\n')
	sleep(1.5)
	print(text)
	
def GetA(quest):
	answers = dict()
	for q in quest:
		answers[q] = input('Enter a ' + q +': ')
	return answers
    
def GetQ(data):
	questions = []
	for i in range(len(data)):
		if data[i] == '<':
			start = i + 1
		if data[i] == '>':
			questions.append(data[start:i])
	return questions

def main():
	f = os.path.join(directory, 'mad_lib_party.txt')
	file = open(f, 'r')
	text = file.read()
	play(text)


main()

