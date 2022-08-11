class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        consistent_strings = 0
        allowed_set = set(allowed)
        for idx, word in enumerate(words):

            word_set = set(word)
            intersection_set = allowed_set.intersection(word_set)

            if len(intersection_set) == len(word_set):
                consistent_strings += 1

        return consistent_strings
