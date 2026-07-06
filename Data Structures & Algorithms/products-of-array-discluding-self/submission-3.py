class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_arr = [1 for _ in range(n)]
        pre = 1
        r_arr = [1 for _ in range(n)]
        post = 1

        for i in range(n):
            l_arr[i] *= pre
            pre *= nums[i]
        
        for i in range(n-1, -1, -1):
            r_arr[i] *= post
            post *= nums[i]
        
        res = [1 for _ in range(n)]

        for i in range(n):
            res[i] *= l_arr[i] * r_arr[i]


        return res
        


