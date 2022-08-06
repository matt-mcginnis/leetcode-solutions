from typing import Optional

class Solution:
    def isValid(self, s: str) -> bool:
        d = {")":"(", "}":"{", "]":"["}
        
        stack = []
        for ch in s:
            if ch in d.values():
                stack.append(ch)
            elif ch in d.keys():
                if len(stack) == 0 or stack.pop() != d[ch]:
                    return False
            
        return stack == []