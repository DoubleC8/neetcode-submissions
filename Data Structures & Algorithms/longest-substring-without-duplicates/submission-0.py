class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        max_len = 0
        l = 0
        r = 0

        while r < n:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            curr_len = r - l + 1            
            r += 1
            max_len = max(max_len, curr_len)
        
        return max_len
