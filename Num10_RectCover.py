# -*- coding:utf-8 -*-
class Solution:
    def rectCoverDiGui(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        else:
            return Solution().rectCoverDiGui(number-1) + Solution().rectCoverDiGui(number-2)

    def rectCover(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        else:
            result = []
            number1 = 1
            number2 = 2
            result.append(number1)
            result.append(number2)
            for i in range(number):
                number1 = number1 + number2
                result.append(number1)
                if len(result) == number:
                    break
                number2 = number2 + number1
                result.append(number2)
                if len(result) == number:
                    break
        return result[len(result)-1]
