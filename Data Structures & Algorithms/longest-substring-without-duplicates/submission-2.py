class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        max_len = 0
        l, r = 0, 0

        while r < n:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
    
            seen.add(s[r])
            cur_len = r - l + 1
            max_len = max(max_len, cur_len)
            r += 1
        
        return max_len
