# https://leetcode.com/problems/contains-duplicate/
'''
:type: List[int]
:rtype: bool
'''
# Solution 1: one-liner using set
class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)

'''
time complexity: O(n)
space complexity: O(1)
'''

# Solution 2: 2-pointers
class Solution:
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == nums[i]:
                    return True
        return False

'''
time complexity: O(n2)
space complexity: O(1)
'''

if __name__ == "__main__":
    nums = [2, 1, 3, 3]
    print(Solution().containsDuplicate(nums))
