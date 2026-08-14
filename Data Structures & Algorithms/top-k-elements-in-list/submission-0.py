from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        n = len(nums)
        buckets = [[] for _ in range(n+1)]

        for num in nums:
            freq[num] += 1

        for key, val in freq.items():
            buckets[val].append(key)
        
        res = []

        for i in range(len(buckets) - 1, -1, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res