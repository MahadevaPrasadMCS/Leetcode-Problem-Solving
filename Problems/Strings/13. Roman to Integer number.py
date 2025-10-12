class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {'I':1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}

        sum = 0

        for i in range(len(s)-1):
            curr_val = s[i]
            next_val = s[i+1]
            if map[curr_val] < map[next_val]:
                sum -= map[curr_val]
                
            else:
                sum += map[curr_val]
        sum += map[s[-1]]
        return sum
