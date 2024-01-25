class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        count = []
        cnt=0
        for arr in mat:
            cnt=sum(arr)
            count.append(cnt)
        maxcnt = max(count)
        return [count.index(maxcnt), maxcnt]
