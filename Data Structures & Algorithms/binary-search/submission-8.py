class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2 # 6 / 2 = 3
        left = 0
        right = len(nums) - 1 # 6 - 1 = 5
        result = -1
        if target == nums[mid]: # target = 12 == nums[3] = 5 false
            result = mid
            return result
        elif target > nums[mid]: # target = 12 > nums[3] = 5 true left = 4
            left = mid + 1
        elif target < nums[mid]: # target = 2 < nums[1] = 5 false right = 5
            right = mid - 1
        
        for x in range(left,right + 1): # x in range(4,5)
            if nums[x] == target: 
                result = x
        if (left == right and target == nums[left]):
            result = left
        return result


