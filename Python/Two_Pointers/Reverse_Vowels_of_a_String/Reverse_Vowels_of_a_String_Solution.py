class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        only_vow = [char for char in s if char in vowels]
        only_vow = only_vow[::-1]
        reversed_s = ""
        ind = 0
        for char in s:
            if char in vowels:
                reversed_s += only_vow[ind]
                ind+=1
            else:
                reversed_s += char
        return reversed_s
