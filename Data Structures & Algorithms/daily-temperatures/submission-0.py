class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        
        # this will keep track of the indices 
        stack = []

        #since we are looking for the next greater element ->
        #use monotonic decreasing stack:
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index

            stack.append(i)
        
        return res



