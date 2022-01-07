# https://leetcode.com/problems/max-consecutive-ones/

'''
:type: List[int]
:rtype: int
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        current_length = 0
        max_length = 0
        for i in nums:
            if i == 1:
                current_length += 1
                if current_length > max_length:
                    current_length = max_length
            else:
                current_length = 0
        return max_length

if __name__ == "__main__":
    nums = [1,1,0,1,1,1]
    print(Solution().findMaxConsecutiveOnes(nums))

'''
time complexity: O(n)
space complextity: O(1)
'''