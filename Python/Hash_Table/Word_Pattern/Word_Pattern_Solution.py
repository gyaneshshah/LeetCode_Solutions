class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split(' ')
        if len(list_s) != len(pattern):
            return False
        dict1 = {}
        dict2 = {}
        val1 = 1
        val2 = 1

        for i in range(len(list_s)):
            if list_s[i] not in dict1.keys():
                dict1[list_s[i]] = val1
                val1 += 1
            if pattern[i] not in dict2.keys():
                dict2[pattern[i]] = val2
                val2 += 1
            if dict2[pattern[i]] != dict1[list_s[i]]:
                return False
        return True 
