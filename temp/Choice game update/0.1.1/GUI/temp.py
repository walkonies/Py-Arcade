from tree_class import node

file = []
head = node(0,'Hello world')



def read():
	cur = head
	num = 0
	dead = 'dead'
	#dead = "gameOver(name)"
	run = True

	while run:
		num +=1
		line = input(f'L{num}: ')
		if line != dead:
			cur.left = node(num, line, cur)
			cur = cur.left
		else:
			cur.left = 'dead'

			line = input(f'R{num}: ')

			if line == dead:
				cur.right = 'dead'
				cur = cur.p.p
				if cur == head and head.right:
					run = False
					break

			else:
				cur.right = node(num, line, cur)
				cur = cur.right
		printTree(head)
		print('*\n*\n*')

def printTree(head):
	if head == 'dead':
		return
	print(head)
	print('left: ', end = '')
	printTree(head.left)
	print('right: ', end = '')
	printTree(head.right)

def traverse(head):
	node = head
	switch = ''
	while switch != 'q':
		print(node)
		switch = input()

		if switch == 'l':
			node = node.left
		elif switch == 'r':
			node = node.right
		elif switch == 'p':
			node = node.p

def test():
	a = node(0, 'a')
	b = node(1, 'b', head)
	c = node(2,'c', head)
	end = 'dead'
	head.left=b
	head.right=c
	b.left= end
	b.right=end
	c.left = c.right = end
	traverse(head)
# mid
# left
# 

def main():
	read()
	traverse(head)
if __name__ == '__main__':
	main()