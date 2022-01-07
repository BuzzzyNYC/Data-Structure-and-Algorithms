# https://leetcode.com/problems/valid-mountain-array/
'''
:type: List[arr]
:rtype: Bool

If we walk along the mountain from left to right, 
we have to move strictly up, then strictly down.
Algorithm: walk up from left to right until we can't: that has to be the peak. 
We should ensure the peak is not the first or last element. 
Then, we walk down. If we reach the end, the array is valid, otherwise its not.
'''

class Solution:
    def validMountainArray(self, arr):
        i = 0
        # go up
        while i < len(arr) and arr[i + 1] > arr[i]:
            i += 1
        # corner cases where the arr either goes up or down
        if i == len(arr) - 1 or i == 0:
            return False

        # go down
        while i < len(arr) and arr[i + 1] < arr[i]:
            i + 1
        if i == len(arr) - 1:
            return True
        else:
            return False

'''
time complexity: O(n) - n is length of arr
space complexity: O(1)
'''