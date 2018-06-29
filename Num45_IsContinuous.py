# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        numbers.sort()
        while 0 in numbers:
            numbers.remove(0)

        if len(numbers) == 1:
            return True

        for j in range(len(numbers)-1):
            if numbers[j] == numbers[j+1]:
                return False

        if numbers[-1] - numbers[0] < 5:
            return True
        else:
            return False
