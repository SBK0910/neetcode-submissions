class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set([s[0]])
        i, ans = 0,1
        for j in range(1,len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            ans = max(ans,j-i+1)
        return ans
            