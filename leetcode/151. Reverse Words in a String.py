# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution1:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ''

        for c in s:
            if c == ' ':
                if len(word) != 0:
                    words.append(word)
                word = ''
            else:
                word += c
   
        if len(word) != 0:
            words.append(word)

        return ' '.join(reversed(words))

      
import re
class Solution2:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(re.sub(' +',' ',s).split(' '))).strip()
