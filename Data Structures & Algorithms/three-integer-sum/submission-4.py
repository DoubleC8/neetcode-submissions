from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums) 
        res = []
        n = len(sortedNums)

        for i in range(n):
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue

            l = i + 1
            r = n - 1
            while l < r:
                if sortedNums[i] + sortedNums[l] + sortedNums[r] < 0:
                    l += 1
                elif sortedNums[i] + sortedNums[l] + sortedNums[r] > 0:
                    r -= 1
                elif sortedNums[i] + sortedNums[l] + sortedNums[r] == 0:
                    res.append([sortedNums[i], sortedNums[l], sortedNums[r]])
                    l += 1
                    r -= 1
                    while sortedNums[l] == sortedNums[l - 1] and l < r:
                        l += 1
        
        return res