class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        1) Iterate through the elements of the string
        2) Use a variable to keep track of current max length
        3) Use a list to keep track of current letters
        4) If a letter is repeated, then slice list and continue searching
        '''
        max_len = 1
        tracked_chars = s[0]
