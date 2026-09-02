class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        l = 0
        r = 0
        max_len = 0

        while r < n:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            curr_len = r - l + 1
            max_len = max(max_len, curr_len)
            seen.add(s[r])
            r += 1
        
        return max_len