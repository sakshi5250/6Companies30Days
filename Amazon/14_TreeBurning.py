class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Info:
    def __init__(self):
        self.lDepth = 0
        self.rDepth = 0
        self.contains = False
        self.time = -1


class Solution:

    res = 0

    def calcTime(self, node, info, target):

        if node == None:
            return info

        if node.left == None and node.right == None:

            if node.val == target:
                info.contains = True
                info.time = 0
            return info

        leftInfo = Info()
        leftInfo = self.calcTime(node.left, leftInfo, target)

        rightInfo = Info()
        rightInfo = self.calcTime(node.right, rightInfo, target)

        info.time = leftInfo.time + \
            1 if (node.left and leftInfo.contains) else -1

        if info.time == -1:
            info.time = rightInfo.time + \
                1 if (node.right and rightInfo.contains) else -1

        info.contains = (node.left and leftInfo.contains) or (
            node.right and rightInfo.contains)

        info.lDepth = 0 if (not node.left) else (
            1+max(leftInfo.lDepth, leftInfo.rDepth))

        info.rDepth = 0 if (not node.right) else (
            1+max(rightInfo.lDepth, rightInfo.rDepth))

        if info.contains:
            if node.left and leftInfo.contains:

                self.res = max(self.res, info.time+info.rDepth)

            if node.right and rightInfo.contains:

                self.res = max(self.res, info.time+info.lDepth)

        return info

    def solve(self, root, target):
        info = Info()
        self.calcTime(root, info, target)
        return self.res


if __name__ == '__main__':

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(9)
    root.left.left.left = TreeNode(10)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(12)
    root.left.right.left.left = TreeNode(11)

    target = 10

    s = Solution()
    print(s.solve(root, target))
