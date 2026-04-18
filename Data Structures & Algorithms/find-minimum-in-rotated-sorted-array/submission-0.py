class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        k = 100000
        while l <= r:
            if nums[l] < nums[r]:
                return min(k, nums[l])

            mid = (l + r) // 2
            k = min(k,nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return k
        