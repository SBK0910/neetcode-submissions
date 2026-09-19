class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        e,c = nums[0], 1
        for i in range(1,len(nums)):
            if c == 0:
                e = nums[i]
                c = 1
            elif e == nums[i]:
                c += 1
            else:
                c -= 1
        return e