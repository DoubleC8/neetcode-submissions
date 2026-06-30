class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            base = r - l
            height = min(heights[l], heights[r])
            cur_area = base * height

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
            max_area = max(max_area, cur_area)
        
        return max_area