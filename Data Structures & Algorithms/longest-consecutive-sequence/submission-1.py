class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        seen = set()
        n = len(nums)

        for num in nums:
            seen.add(num)

        for i in range(n):
            curr_len = 1
            while (nums[i] + 1) in seen:
                curr_len += 1
                nums[i] += 1
            
            max_len = max(max_len, curr_len)
        
        return max_len