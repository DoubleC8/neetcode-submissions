from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_len = 0
        n = len(s)
        l, r = 0, 0

        while r < n:
            freq[s[r]] += 1
            max_freq = max(freq.values())

            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            
            cur_len = r - l + 1
            max_len = max(max_len, cur_len)
            r += 1
        
        return max_len
