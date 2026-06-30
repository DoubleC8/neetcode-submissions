class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        n = len(sortedNums)
        res = []

        for i in range(n):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue 
    
            l = i + 1
            r = n - 1

            while l < r:
                if sortedNums[i] + sortedNums[l] + sortedNums[r] < 0:
                    l += 1
                elif sortedNums[i] + sortedNums[l] + sortedNums[r] > 0:
                    r -= 1
                else:
                    res.append([sortedNums[i], sortedNums[l], sortedNums[r]])
                    l += 1
                    r -= 1 
                    while l < r and sortedNums[l] == sortedNums[l - 1]:
                        l += 1
        
        return res