class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                prefix_prod[i] = nums[i]
            else:
                prefix_prod[i] = prefix_prod[i-1] * nums[i]
        sol = [1] * len(nums)
        curr = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                sol[i] = prefix_prod[i-1]
            elif i == 0:
                sol[i] = curr
            else:
                sol[i] = curr * prefix_prod[i-1]
            curr *= nums[i]
        return sol