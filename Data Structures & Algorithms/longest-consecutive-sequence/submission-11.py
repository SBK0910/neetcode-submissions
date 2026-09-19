class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ml = 0
        for n in nums:
            if n - 1 not in seen:
                cl = 1
                curr = n
                while curr + 1 in seen:
                    cl += 1
                    curr += 1
                ml = max(cl, ml)
        return ml