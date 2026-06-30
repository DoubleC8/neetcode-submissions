class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_pre = 1
        r_pre = 1
        n = len(nums)
        
        l_arr = [1 for _ in range(n)]
        r_arr = [1 for _ in range(n)]

        for i in range(n):
            l_arr[i] *= l_pre
            l_pre *= nums[i]
        
        for i in range(n - 1, -1, -1):
            r_arr[i] *= r_pre
            r_pre *= nums[i]
        
        res = [1 for _ in range(n)]

        for i in range(n):
            res[i] *= l_arr[i] * r_arr[i]

        return res

