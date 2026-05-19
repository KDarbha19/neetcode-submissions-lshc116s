class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = set()
        for x in nums:
            if x in dup:
                return x
            else:
                dup.add(x)
        return 0
        