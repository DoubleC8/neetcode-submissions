class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initial thoughts:
        # make two pointer, at the start and end
        # we loop while (l < r)
        # add them together if the result is > than target
        # we move the r pointer down
        # if the result is < target 
        # we move teh l pointer up
        # if it equals the target we simply return [l, r]

        l = 0
        r = len(numbers) - 1

        while(l < r):
            res = numbers[l] + numbers[r]
            if res < target:
                l += 1
            elif res > target:
                r -= 1
            else: 
                return [l + 1, r + 1] 

