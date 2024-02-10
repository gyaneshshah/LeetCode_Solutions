class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        duration = releaseTimes[0]
        ind = 0
        diff = 0
        for i in range(1, len(releaseTimes)):
            diff = releaseTimes[i]-releaseTimes[i-1]
            if diff>duration:
                ind = i
                duration = diff
            elif diff == duration:
                if ord(keysPressed[i]) >= ord(keysPressed[ind]):
                    ind = i
                    duration = diff 
        return keysPressed[ind]
