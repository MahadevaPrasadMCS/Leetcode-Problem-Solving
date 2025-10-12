class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        #odd length array
        if n % 2 != 0:
            median = nums1[n // 2]
        #even length array
        else:
            mid = n // 2
            median = (nums1[mid] + nums1[mid-1]) / 2.0
        return median
