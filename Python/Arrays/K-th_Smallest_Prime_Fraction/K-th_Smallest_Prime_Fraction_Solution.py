class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        prime_dict = {}
        for i in range(len(arr)-1):
            for j in range(i, len(arr)):
                prime_dict[arr[i]/arr[j]] = [arr[i], arr[j]]
        numbers = sorted(list(prime_dict.keys()))
        return prime_dict[numbers[k-1]]
