class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(n, i) for i, n in enumerate(nums)]
        nums.sort(key=lambda x: x[0])

        left, right = 0, len(nums) - 1
        while left < right:
            curr = nums[left][0] + nums[right][0]
            if curr == target:
                return sorted([nums[left][1], nums[right][1]])
            elif curr < target:
                left += 1
            else:
                right -= 1 
        