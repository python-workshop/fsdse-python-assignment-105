def find_diff(s1, s2):
    if s1 is None or s2 is None:
        return None
    else:
        l1 = []
        l2 = []
        for item in s1:
            l1.append(item)
        for item in s2:
            l2.append(item)

        s1 = set(l1)
        s2 = set(l2)
        return list(s1.union(s2) - s1.intersection(s2))[0]
