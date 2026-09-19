class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_ = ""
        for i in strs:
            encode_ += str(len(i)) + "#" + i
        return encode_

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            num = 0
            while s[i] != '#':
                num = num * 10 + int(s[i])
                i += 1
            i += 1
            ans.append(s[i:i+num])
            i += num
        return ans