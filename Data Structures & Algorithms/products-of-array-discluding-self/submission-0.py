class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        l_index = 1
        l_arr = [1] * n
        r_index = 1
        r_arr = [1] * n
        
        res = [1] * n

        for i in range(n):
            l_arr[i] *= l_index
            l_index *= nums[i]
        
        for i in range(n - 1, - 1, -1):
            r_arr[i] *= r_index
            r_index *= nums[i]

        for i in range(n):
            res[i] = l_arr[i] * r_arr[i]

        return res

