class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        max_len = 0
        hashSet = set()
        for right in range(len(s)):
          #inner loop to remove the elements form the set until duplicate is removed.(Shrinking hashtable)
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1
            #Adding unique and substring elements to hashtable (Expanding the array)
            hashSet.add(s[right])
            max_len = max(max_len, len(hashSet))
        return max_len
