from collections import defaultdict


def Anagrams(words):
    duplicateList = defaultdict(list)

    for word in words:
        duplicateList["".join(sorted(word))].append(word)

    for group in duplicateList.values():
        print(" ".join(group))


if __name__ == "__main__":
    words = ["abc", "acb", "bba", "on", "no", "is"]
    Anagrams(words)
