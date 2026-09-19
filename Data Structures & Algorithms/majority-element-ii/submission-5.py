class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        topk = [[0, 0], [0, 0]]

        # Find the two possible candidates
        for n in nums:
            if topk[0][0] == n:
                topk[0][1] += 1
            elif topk[1][0] == n:
                topk[1][1] += 1
            elif topk[0][1] == 0:
                topk[0] = [n, 1]
            elif topk[1][1] == 0:
                topk[1] = [n, 1]
            else:
                topk[0][1] -= 1
                topk[1][1] -= 1

        # Verify candidates
        count1 = count2 = 0

        for n in nums:
            if n == topk[0][0]:
                count1 += 1
            elif n == topk[1][0]:
                count2 += 1

        ans = []

        if count1 > len(nums) // 3:
            ans.append(topk[0][0])

        if count2 > len(nums) // 3:
            ans.append(topk[1][0])

        return ans