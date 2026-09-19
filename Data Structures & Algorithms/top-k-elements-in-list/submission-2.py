class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cdict = {}
        for n in nums:
            cdict[n] = cdict.get(n, 0) + 1
        
        fbuck = [[] for _ in range(len(nums)+1)]
        for n,f in cdict.items():
            fbuck[f].append(n)
        
        sol = []
        for i in range(len(nums), -1, -1):
            for buck in fbuck[i]:
                sol.append(buck)
            if len(sol) == k:
                break
        return sol
