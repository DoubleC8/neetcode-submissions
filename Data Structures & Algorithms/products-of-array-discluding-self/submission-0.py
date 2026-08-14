class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = 1
        pre_arr = [1 for _ in range(n)]
        post = 1
        post_arr = [1 for _ in range(n)]
        res = [1 for _ in range(n)]

        for i in range(n):
            pre_arr[i] *= pre
            pre *= nums[i]

        for i in range(n - 1, -1, -1):
            post_arr[i] *= post
            post *= nums[i]
        
        for i in range(n):
            res[i] *= pre_arr[i] * post_arr[i]
        
        return res