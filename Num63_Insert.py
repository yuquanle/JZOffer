# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data = []
    def Insert(self, num):
        self.data.append(num)
        self.data.sort()
    def GetMedian(self, data):
        if len(self.data) % 2 == 0:
            return (self.data[len(self.data)/2] + self.data[len(self.data)/2-1])/2.0
        else:
            return self.data[len(self.data)/2]