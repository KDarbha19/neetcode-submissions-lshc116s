class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxHeight = 0
        while l < r:
            height = (r - l) * min(heights[r], heights[l])
            maxHeight = max(maxHeight, height)
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
        return maxHeight

            
        