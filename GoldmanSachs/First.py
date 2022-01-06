from collections import defaultdict


def Anagrams(arr):
    grpWords = defaultdict(list)

    for word in arr:
        grpWords["".join(sorted(word))].append(word)

    for group in grpWords.values():
        print(" ".join(group))


if __name__ == "__main__":
    words = ["abc", "acb", "bba", "on", "no", "is"]
    Anagrams(words)
