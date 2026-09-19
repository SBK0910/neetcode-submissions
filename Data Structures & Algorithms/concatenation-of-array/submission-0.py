class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        sol = [1] * len(nums) * 2
        for i in range(len(nums)):
            sol[i] = nums[i]
            sol[i + len(nums)] = nums[i]
        return sol