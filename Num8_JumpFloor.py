

# -*- coding:utf-8 -*-
class Solution:
    # 从3开始，3分解为后退1和后退2得到的数的次数和,可以用递归
    def jumpFloorDiGui(self, number):
        if number == 1 or number == 2:
            return number
        else:
            return Solution().jumpFloorDiGui(number-1) + Solution().jumpFloorDiGui(number-2)

    def jumpFloor(self, number):
        if number == 1 or number == 2:
            return number
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

solution = Solution()
print(solution.jumpFloor(3))