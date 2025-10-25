class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #Length that should be matched
        for i in range(len(haystack) - len(needle) + 1):
            #Slice the given string with matching string
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
            
