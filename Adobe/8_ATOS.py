

def myAtoi(string):
    res = 0
    sign = 1
    i = 0

    if string[0] == '-':
        sign = -1
        i += 1

    for j in range(i, len(string)):
        res = res*10+(ord(string[j])-ord('0'))

    return sign * res


string = "-123"


print(myAtoi(string))
