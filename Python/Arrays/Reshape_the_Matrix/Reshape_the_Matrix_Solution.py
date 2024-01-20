class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        l = [ele for lis in mat for ele in lis]
        ans = mat
        if len(l) == r*c:
            ind = 0
            ans = []
            for i in range(0,r):
                temp = []
                for j in range(0, c):
                    temp.append(l[ind])
                    ind+=1
                ans.append(temp)
        return ans
