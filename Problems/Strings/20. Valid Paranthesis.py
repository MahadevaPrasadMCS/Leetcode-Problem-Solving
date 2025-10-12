class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        valid = {')' : '(' , ']' : '[' , '}' : '{'}
        stack = []

        for char in s:
            if char not in valid:
                stack.append(char)
            else:
                top_elem = stack.pop() if stack else '#'
                if valid[char] != top_elem:
                    return False
        return not stack
