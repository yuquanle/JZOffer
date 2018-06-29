# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.visit = {}

    def moving(self, threshold, rows, cols, row, col):
        if row/10 + row%10 + col/10 + col%10 > threshold:
            return 0
        if row >= rows or col >=cols or row<0 or col <0:
            return 0
        if (row, col) in self.visit:
            return 0
        self.visit[(row, col)] = 1

        return 1 + self.moving(threshold, rows, cols, row-1, col)\
               + self.moving(threshold, rows, cols, row+1, col)\
               + self.moving(threshold, rows, cols, row, col-1) \
                + self.moving(threshold, rows, cols, row, col+1)

    def movingCount(self, threshold, rows, cols):
        return self.moving(threshold, rows, cols, 0, 0)
