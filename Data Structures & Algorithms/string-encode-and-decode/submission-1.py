class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            len_s = str(len(s))

            res += len_s + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        n = len(s)
        res = []
        i = 0

        while i < n:
            j = i 
            while s[j] != '#':
                j += 1

            len_s = int(s[i:j])

            res.append(s[j + 1 : j + 1 + len_s])

            i = j + 1 + len_s
        
        return res
    