class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(0, len(nums)):
            max_ = min(i+k+1, len(nums))
            for j in range(i+1,max_):
                if nums[i] == nums[j]:
                    return True
        return False