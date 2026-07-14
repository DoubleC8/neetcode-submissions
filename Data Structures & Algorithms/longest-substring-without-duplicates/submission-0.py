class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        n = len(s)
        seen = set()
        l = 0
        r = 0

        while r < n:
            # while in illegal state, we update our set
            # until we are legal
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # once we are in legal state, we can update our
            # cur_element
            curr_len = r - l + 1
            max_len = max(max_len, curr_len)
            seen.add(s[r])
            r += 1
        
        return max_len 
