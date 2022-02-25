from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carrier = 1
        for i in range(len(digits)-1, -1, -1):
            num = digits[i]
            new_num = (num + carrier)%10
            carrier = (num + carrier)//10
            digits[i] = new_num

        if carrier > 0:
            digits = [carrier] + digits

        return digits