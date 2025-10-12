class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #Store dictionary in descending order
        val_map = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }

        ans = []
        for val in sorted(val_map.keys(), reverse=True):  # Python preserves insertion order only in version 3.7+
          #check highest val that can divide number 
          count = num // val
           if count:
             #multiply value of key val with count
            ans.append(val_map[val]*count)
             #reduce the number
            num -= val*count
        return ''.join(ans) 
