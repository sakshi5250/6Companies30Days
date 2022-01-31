def pacificAtlantic(arr):
    if not arr or not arr[0]:
        return []

        
    pacific = set()
    atlantic = set()
    
    m, n = len(arr), len(arr[0])

    
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    
    def dfs(visited, x, y):
        visited.add((x, y))
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

           
            if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited and arr[new_x][new_y] >= arr[x][y]:
                dfs(visited, new_x, new_y)

        
    for i in range(m):
        dfs(pacific, i, 0)
        dfs(atlantic, i, n-1)

        
    for j in range(n):
        dfs(pacific, 0, j)
        dfs(atlantic, m-1, j)

        
    return list(pacific.intersection(atlantic))


arr = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
    2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(pacificAtlantic(arr))
