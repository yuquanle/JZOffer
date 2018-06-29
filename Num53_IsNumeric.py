import re
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        m = re.compile("[+-]?[0-9]*([.][0-9]*)?([eE][+-]?[0-9]+)?")
        if re.match(m, s).group() == s:
            return True
        else:
            return False
