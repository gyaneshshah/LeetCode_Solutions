class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome_length = 0
        longest_palindrome = ""
        for i in range(len(s)):
            for j in range(len(s)-1, i-1, -1):
                if j-i+1 > palindrome_length:
                    if s[i:j+1] == s[i:j+1][::-1]:
                        palindrome_length = j-i+1
                        longest_palindrome = s[i:j+1]
                        break
        return longest_palindrome
