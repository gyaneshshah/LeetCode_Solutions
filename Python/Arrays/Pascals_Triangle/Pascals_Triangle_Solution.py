class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            temp=[]
            prev = ans[i-1]
            inc = 0
            for j in range(0, i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(prev[inc] + prev[inc+1])
                    inc+=1
            ans.append(temp)
        return ans
