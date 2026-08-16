class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        l = 0
        r = n - 1

        while l < r:
            curr_height = min(heights[l], heights[r])
            curr_width = r - l 
            curr_area = curr_height * curr_width 
            max_area = max(max_area, curr_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area