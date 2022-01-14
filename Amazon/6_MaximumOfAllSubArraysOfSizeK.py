from collections import deque


def max_of_subarrays(arr, n, k):
    queue = deque()
    result = []
    for i in range(k):
        while queue and arr[i] > queue[-1][0]:
            queue.pop()
        queue.append((arr[i], i))
    result.append(queue[0][0])

    for i in range(1, n-k+1):
        if (i+k-1) - queue[0][1] > k-1:
            queue.popleft()
        while queue and arr[i+k-1] > queue[-1][0]:
            queue.pop()
        queue.append((arr[i+k-1], i+k-1))
        result.append(queue[0][0])

    return result


arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
n = len(arr)
k = 3
res = max_of_subarrays(arr, n, k)
for i in range(len(res)):
    print(res[i], end=" ")
print()
