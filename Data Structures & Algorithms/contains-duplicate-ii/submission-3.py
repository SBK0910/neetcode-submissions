class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        seen = {nums[0]: 1}
        for j in range(1, len(nums)):
            while abs(i - j) > k:
                seen[nums[i]] -= 1
                if seen[nums[i]] == 0:
                    del seen[nums[i]]
                i += 1
            if nums[j] in seen and seen[nums[j]] > 0:
                return True
            seen[nums[j]] = seen.get(nums[j], 0) + 1
            
        return False