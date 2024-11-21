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

# Best Solution : https://leetcode.com/problems/group-anagrams/solutions/4683832/beats-99-users-c-java-python-javascript-2-approaches-explained/