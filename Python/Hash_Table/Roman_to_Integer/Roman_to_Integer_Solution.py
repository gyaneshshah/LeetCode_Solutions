class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,'M': 1000}
        summ = 0
        s_len = len(s)
        for i, numeral in enumerate(s):
            summ += symbols[numeral]
            if i!=s_len-1:
                if numeral == 'I' and (s[i+1]=='V' or s[i+1]=='X'):
                    summ -= 2
                elif numeral == 'X' and (s[i+1]=='L' or s[i+1]=='C'):
                    summ -= 20
                elif numeral == 'C' and (s[i+1]=='D' or s[i+1]=='M'):
                    summ -= 200
        return summ
