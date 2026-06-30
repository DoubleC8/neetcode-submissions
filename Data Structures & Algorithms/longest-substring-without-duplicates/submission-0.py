class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        n = len(s)
        l, r = 0, 0

        while r < n:
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                max_len = max(max_len, r - l + 1)
                seen.add(s[r])
                r += 1
        
        return max_len