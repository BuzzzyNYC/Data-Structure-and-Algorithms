# https://leetcode.com/problems/maximum-subarray/
'''
:type: List[int]
:rtype: int
'''

class Solution:
    def maxSubarray(self, nums):
        local_sum = 0
        max_sum = nums[0]
        for num in nums:
            if local_sum < 0:
                local_sum = num
            else:
                local_sum += num
            max_sum = max(local_sum, max_sum)
        return max_sum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubarray(nums))
