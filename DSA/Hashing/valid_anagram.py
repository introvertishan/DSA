from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #return Counter(s) ==  Counter(t)
        return "".join(sorted(s)) == "".join(sorted(t))

aa = "anagram"
bb = "nagaram"
a = Solution()
print(a.isAnagram(aa,bb))
