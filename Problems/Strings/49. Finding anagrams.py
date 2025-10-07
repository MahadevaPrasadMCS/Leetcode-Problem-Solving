#import the defaultdict to create dictionaries of different types
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #Dictionary that stores values as a list
        ans = defaultdict(list)
        for s in strs:
            #Find the key by sorting the string and joining it to empty string.
            key = "".join(sorted(s))
            #For different anagram lists are appended with strings
            ans[key].append(s)
        #Return a list of all values stored in the dictionary.
        return list(ans.values())
