class getNode:
    def __init__(self, data):

        self.data = data
        self.left = self.right = None


def countSubtreesWithSumX(root, count, x):

    if (not root):
        return 0

    ls = countSubtreesWithSumX(root.left,
                               count, x)

    rs = countSubtreesWithSumX(root.right,
                               count, x)

    Sum = ls + rs + root.data

    if (Sum == x):
        count[0] += 1

    return Sum


def countSubtreesWithSumXUtil(root, x):

    if (not root):
        return 0

    count = [0]

    ls = countSubtreesWithSumX(root.left,
                               count, x)

    rs = countSubtreesWithSumX(root.right,
                               count, x)

    if ((ls + rs + root.data) == x):
        count[0] += 1

    return count[0]


if __name__ == '__main__':
    root = getNode(5)
    root.left = getNode(-10)
    root.right = getNode(3)
    root.left.left = getNode(9)
    root.left.right = getNode(8)
    root.right.left = getNode(-4)
    root.right.right = getNode(7)

    x = 7

    print("Count =",
          countSubtreesWithSumXUtil(root, x))
