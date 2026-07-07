class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_len = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                cur_len = 1
                while num + 1 in set_nums:
                    cur_len += 1
                    num += 1
                
                max_len = max(max_len, cur_len)
            else:
                continue
        
        return max_len