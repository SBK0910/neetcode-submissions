class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for s in strs:
            e += str(len(s))
            e += "#"
            e += s
        return e
    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        sol = []
        while i < len(s):
            l = ""
            while s[i] != "#":
                l += s[i]
                i += 1
            l = int(l)
            sol.append(s[i+1:i + l + 1])
            i += l + 1
        return sol