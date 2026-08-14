from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        l = 0
        r = 0
        res = []
        # is going to filled of indices
        q = deque()

        while r < n:
            # while q is not empty and the value at r is 
            # greater than the right most value in our deque 
            # we pop the values
            # while smaller values exist in our deque, we pop the values
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # after removing all small values, we can add our bigger value
            q.append(r)

            # if our left value is out of bounds
            # we remove the the left most value
            if l > q[0]:
                q.popleft()
            
            # checking that our window is at least size k
            # we only update l when our window is at least size k
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1

            r += 1

        return res 