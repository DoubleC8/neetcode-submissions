from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        n = len(s)
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in range(n):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1
        
        return s_dict == t_dict
        

        