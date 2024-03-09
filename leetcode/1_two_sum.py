class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create dict for store difference
        hashmap = dict()
        
        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in hashmap:
                return [hashmap[diff], i]
            
            hashmap[num] = i
            
        return None
