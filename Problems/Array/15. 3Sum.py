class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #Sorting the array , so that we can use two pointers approach.
        nums.sort()

        #Empty list to store triplets.
        triplets = []
      
        if nums > 2:
            n = len(nums)
          
            #Outerloop to fix one element of the triplets.
            for i in range(n-2):
              
                #Condition to check whether the current number is same as previous.
                if i > 0 and nums[i] == nums[i-1]:
                    continue

                #Two pointers to check different combinations of triplet
                left = i+1
                right = n-1

                #Inner loop to find and store different triplets
                while left < right:
                    total = nums[i] + nums[left] + nums[right]

                    if total == 0:
                        triplets.append([nums[i],nums[left],nums[right]])
                        left += 1
                        right -= 1

                        #Loops to skip duplicates
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

                    #If total is greater than 0 , we need a small number to get 0.
                    elif total > 0:
                        right -= 1

                    #If total is less than 0 , we need a big number to get 0.
                    else:
                        left += 1
                      
        return triplets
