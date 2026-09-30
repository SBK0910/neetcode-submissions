class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x > arr[-1]:
            return arr[len(arr)-k:]
        ans = []
        for i in range(len(arr)):
            if len(ans) < k:
                ans.append(arr[i])
            elif abs(ans[0] - x) > abs(arr[i] - x):
                ans.append(arr[i])
            while len(ans) > k:
                ans.pop(0)
        return ans
             