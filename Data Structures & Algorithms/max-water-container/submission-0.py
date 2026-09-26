class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0,len(heights) - 1
        ans = 0
        while left < right:
            a = min(heights[left], heights[right]) * (right - left)
            ans = max(ans, a)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return ans