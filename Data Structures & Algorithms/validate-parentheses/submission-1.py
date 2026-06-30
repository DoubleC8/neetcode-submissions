class Solution:
    def isValid(self, s: str) -> bool:
        closed_to_open = {
            ')': '(',
            ']': '[', 
            '}': '{'
        }

        stack = []

        for c in s:
            # check if char is closing bracket
            if c in closed_to_open:
                # if char is closing bracket and is the corresponding closing bracket
                # pop the stack 
                if stack and stack[-1] == closed_to_open[c]:
                    stack.pop()
                # if its not the corresponding closing bracker or if the stack is empty
                # return false
                else:
                    return False
            else:
                stack.append(c)
                
        
        return True if not stack else False
