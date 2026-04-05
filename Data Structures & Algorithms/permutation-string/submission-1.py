class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1 = list(s1)
        ls1.sort()

        l = 0
        r = l + len(s1)
        while r < len(s2) + 1:
            s = s2[l:r]
            ss = list(s)
            ss.sort()
            if ss == ls1:
                return True
            else:
                l += 1
                r += 1
        return False
