class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        n = len(set_nums)
        max_len = 0
        i = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                curr_len = 1
                curr_num = num
                while (curr_num + 1) in set_nums:
                    curr_len += 1
                    curr_num += 1
                max_len = max(max_len, curr_len)
            else:
                continue 

        return max_len  
        