class Solution:
    @staticmethod
    def fhash(word: str) -> tuple:
        fcount = [0] * 26
        for w in word:
            i = ord(w) - ord('a')
            fcount[i] += 1
        return tuple(fcount)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        agroup = {}
        for s in strs:
            h = Solution.fhash(s)
            if h in agroup:
                agroup[h].append(s)
            else:
                agroup[h] = [s]
        return list(agroup.values())