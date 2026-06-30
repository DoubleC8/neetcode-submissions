class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {
            ')': '(', 
            '}': '{', 
            ']': '['
        }
        stack = []

        for c in s:
            # if c is a closing bracker
            if c in closedToOpen:
                # we check that the stack is not empty and if the 
                # it has a corresponding opening bracket
                if stack and stack[-1] == closedToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False