class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        max_len = 0

        for num in setNums:
            cur_len = 1
            # we check if the num is the start of the seq
            if (num -  1) not in setNums:
                while (num + 1) in setNums:
                    cur_len += 1
                    num += 1
            
            max_len = max(max_len, cur_len)
        
        return max_len