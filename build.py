def find_diff(s1, s2):
    if s1 is None or s2 is None:
        raise TypeError()

    print set(s2).difference(s1)
    return list(set(s2).difference(s1))[0]
