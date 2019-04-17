class Node(object):

    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


root = Node()
n1 = Node()
n2 = Node()
n3 = Node()
n4 = Node()
n5 = Node()
n6 = Node()
root.data = "root"
root.left = n1
root.right = n2

n1.data = 1
n2.data = 2

n1.left = n3
n1.right = n4

n3.data = 3
n4.data = 4

n2.left = n5
n2.right = n6

n5.data = 5
n6.data = 6

def traverse(root):
    if root != None:
        print(root.data)
        traverse(root.left)
        traverse(root.right)

traverse(root)

