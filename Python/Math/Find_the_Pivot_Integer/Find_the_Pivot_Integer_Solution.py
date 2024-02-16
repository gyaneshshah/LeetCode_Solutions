class Solution:
    def pivotInteger(self, n: int) -> int:
        ans = -1
        for i in range(floor(n/2), n+1):
            if sum([j for j in range(0, i+1)]) == sum([k for k in range(i, n+1)]):
                ans = i
                break
        return ans
