class Solution:
    def findOrder(self, numCourses, prerequisites):

        adjacencyList = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            adjacencyList[course].append(prereq)

        entries = [i for i in range(numCourses)]

        path = [False for i in range(numCourses)]

        result = []

        stack = []

        while entries:

            if not stack:
                stack.append((entries.pop(), False))

            while stack:

                curr, returned = stack.pop()

                if curr in result:
                    continue

                elif returned:
                    result.append(curr)
                    path[curr] = False

                elif path[curr]:
                    return []
                else:

                    stack.append((curr, True))

                    path[curr] = True

                    for prereq in adjacencyList[curr]:
                        stack.append((prereq, False))

        return result


obj = Solution()
numCourses = 2
prerequisites = [[1, 0]]
print(obj.findOrder(numCourses, prerequisites))
