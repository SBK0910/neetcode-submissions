class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = -1
        for i , n in enumerate(nums):
            if n == val:
                continue
            j += 1
            nums[i],nums[j] = nums[j],nums[i]
        return j + 1