class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_pos, b_pos = len(a)-1, len(b)-1
        res = []
        carry = 0
        while a_pos >= 0 and b_pos >= 0:
            current= int(a[a_pos]) + int(b[b_pos]) + carry
            res.append(str(current%2))
            carry = current // 2
            a_pos -= 1
            b_pos -= 1

        while a_pos >= 0:
            current = int(a[a_pos]) + carry
            res.append(str(current%2))
            carry = current//2
            a_pos -= 1


        while b_pos >= 0:
            current = int(b[b_pos]) + carry
            res.append(str(current%2))
            carry = current//2
            b_pos -= 1

        if carry:
            res.append(str(carry))

        return ''.join([ res[i] for i in range(len(res)-1, -1, -1)])