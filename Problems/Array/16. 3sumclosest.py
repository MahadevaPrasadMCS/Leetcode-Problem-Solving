class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #Sort the array to use two pointers
        nums.sort()
        diff = 0
        best_diff = float("inf")
        closest_sum = 0
        n = len(nums)
      
        if n > 2:

            #Outerloop to set one number fixed
            for i in range(n-2):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                #Two pointers to move from both sides
                left = i+1
                right = n-1

                #Innerloop to find two numbers
                while left < right:
                    sums = nums[i] + nums[left] + nums[right]
                    diff = abs(target-sums)

                    #update closest_sum when you get best difference
                    if best_diff > diff:
                        closest_sum = sums
                        best_diff = diff
                    
                    if sums < target:
                        left += 1
                    elif sums > target:
                        right -= 1
                    else:
                        return sums
                      
        return closest_sum 

