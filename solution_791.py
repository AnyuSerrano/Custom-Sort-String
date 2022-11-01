

from collections import Counter

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        ret = ''
        ref = dict(Counter(list(T)))
        
        for s in S:
            if not s in ref: continue
            ret += s * ref[s]
            ref.pop(s)
        
        for k in ref:
            ret += k * ref[k]
        
        return ret