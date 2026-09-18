class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set(nums)
        y = False
        if len(x) != len(nums):
            y = True
        return y