from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        for key, value in count.items():
            buckets[value].append(key)
        
        res = []

        for i in range(len(buckets) - 1, -1 , -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
