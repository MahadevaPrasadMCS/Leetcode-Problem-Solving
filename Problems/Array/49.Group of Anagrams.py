from collections import defaultdict as dd

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #dictionary that can store value as a list
        ans = dd(list)
      
        for char in strs:
            #find the anagram
            key = "".join(sorted(char))
            #append stirng its group
            ans[key].append(char)
        return list(ans.values())
