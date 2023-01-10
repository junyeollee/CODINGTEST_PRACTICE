# https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        i = len(s) - 1
        result = 0

        while s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            result += 1
            i -= 1

        return result
