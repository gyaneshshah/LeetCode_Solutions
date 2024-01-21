class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        haystack_length = len(haystack)
        temp = []
        ans = -1
        for i in range(0, haystack_length-needle_length+1):
            if haystack[i] == needle[0]:
                if haystack[i:i+needle_length] == needle:
                    ans=i
                    break
        return ans
