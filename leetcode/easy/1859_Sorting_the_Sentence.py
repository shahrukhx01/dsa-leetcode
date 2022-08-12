class Solution:
    def sortSentence(self, s: str) -> str:

        words = s.split(" ")
        wordsCount = len(words)
        sorrtedSentence = [None] * wordsCount
        for idx in range(0, wordsCount):
            word = words[idx][:-1]
            index = int(words[idx][-1])
            sorrtedSentence[index - 1] = word

        return " ".join(sorrtedSentence)
