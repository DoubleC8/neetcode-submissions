class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        setNums = set(nums)

        for num in setNums:
            # i.e. num is start of seq
            if not (num - 1) in setNums:
                cur_len = 1
                # while num + 1 in set, we increment the cur_len
                while num + 1 in setNums:
                    cur_len += 1
                    num += 1
                max_len = max(max_len, cur_len)
        
        return max_len
    
