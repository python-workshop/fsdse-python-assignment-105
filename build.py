def find_diff(s1,s2):
    common = set(s1).intersection(set(s2))
    s_1 = set(s1)
    s_2 = set(s2)
    d1 = s_1.difference(s_2)
    d2 = s_2.difference(s_1)
    d1.update(d2)
    return d1.pop()



find_diff('aaabbbccdd','aabbccddee')
