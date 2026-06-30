class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        max_len = 0
        l, r = 0, 0

        while r < n:
            # while we are in an illegal state, we upate 
            # until we are not 
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            cur_len = r - l + 1
            seen.add(s[r])
            r += 1
            max_len = max(max_len, cur_len)
        
        return max_len

