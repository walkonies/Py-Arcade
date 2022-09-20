class node:
    def __init__(self, num, question, p=None):
        self.question = question
        self.left = None #path one
        self.right = None
        self.num = num
        if p:
            self.setParent(p)
        else:
            self.setParent(None)

    def IsLeaf(self):
        return NumChildren() == 0
    
    def NumChildren(self):
        if self.left == None:
            return 0
        if self.right == None:
            return 1
        else:
            return 2
    def setParent(self, p):
        self.p = p

    def __str__(self):
        return self.question
class GameTree:
    def __init__(self):
        self.root = None
        self.current = None
        
    def IsEmpty(self):
        if self.root == None:
            return True
        return False
    
    def nextNode(self, root):
        if IsEmpty():
            return None
        while root.left != None:
            root = root.left
        return root
            
    def add_node(self, question):
        new_node = node(question)
        next_node = nextNode(self.root)
        next_node.left = new_node
        if question.question[0] == '$':
            return
        else:
            add_node()
            add_node()
            
        
