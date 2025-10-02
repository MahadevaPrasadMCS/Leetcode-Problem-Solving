class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        quadruplets = []

        if len(nums) > 3:
            n = len(nums)

            #Outer loop to set first variable.
            for i in range(n-3):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                #Inner loop to set second variable.
                for j in range(i+1,n-2):
                    if j > i+1 and nums[j] == nums[j-1]:
                        continue
                    #Initializing two pointers
                    left = j + 1
                    right = n - 1
                  
                    while left < right:
                        total = nums[i] + nums[j] + nums[left] + nums[right]

                        #Checking equality of total and target
                        if total == target:
                            quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                            left += 1
                            while left < right and nums[left] == nums[left-1]:
                                left += 1
                            right -= 1
                            while left < right and nums[right] == nums[right+1]:
                                right -= 1
                        elif total > target:
                            right -= 1
                        else:
                            left += 1
        return quadruplets


        
        
