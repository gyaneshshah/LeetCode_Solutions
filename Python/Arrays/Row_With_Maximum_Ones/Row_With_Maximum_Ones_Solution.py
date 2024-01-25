class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        count = []
        cnt=0
        for arr in mat:
            cnt=0
            for no in arr:
                cnt+=no
            count.append(cnt)
        maxcnt = max(count)
        return [count.index(maxcnt), maxcnt]
