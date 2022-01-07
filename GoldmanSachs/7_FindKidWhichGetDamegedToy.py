def FindKidWhichGetDamegedToy(n, m, k):

    if (m <= n - k + 1):
        return m + k - 1

    m = m - (n - k + 1)

    if(m % n == 0):
        return n
    else:
        return m % n


n = 5  # No of kids
m = 2  # No of Toy
k = 1  # Random No from where distribution should started
print(FindKidWhichGetDamegedToy(n, m, k))
