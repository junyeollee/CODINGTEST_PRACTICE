# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {'}':'{', ']':'[', ')':'('}
        for cnt_bracket in s:
            if cnt_bracket not in map:
                stack.append(cnt_bracket)
            elif cnt_bracket in map and len(stack) !=0:
                if map[cnt_bracket] != stack.pop():
                    return False
            else:
                return False
        return len(stack) == 0
