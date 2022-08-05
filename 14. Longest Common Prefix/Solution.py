from typing import Optional

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ''
        else:
            lcp = strs[0]
            for s in strs:
                for i, c in enumerate(lcp):
                    if i < len(s) and c == s[i]:
                        continue
                    else:
                        lcp = lcp[0:i]
            
            return lcp