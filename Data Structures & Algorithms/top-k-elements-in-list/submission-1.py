class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cdict = {}
        for n in nums:
            cdict[n] = cdict.get(n, 0) + 1
        pairs = list(cdict.items())
        pairs.sort(key=lambda x: x[1],reverse=True)
        return [pairs[i][0] for i in range(k) ]
