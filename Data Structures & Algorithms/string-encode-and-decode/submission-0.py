class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            s_len = str(len(s))
            res += s_len + '#' + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)
        i = 0

        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            
            s_len = int(s[i:j])
            res.append(s[j+1:+j+1+s_len])
            i = j + s_len + 1

            

        return res