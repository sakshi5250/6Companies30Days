class node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def toSumTree(Node):

    if(Node == None):
        return 0

    old_val = Node.data

    Node.data = toSumTree(Node.left) + \
        toSumTree(Node.right)

    return Node.data + old_val


def printInorder(Node):
    if (Node == None):
        return
    printInorder(Node.left)
    print(Node.data, end=" ")
    printInorder(Node.right)


def newNode(data):
    temp = node(0)
    temp.data = data
    temp.left = None
    temp.right = None

    return temp


if __name__ == "__main__":
    root = None
    x = 0

    root = newNode(10)
    root.left = newNode(-2)
    root.right = newNode(6)
    root.left.left = newNode(8)
    root.left.right = newNode(-4)
    root.right.left = newNode(7)
    root.right.right = newNode(5)

    toSumTree(root)

    print("Inorder Traversal of the resultant tree is: ")
    printInorder(root)
