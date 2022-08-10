class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        match_count = 0

        for idx in range(len(items)):
            type, color, name = items[idx][0], items[idx][1], items[idx][2]
            if ruleKey == "type" and ruleValue == type:
                match_count += 1
            elif ruleKey == "name" and ruleValue == name:
                match_count += 1
            elif ruleKey == "color" and ruleValue == color:
                match_count += 1

        return match_count
