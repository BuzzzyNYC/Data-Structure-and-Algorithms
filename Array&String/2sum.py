# https://leetcode.com/problems/two-sum/

'''
:type: List[int], int
:rtype: List[int]
'''
# Solution 1: using hashmap
class Solution1:
    def twoSum(self, nums, target):
        hash_map = {}
        # key-value pair: key is a number in nums, value is index of that number
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif not in hash_map:
                hash_map[nums[i]] = i
            else:
                return [i, hash_map[dif]]


'''
time complexity: O(n)
space complexity: O(1)
'''
# Solution 2: Two-pointer
class Solution2:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            dif = target - nums[i]
            for j in range(len(nums)):
                if i != j and nums[j] == dif:
                    return [i, j] 

'''
time complexity: O(n2)
space complexity: O(n2)
'''

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(Solution1().twoSum(nums, target))
    print(Solution2().twoSum(nums, target))
