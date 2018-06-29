# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.dict_map = {}
        self.s = ''
    # 返回对应char
    def FirstAppearingOnce(self):
        for i in self.s:
            if self.dict_map[i] == 1:
                return i
        return "#"
    def Insert(self, char):
        self.s = self.s + char
        if char in self.dict_map:
            self.dict_map[char] = self.dict_map[char]+1
        else:
            self.dict_map[char]=1