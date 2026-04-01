class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        together = []
        for i in range(len(nums) - 1):
            total = 1
            for j in range(i + 1, len(nums)):
                total *= nums[j]
            prefix.append(total)
        prefix.append(1)

        for i in range(len(nums) - 1, 0, -1):
            total = 1
            for j in range(i - 1, -1, -1):
                total *= nums[j]
            suffix.append(total)
        suffix.append(1)

        suffix.reverse()

        for i in range(len(nums)):
            together.append(prefix[i] * suffix[i])
        return together 


