class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #First and last position in the array
        left = 0
        right = len(nums) - 1

        while left <= right:
            #Calculate the mid using left and right index
            mid = (left+right) // 2

            #If element stored at mid is equal to target
            if nums[mid] == target:
                return mid
              
            elif nums[left] <= nums[mid]:
                #Arrays left half is sorted.
                if nums[left] <= target < nums[mid]:
                    #The element of array is present in left part.
                    right = mid - 1
                else:
                    #The element of array is present in right part.
                    left = mid + 1
            else:
              #Arrays right half is sorted.
                #The element of array is present in right part.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    #The element of array is present in left part.
                    right = mid - 1
        return -1
