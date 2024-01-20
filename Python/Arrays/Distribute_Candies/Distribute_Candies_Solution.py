class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_candyType = list(set(candyType))
        nunique = len(unique_candyType)
        n = len(candyType)
        ans = n/2
        if nunique <= ans:
            ans = nunique
        return int(ans)
