class Tree(object):

    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

root = Tree()
root.data = "root"
root.left = Tree()
root.left = "left"
root.right = Tree()
root.right = "right"

print()