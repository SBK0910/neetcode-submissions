class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target > sum(nums):
            return 0
        ans = len(nums)
        left,cs = 0, 0
        for right in range(0,len(nums)):
            cs += nums[right]
            while cs >= target:
                ans = min(ans, right - left + 1)
                cs -= nums[left]
                left += 1
        return ans