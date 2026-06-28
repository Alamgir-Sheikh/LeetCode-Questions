class Solution:
    def check_carry(self, digits, i, d):
        carry = 0
        if d == 10:
            d = 0
            digits[i] = d
            carry = 1
        else:
            digits[i] = d
        return carry
        
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 0
        while i >= 0:
            d = digits[i]
            print(d)
            if not carry and i == len(digits) - 1:
                d += 1
            else:
                d = d + carry
            carry = self.check_carry(digits,i,d)
            i -= 1
        if carry:
            digits.insert(0, carry)
        return digits