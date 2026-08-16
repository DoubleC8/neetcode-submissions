from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0
        freq = defaultdict(int)
        l = 0
        r = 0
        
        while r < n:
            freq[s[r]] += 1
            max_freq = max(freq.values())

            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            
            curr_len = r - l + 1
            max_len = max(max_len, curr_len)
            r += 1
        
        return max_len