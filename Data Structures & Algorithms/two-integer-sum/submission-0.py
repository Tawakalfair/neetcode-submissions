class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nilai = {}
        for (i,j) in enumerate(nums):
            diference = target - j
            if diference in nilai:
                return [nilai[diference], i]
            
            nilai[j] = i  