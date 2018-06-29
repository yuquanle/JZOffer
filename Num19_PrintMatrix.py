

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        if row == 0 or col == 0:
            return None

        if min(row, col) % 2 == 0:
            layer = min(row, col) / 2
        else:
            layer = min(row, col) / 2 + 1

        result = []
        for i in range(int(layer)):
            k = i
            while k < col - i:
                result.append(matrix[i][k])
                k = k + 1

            k = i + 1
            while k < row - i:
                result.append(matrix[k][col-1-i])
                k = k + 1

            k = col-1-i-1
            while  k>=i and (row - i - 1) != i:
                result.append(matrix[row-1-i][k])
                k = k - 1

            k = row-1-i-1
            while k>=(i+1) and (col-i-1) != i:
                result.append(matrix[k][i])
                k = k - 1

        return result

# M = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
M =[[1],[2],[3],[4],[5]]
solution = Solution()
print(solution.printMatrix(M))



