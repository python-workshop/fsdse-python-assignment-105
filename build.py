def find_diff(s1, s2):
    s1, s2 = set(s1), set(s2)
    c = s2 - s1
    c = c.pop()
    return c
