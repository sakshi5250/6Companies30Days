hashTable = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def printWordUtil(number, curr, output, n):
    if(curr == n):
        print(output)
        return
    for i in range(len(hashTable[number[curr]])):
        output.append(hashTable[number[curr]][i])
        printWordUtil(number, curr+1, output, n)
        output.pop()
        if (number[curr] == 0 or number[curr] == 1):
            return


def printWord(number, n):
    printWordUtil(number, 0, [], n)


number = [2, 3, 4]
n = len(number)
printWord(number, n)
