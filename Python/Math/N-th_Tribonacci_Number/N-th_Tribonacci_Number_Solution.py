class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0, 1, 1]
        if n<3:
            return tri[n]
        summ = 0
        for i in range(n-2):
            summ = tri[0] + tri[1] + tri[2]
            tri.append(summ)
            tri.pop(0)
        return summ
