from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq[num] += 1
    
        for key, value in freq.items():
            buckets[value].append(key)
        
        res = []
        n = len(buckets)

        for i in range(n - 1, -1, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res