class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters_reversed = [i for i in s if i.isalpha()]
        pos = len(letters_reversed)-1
        for ind, char in enumerate(s):
            if char.isalpha():
                s = s[:ind] + letters_reversed[pos] + s[ind+1:]
                pos-=1
        return s
