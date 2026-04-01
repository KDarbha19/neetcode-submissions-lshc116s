class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0
        count = 1
        num = set(nums)
        nums = list(num)
        nums.sort()
        print(nums)

        if len(nums) == 1:
            return 1

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                count += 1
            if nums[i + 1] - nums[i] != 1:
                count = 1
            if count > maxCount:
                maxCount = count
        return maxCount
        