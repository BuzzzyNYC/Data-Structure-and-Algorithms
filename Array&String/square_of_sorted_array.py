# https://leetcode.com/problems/squares-of-a-sorted-array/

'''
:type: List[int]
:rtype: List[int]
'''
# Solution 1: use sort()

class Solution1:
    def sortedSquare(self, nums):
        for i in range(len(nums)):
            nums[i] *= i
        nums.sort()
        return nums

'''
time complexity: O(n) + O(nlogn) = O(nlogn)
space complexity: O(1)
'''

# Solution 2: Two-pointer

class Solution2:
    def sortedSquare(self, nums):
        tmp =[]
        for i in range(len(nums)):
            if nums[i] >= 0:
                break
        j = i
        i = j - 1
        while j < len(nums) and i >= 0:
            if nums[i] ** 2 > nums[j] ** 2:
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i -= 1
        while j < len(nums):
            tmp.append(nums[j]**2)
            j += 1
        while i >= 0:
            tmp.append(nums[i]**2)
            i -= 1
        return tmp

if __name__ ==  "__main__":
    nums = [-4,-1,0,3,10]
    print(Solution1().sortedSquare(nums))
    print(Solution2().sortedSquare(nums))


