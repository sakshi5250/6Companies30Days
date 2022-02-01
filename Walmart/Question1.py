from collections import defaultdict, deque


def FindMaximumProb(edges, probability, start, end):
    g = defaultdict(list)
    for i in range(len(edges)):
        src, dst = edges[i][0], edges[i][1]
        prob = probability[i]
        g[src].append((dst, prob))
        g[dst].append((src, prob))
    q = deque()
    q.append((start, 1))
    visited = defaultdict(int)
    while q:
        node, prob = q.popleft()
        if visited[node] > prob:
            continue
        else:
            visited[node] = prob
        for adj, nextProb in g[node]:
            if visited[adj] < prob * nextProb:
                q.append((adj, prob * nextProb))
    return visited[end]


edges = [[0, 1], [1, 2], [0, 2]]
probability = [0.5, 0.5, 0.2]
start = 0
end = 2
print(FindMaximumProb(edges, probability, start, end))
