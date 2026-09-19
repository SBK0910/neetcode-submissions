class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        s1, s2 = strs[0], strs[-1]
        ci = 0
        while ci < min(len(s1),len(s2)):
            if s1[ci] != s2[ci]:
                break
            ci += 1
        if ci - 1 >= 0:
            return s1[:ci]
        return ""