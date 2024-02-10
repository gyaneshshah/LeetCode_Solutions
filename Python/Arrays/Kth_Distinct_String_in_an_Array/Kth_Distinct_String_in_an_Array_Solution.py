class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans = ""
        cnt = 0
        for string in arr:
            if arr.count(string) == 1:
                cnt+=1
            if cnt == k:
                ans = string 
                break
        return ans
