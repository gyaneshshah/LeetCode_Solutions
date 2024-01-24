class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        ans = [area, 1 ]
        diff = area-1
        for i in range(2, int(area/2)+1):
            if area%i==0 and i>=area/i:
                l=i
                w=int(area/i)
                if l==w:
                    ans=[l, w]
                    break
                else:
                    if l-w < diff:
                        diff = l-w
                        ans=[l, w]
        return ans   
