class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        freq = {}
        n = len(nums)
        maximum = n // 2
        #Find frequencies of numbers
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        #Find the key of number with high frequency
        for num in freq:
            if maximum < max(maximum, freq[num]):
                key = num
        return key
