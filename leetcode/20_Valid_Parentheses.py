from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) <= 1:
            return False

        stack = deque()

        brackets_map = {"(": ")", "[": "]", "{": "}"}

        for bracket in s:
            if bracket in list(brackets_map.keys()):
                stack.append(bracket)
            else:
                if not len(stack) or brackets_map[stack.pop()] != bracket:
                    return False

        return len(stack) < 1
