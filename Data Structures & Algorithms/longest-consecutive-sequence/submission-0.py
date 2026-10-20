class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_len = 0

        for num in nums:
            if (num - 1) in set_nums:
                continue 
            
            curr_len = 1
            curr_num = num

            while (curr_num + 1) in set_nums:
                curr_len += 1
                curr_num += 1
            
            max_len = max(max_len, curr_len)
        
        return max_len