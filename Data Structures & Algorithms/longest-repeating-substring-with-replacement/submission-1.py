from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0
        l = 0
        r = 0
        freq = defaultdict(int)

        while r < n:
            freq[s[r]] += 1
            max_freq = max(freq.values())

            # illegal state when
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1
        
        return max_len
