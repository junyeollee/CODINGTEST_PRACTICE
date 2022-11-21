class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, 0 , -1):
            nums[i] == nums[i-1] and nums.pop(i)
        return len(nums)
