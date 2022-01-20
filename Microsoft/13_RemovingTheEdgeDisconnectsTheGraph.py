class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFS(self, v, visited):

        visited[v] = True

        i = 0
        while i != len(self.adj[v]):
            if (not visited[self.adj[v][i]]):
                self.DFS(self.adj[v][i], visited)
            i += 1

    def isConnected(self):
        visited = [False] * self.V

        self.DFS(0, visited)

        for i in range(1, self.V):
            if (visited[i] == False):
                return False

        return True

    def isBridge(self, u, v):

        indU = self.adj[v].index(u)
        indV = self.adj[u].index(v)
        del self.adj[u][indV]
        del self.adj[v][indU]

        res = self.isConnected()

        self.addEdge(u, v)

        return (res == False)


if __name__ == '__main__':

    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)

    if g.isBridge(2, 3):
        print("Yes")
    else:
        print("No")
