# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid) -> 'Node':
        def process(r1, r2, c1, c2):
            cnt0 = 0
            cnt1 = 0
            for i in range(r1, r2):
                for j in range(c1, c2):
                    if grid[i][j] == 0:
                        cnt0 += 1
                    else:
                        cnt1 += 1
            if cnt0 == 0:
                node = Node(1, True)
                return node
            if cnt1 == 0:
                node = Node(0, True)
                return node
            node = Node(0, False)
            node.topLeft = process(r1, (r1 + r2)//2, c1, (c1+c2)//2)
            node.topRight = process(r1, (r1 + r2)//2, (c1+c2)//2, c2)
            node.bottomLeft = process((r1 + r2)//2, r2, c1, (c1+c2)//2)
            node.bottomRight = process((r1 + r2)//2, r2, (c1+c2)//2, c2)
            return node
        if len(grid) == 0:
            return None
        return process(0, len(grid), 0, len(grid))
