class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        start_idx = 0
        result = 0
        
        for i, c in enumerate(s):
            if len(s) - start_idx + 1 <= result:
                return result
            else:
                start_idx = max(start_idx, hashmap.get(c, 0))
                hashmap[c] = i + 1
            
            result = max(result, i - start_idx + 1)
                
        return result
