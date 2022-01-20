class Solution():
    def canFinish(self, numCourses, prerequisites):
        if numCourses == 0 or len(prerequisites) == 0:
            return True
        g = []
        for i in range(numCourses):
            g.append([])

        inDegree = [0] * (numCourses)
        for i, j in prerequisites:
            inDegree[j] = inDegree[j] + 1
            g[i].append(j)
        q = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.insert(0, i)
        cnt = 0
        while q:
            i = q.pop()
            for neigh in g[i]:
                if inDegree[neigh] > 0:
                    inDegree[neigh] = inDegree[neigh] - 1
                    if inDegree[neigh] == 0:
                        q.insert(0, neigh)
            cnt = cnt + 1
        if cnt == numCourses:
            return True
        return False


numCourses = 2
prerequisites = [[1, 0]]
obj = Solution()
print(obj.canFinish(numCourses, prerequisites))
