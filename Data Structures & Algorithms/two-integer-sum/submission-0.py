from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        comp_dict = defaultdict()

        for i in range(n):
            complement = target - nums[i]
            if complement in comp_dict:
                return [comp_dict[complement], i]
            else:
                comp_dict[nums[i]] = i 