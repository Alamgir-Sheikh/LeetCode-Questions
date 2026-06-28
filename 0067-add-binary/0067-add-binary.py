class Solution:
    def add_digits(self, d1, d2="0", carry=0):
        if not carry:
            s = int(d1) + int(d2)
        else:
            s = int(d1) + int(d2) + carry
        if s == 2:
            s = 0
            carry = 1
        elif s == 3:
            s = 1
            carry = 1
        else:
            s = s
            carry = 0
        return s,carry

    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 and j >= 0:
            t, carry = self.add_digits(a[i], b[j], carry)
            res += str(t)
            i -= 1
            j -= 1
        while i >= 0:
            t, carry = self.add_digits(a[i], carry=carry)
            res += str(t)
            i -= 1
        while j >= 0:
            t, carry = self.add_digits(b[j], carry=carry)
            res += str(t)
            j -= 1
        if carry:
            res += str(carry)
        return res [::-1]