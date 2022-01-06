def CountSubArray(Array, n, k):
    count = 0
    for i in range(0, n):
        if(Array[i] < k):
            count += 1
        mul = Array[i]
        for j in range(i+1, n):
            mul = mul * Array[j]
            if(mul < k):
                count += 1
            else:
                break
    return count


n = int(input("How many Number You want to Enter in Array:"))
Array = []
for i in range(n):
    i = int(input())
    Array.append(i)
k = int(input("Value Of K:"))
print(Array)
print("Output:", CountSubArray(Array, n, k))
