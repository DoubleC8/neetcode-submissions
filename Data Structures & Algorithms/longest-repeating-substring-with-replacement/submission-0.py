from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        n = len(s)
        max_len = 0
        l = 0
        r = 0

        while r < n:
            freq[s[r]] += 1
            max_count = max(freq.values())

            while (r - l + 1) - max_count > k:
                freq[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, (r - l + 1))
            r += 1
        
        return max_len
            


