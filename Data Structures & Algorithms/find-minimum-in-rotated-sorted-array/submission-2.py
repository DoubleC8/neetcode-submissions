class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_val = 1001

        while l <= r:
            if nums[l] < nums[r]:
                min_val = min(min_val, nums[l])
                l += 1
            else:
                min_val = min(min_val, nums[r])
                r -= 1

        return min_val