def maxDivide(a, b):
    while a % b == 0:
        a = a / b
    return a


def CheckUgly(no):
    no = maxDivide(no, 2)
    no = maxDivide(no, 3)
    no = maxDivide(no, 5)
    return 1 if no == 1 else 0


def getUglyNo(n):
    i = 1
    count = 1

    while n > count:
        i += 1
        if CheckUgly(i):
            count += 1
    return i


n = int(input("Enter Nth No:"))
no = getUglyNo(n)
print(n, "th ugly no. is: ", no)
