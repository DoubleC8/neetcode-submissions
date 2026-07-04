from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        n = len(nums)
        # creating a list of lists 
        # the num of times a num appears correlates
        # to where its placed in the buckets array
        buckets = [[] for _ in range(n + 1)]

        # get initial count for each num
        for num in nums:
            count[num] += 1
        
        for key, value in count.items():
            buckets[value].append(key)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res

