class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ss = list(s)
        tt = list(t)
        ss.sort()
        tt.sort()
        return ss == tt
        