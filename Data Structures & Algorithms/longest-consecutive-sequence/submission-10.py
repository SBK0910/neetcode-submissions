class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        sol = 0
        cl = 1
        for i in range(1, len(nums)):

            if nums[i-1] + 1 == nums[i]:
                cl += 1
            elif nums[i-1] == nums[i]:
                continue
            else:
                sol = max(sol, cl)
                cl = 1
        return max(sol, cl)