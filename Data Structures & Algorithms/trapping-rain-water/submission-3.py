class Solution:
    def trap(self, height: List[int]) -> int:
        len_height = len(height)
        max_l, max_r = 0, 0
        max_l_arr, max_r_arr = [], [0 for j in range(len_height)]
        trapped = 0

        for i in range(len_height):
            max_l = max(max_l, height[i])
            max_l_arr.append(max_l)

        for j in range(len_height - 1, -1, -1):
            max_r = max(max_r, height[j])
            max_r_arr[j] = max_r
        
        for i in range(len_height):
            trapped += min(max_l_arr[i], max_r_arr[i]) - height[i]


        return trapped


            

                    





