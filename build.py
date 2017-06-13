def find_diff(s1, s2):
    set_s1 = set(s1)
    set_s2 = set(s2)
    if set_s1.symmetric_difference(set_s2):
        return list(set_s1.symmetric_difference(set_s2))[0]

print(find_diff('rup', 'ruph'))
