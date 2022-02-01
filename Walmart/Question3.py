def winnerOfGame(colors):

    count_A = count_B = 0

    for i in range(1, len(colors) - 1):
        if colors[i-1] == colors[i] == colors[i+1] == 'A':
            count_A += 1

        if colors[i-1] == colors[i] == colors[i+1] == 'B':
            count_B += 1

    return count_A > count_B


colors = "AAABABB"
print(winnerOfGame(colors))
