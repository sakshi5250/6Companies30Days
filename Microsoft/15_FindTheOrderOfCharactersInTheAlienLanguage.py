import collections


def topological_sort(nodes_map, nodes):
    def recursion(nodes_map, node, result, visited):
        if node in visited:
            return
        visited.append(node)
        if node in nodes_map:
            for c in nodes_map[node]:
                recursion(nodes_map, c, result, visited)
        result.append(node)

    visited, result = [], []
    for node in nodes.keys():
        recursion(nodes_map, node, result, visited)
    return reversed(result)


words = ["baa", "abcd", "abca", "cab", "cad"]
chars = collections.OrderedDict()
for word in words:
    for c in word:
        chars[c] = True

nodes_map = collections.defaultdict(list)
for i, word in enumerate(words[:-1]):
    nxt = words[i+1]
    for a, b in zip(word, nxt):
        if a != b:
            nodes_map[a] += [b]
            break
for i in topological_sort(nodes_map, chars):
    print(i)
