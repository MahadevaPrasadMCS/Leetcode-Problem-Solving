class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for digi in range(len(digits)-1,-1,-1):
            if digits[digi] != 9:
                digits[digi] += 1
                return digits
            else:
                digits[digi] = 0
        return [1]+digits
