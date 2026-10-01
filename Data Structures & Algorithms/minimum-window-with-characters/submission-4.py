class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tf = {}
        for ch in t:
            tf[ch] = tf.get(ch, 0) + 1

        sf = {}
        required = len(t)
        left = 0
        ans = ""

        for right, ch in enumerate(s):
            sf[ch] = sf.get(ch, 0) + 1

            # This character contributed to satisfying t
            if ch in tf and sf[ch] <= tf[ch]:
                required -= 1

            while required == 0:
                # Current window is valid
                if not ans or len(ans) > right - left + 1:
                    ans = s[left:right + 1]

                left_ch = s[left]
                sf[left_ch] -= 1

                # Removing this character made the window invalid
                if left_ch in tf and sf[left_ch] < tf[left_ch]:
                    required += 1

                left += 1

        return ans