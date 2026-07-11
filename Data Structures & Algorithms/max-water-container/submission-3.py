class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            base = r - l
            height = min(heights[l], heights[r])
            cur_area = base * height
            max_area = max(max_area, cur_area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1
        
        return max_area