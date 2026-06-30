class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        setNums = set(nums)

        for num in setNums:
            if (num - 1) not in setNums:
                cur_len = 1
                while num + cur_len in setNums:
                    cur_len += 1
                max_len = max(max_len, cur_len)

        return max_len
