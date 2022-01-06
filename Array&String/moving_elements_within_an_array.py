# An array contains both positive and negative numbers in random order. 
# Rearrange the array elements so that all negative numbers appear before all positive numbers.
'''
:type: List[int]
:rtype: List[int]
'''
# Solution1: quicksort
class Solution1:
    def rearrange(self, arr, n):
        # Use quicksort. Initialize j = 0
        j = 0
        for i in range(0, n):
            if (arr[i] < 0):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                j += 1
        return arr

if __name__ == "__main__":
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    n = len(arr)
    print(Solution1().rearrange(arr, n))
    
"""
Time complexity: O(n)
Space complexity: O(1)
"""

# Solution2: two-pointer
'''
Two Pointer Approach: The idea is to solve this problem with constant space and linear time
by using a two-pointer or two-variable approach where we simply take two variables like left 
and right which hold the 0 and n-1 indexes. Just need to check that :
1. Check if the left and right pointer elements are negative then simply increment the left pointer.
2. Otherwise, if the left element is positive and the right element is negative then simply swap the elements, 
and simultaneously increment and decrement the left and right pointers.
3. Else if the left element is positive and the right element is also positive then simply decrement the right pointer.
4. Repeat the above 3 steps until the left pointer ≤ right pointer.
'''
class Solution2:
    def rearrange(self, arr, n):
        i = 0
        j = n - 1
        while i <= j:
            if arr[i] < 0 and arr[j] < 0:
                i += 1
            elif arr[i] > 0 and arr[j] < 0:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            elif arr[i] > 0 and arr[j] > 0:
                j -= 1
            else:
                i += 1
                j -= 1
    
    def display(arr):
        for i in range(len(arr)):
            print(arr[i], end=" ")

if __name__ == "__main__":
    arr=[-12, 11, -13, -5, 6, -7, 5, -3, 11]
    n = len(arr)
    print(Solution2().rearrange(arr, n))

'''
time complexity: O(n)
space complexity: O(1)
'''