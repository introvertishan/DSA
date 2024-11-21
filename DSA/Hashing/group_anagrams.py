strs = ["eat","tea","tan","ate","nat","bat"]
#strs = ["a"]

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        tmp = {}
        tmp_arr = []
        for i in strs:
            if tmp.get("".join(sorted(i))):
                tmp.setdefault("".join(sorted(i)), []).extend([i])
            else:
                tmp.setdefault("".join(sorted(i)),[]).append(i)

        for j in tmp.values():
            tmp_arr.append(j)

        return tmp_arr


a = Solution()
print(a.groupAnagrams(strs))