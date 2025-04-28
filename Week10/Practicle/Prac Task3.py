class NumOrStr:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        is_self_num = isinstance(self.value, int)
        is_other_num = isinstance(other.value, int)
        
        if is_self_num and is_other_num:
            return self.value < other.value
        elif not is_self_num and not is_other_num:
            return self.value > other.value
        else:
            return is_self_num

    def __repr__(self):
        return "%s" % self.value


n1 = NumOrStr(67)
n2 = NumOrStr("k")
n3 = NumOrStr(17)
n4 = NumOrStr("z")
n5 = NumOrStr("t")
n6 = NumOrStr(3)
n7 = NumOrStr("m")
n8 = NumOrStr(14)
n9 = NumOrStr(78)
l = [n1, n2, n3, n4, n5, n6, n7, n8, n9]


l.sort()
print(l)  