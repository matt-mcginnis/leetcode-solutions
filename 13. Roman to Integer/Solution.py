from typing import Optional

class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ret = 0
        prev_char = ''
        for c in s[::-1]:
            if prev_char != '' and rom_dict[c] < rom_dict[prev_char]:
                ret -= rom_dict[c]
            else:
                ret += rom_dict[c]

            prev_char = c
        
        return ret