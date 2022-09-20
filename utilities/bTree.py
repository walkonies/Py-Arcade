class BinaryTree:
    def __init__(self, h, n):
        self.parent = h
        self.node = n
        self.left = None
        self.right = None
    def isLeaf(self):
        if self.left or self.right:
            return False
        return True
    def getLeft(self):
        l = None
        if self.left:
            l = self.left
        return l
    def getRight(self):
        r = None
        if self.right:
            r = self.right
        return r
    def addLeft(self, node):
        t = BinaryTree(self, node)
        self.left = t
    def addRight(self, node):
        t = BinaryTree(self, node)
        self.right = t
    def getParent(self):
        return self.parent
    def remChild(self, child):
        if self.left == child:
            self.left = None
        elif self.right == child:
            self.right = None
    def __str__(self):
        return f'BT {self.node}'

def preOrder(tree):
    if tree is None:
        return
    print(tree.node)#, end=' ')
    preOrder(tree.getLeft())
    preOrder(tree.getRight())

def inOrder(tree):
    if tree is None:
        return
    inOrder(tree.getLeft())
    print(tree.node, end=' ')
    inOrder(tree.getRight())
def postOrder(tree):
    if tree is None:
        return
    postOrder(tree.getLeft())
    postOrder(tree.getRight())
    print(tree.node, end=' ')

def levelOrder(tree):
    h = treeHeight(tree)
    for i in range(1, h+1):
        getLevel(tree, i)

def getLevel(tree, level):
    if tree is None:
        return
    if level == 1:
        print(tree.node)#, end=' ')
    getLevel(tree.left, level-1)
    getLevel(tree.right, level-1)
def treeHeight(tree):
    if tree is None:
        return 0
    l_height = treeHeight(tree.getLeft())
    r_height = treeHeight(tree.getRight())
    return  l_height+1 if l_height>r_height else r_height+1

def saveTree(file, tree):
    if tree is None:
        file.write('END\n')
        return
    file.write(str(tree.node))
    file.write('\n')
    saveTree(file, tree.getLeft())
    saveTree(file, tree.getRight())

def readTree(file, head):
    t = BinaryTree(head,0)
    lines = [line.strip() for line in file.readlines()]
    tree = makeTree(t, lines)
    return  t

def makeTree(head, lines):
    if len(lines) < 1:
        return
    node = lines.pop(0)
    if node == 'END':
        head.getParent().remChild(head)  # remove itself from parent
        return
    head.node = node
    head.addLeft(0)
    makeTree(head.getLeft(), lines)
    head.addRight(0)
    makeTree(head.getRight(), lines)

def step(tree):
    if tree is None:
        print('End')
        #step(tree.getParent())
    print(tree)
    nx = input(': ')
    if nx == 'q':
        return
    elif nx == 'p':
        step(tree.getParent())
    elif nx == 'l':
        step(tree.getLeft())
    else:
        step(tree.getRight())

def traverse(tree):
    inOrder(tree)
    print()
    preOrder(tree)
    print()
    postOrder(tree)
    print()
    levelOrder(tree)
    print()
def testRW(tree):
    traverse(tree)
    with open('file.txt', 'w') as f:
        saveTree(f, tree)
    tree_copy = None
    with open('file.txt', 'r') as f:
        tree_copy = readTree(f, None)
    traverse(tree_copy)

def main():
    t = BinaryTree(None, 1)
    t.addLeft(2)
    t.addRight(3)
    t.left.addLeft(4)
    t.left.addRight(5)

    t2 = None
    with open('file.txt', 'r') as f:
        t2 = readTree(f,None)
    #levelOrder(t2)
    preOrder(t2)
    step(t2)

if __name__ == '__main__':
    main()

