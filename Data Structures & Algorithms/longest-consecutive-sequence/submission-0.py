class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_len = 0

        for num in set_nums:
            curr_num = num
            curr_len = 0
            # This implies curr_nums is the first in seq
            if (curr_num - 1) not in set_nums:
                curr_len = 1
                while (curr_num + 1) in set_nums:
                    curr_len += 1
                    curr_num += 1
                max_len = max(max_len, curr_len)
            else:
                continue
        
        return max_len
