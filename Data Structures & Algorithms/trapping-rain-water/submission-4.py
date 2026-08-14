class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_l, max_r = 0, 0
        l = 0
        r = n - 1
        trapped = 0

        while l < r:
            max_l = max(max_l, height[l])
            max_r = max(max_r, height[r])

            if max_l <= max_r:
                trapped += max(0, max_l - height[l])
                l += 1
                
            elif max_l > max_r:
                trapped += max(0, max_r - height[r])
                r -= 1

        
        return trapped
            


            


            

                    





