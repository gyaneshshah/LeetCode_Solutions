class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        if string[0]!='-':
            ans = int(string[::-1])
            if ans>2147483647:
                ans=0
        else:
            string = string[1:]
            ans = int(string[::-1])*-1
            if ans<-2147483648:
                ans=0
        return ans
