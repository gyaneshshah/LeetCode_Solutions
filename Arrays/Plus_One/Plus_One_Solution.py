class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = digits[-1]+1
        digits[-1] = val%10 
        carry = int(val/10)
        for i in range(len(digits)-2, -1, -1):
            val = digits[i] + carry
            digits[i] = val%10
            carry = int(val/10)
        if carry>0:
            digits[0]=val%10
            digits.insert(0, carry)
        return digits