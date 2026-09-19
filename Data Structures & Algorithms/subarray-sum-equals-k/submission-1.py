class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        prefix_sum = 0
        sol = 0
        for i, n in enumerate(nums):
            prefix_sum += n
            if prefix_sum - k in seen:
                sol += seen[prefix_sum - k]
            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
        return sol