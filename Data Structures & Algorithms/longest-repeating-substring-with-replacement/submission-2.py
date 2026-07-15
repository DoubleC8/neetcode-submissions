from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        n = len(s)
        count = defaultdict(int)
        l = 0
        r = 0

        while r < n:
            count[s[r]] += 1

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            cur_len = r - l + 1
            max_len = max(max_len, cur_len)
            r += 1
        
        return max_len

