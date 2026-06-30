from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            key = sorted(s)

            res[tuple(key)].append(s)
        
        return list(res.values())


