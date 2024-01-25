class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = [sum(arr) for arr in accounts]
        return max(wealth)
