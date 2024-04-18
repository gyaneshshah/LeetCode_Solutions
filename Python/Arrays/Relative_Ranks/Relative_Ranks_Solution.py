class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        ans=[]
        for s in score:
            if s==sorted_score[0]:
                ans.append("Gold Medal")
            elif s==sorted_score[1]:
                ans.append("Silver Medal")
            elif s==sorted_score[2]:
                ans.append("Bronze Medal")
            else:
                ans.append(str(sorted_score.index(s)+1))
        return ans
