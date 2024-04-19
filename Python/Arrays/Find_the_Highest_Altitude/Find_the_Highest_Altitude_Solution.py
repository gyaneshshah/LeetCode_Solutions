class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        curr_alt=0
        for height in gain:
            curr_alt+=height
            if curr_alt>max_alt:
                max_alt=curr_alt
        return max_alt
