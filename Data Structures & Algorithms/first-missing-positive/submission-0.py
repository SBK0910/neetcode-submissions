class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ves = set()
        for i in nums:
            if i > 0:
                ves.add(i)
        for i in range(1, 2^31 - 1):
            if i not in ves:
                return i