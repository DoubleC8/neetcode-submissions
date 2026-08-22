from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)
        buckets = [[] for _ in range(n + 1)]
        res = []

        for num in nums:
            freq[num] += 1

        for key, val in freq.items():
            buckets[val].append(key)
        
        for i in range(len(buckets) - 1, -1, -1):
            for j in buckets[i]:
                res.append(j)
                print(res)
                if len(res) == k:
                    return res