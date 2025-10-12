class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diffs = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff not in diffs:
                diffs[num] = i
            else:
                return ([i,diffs[diff]])
