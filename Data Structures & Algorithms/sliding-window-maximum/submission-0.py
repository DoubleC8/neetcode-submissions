class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        l = 0 
        window = []
        res = []

        for i in range(k):
            window.append(nums[i])
        
        max_num = max(window)
        res.append(max_num)

        for r in range(k, n):
            window.remove(nums[r-k])
            window.append(nums[r])
            print("window: ", window)
            max_num = max(window)
            res.append(max_num)

        return res

        