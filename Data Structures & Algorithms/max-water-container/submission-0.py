class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            cur_area = 0
            if heights[l] < heights[r]:
                cur_area = heights[l] * (r - l)
                l += 1
            elif heights[l] > heights[r]:
                cur_area = heights[r] * (r - l)
                r -= 1
            else:
                cur_area = heights[r] * (r - l)
                r -= 1
            max_area = max(max_area, cur_area)
        
        return max_area