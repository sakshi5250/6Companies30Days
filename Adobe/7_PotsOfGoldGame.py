def findMaxCoins(coin, i, j):

    if i == j:
        return coin[i]

    if i + 1 == j:
        return max(coin[i], coin[j])

    start = coin[i] + min(findMaxCoins(coin, i + 2, j),
                          findMaxCoins(coin, i + 1, j - 1))

    end = coin[j] + min(findMaxCoins(coin, i + 1, j - 1),
                        findMaxCoins(coin, i, j - 2))

    return max(start, end)


if __name__ == '__main__':

    coin = [4, 6, 2, 7]

    print('The maximum coins collected by player is',
          findMaxCoins(coin, 0, len(coin) - 1))
