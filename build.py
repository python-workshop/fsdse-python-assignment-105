def find_diff(s1, s2):
    s = set(s1)
    for char in s2:
        if char not in s:
            return char
