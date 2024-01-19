class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        for t in range(0, len(timeSeries)-1):
            diff = timeSeries[t+1] - timeSeries[t]
            if diff > duration:
                ans+=duration
            else:
                ans+=diff
        ans+=duration
        return ans
