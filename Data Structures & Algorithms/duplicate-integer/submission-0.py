class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d:
                value = d[i] + 1
                d[i] = value
            else:
                d[i] = 1

        for v in d.values():
            if v > 1:
                return True
        return False 