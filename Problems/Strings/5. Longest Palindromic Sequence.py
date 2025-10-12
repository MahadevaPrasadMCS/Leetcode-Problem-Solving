class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        longPal = ""
        for i in range(len(s)):
            #expand from the single centre
            expanded = expand(i,i)
            longPal = expanded if len(expanded) > len(longPal) else longPal
            #expand from the two centres
            expanded = expand(i,i+1)
            longPal = expanded if len(expanded) > len(longPal) else longPal
        return longPal

        
