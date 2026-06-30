from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        n = len(nums)
        buckets = [[] for i in range(n + 1)] 
        res = []

        for num in nums:
            count_dict[num] += 1
        
        for key, value in count_dict.items():
            buckets[value].append(key)
        
        for i in range(n, - 1, -1):
            for j in buckets[i]:
                res.append(j)
            if len(res) == k:
                return res
