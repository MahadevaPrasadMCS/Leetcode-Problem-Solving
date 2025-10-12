class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # pointer for next position of non-val element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                #Skip an index when value is found
                k += 1
        return k
