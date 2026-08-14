class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # first we check if s1 can even fit into s2
        if len(s1) > len(s2):
            return False

        # setting up fixed window len
        k = len(s1)
        n = len(s2)
        l = 0
        s1_freq = [0] * 26
        s2_freq = [0] * 26


        # setting up our initial window
        for c in s1:
            s1_freq[ord(c) - ord("a")] += 1
        
        
        for r in range(n):
            s2_freq[ord(s2[r]) - ord("a")] += 1

            if r >= k:
                s2_freq[ord(s2[l]) - ord("a")] -= 1
                l += 1
            
            if s1_freq == s2_freq:
                return True
        
        return False


