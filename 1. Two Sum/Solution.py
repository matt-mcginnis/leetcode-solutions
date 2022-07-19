class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        1) Create a dictionary to store the number and its index
        2) Iterate through the enumeration of nums
        3) If the difference between target and the current num is 
           in our dictionary, then we have the two nums that sum to 
           target.
           Otherwise, we store num and its index in our dictionary.
        4) Return the index (value) of the num (key) found in our 
           dictionary along with the current index.
        '''
        diff_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in diff_dict:
                return [diff_dict[diff], i]
            else:
                diff_dict[num] = i

        return []
