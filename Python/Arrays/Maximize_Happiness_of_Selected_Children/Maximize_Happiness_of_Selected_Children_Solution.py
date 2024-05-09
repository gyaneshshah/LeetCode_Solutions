class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        summ = 0
        for i in range(0, k):
            if happiness[i] - i < 0:
                return summ
            summ += happiness[i] - i
        return summ
