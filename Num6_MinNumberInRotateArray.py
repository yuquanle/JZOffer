

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        else:
            for i in range(len(rotateArray)-2):
                if rotateArray[i] > rotateArray[i+1]:
                    return rotateArray[i+1]
            # 未旋转情况
            return rotateArray[0]


solution = Solution()
minlist = [5, 5, 5]
print(solution.minNumberInRotateArray(minlist))
