def find_diff(string, compare):
    set1 = set()
    set2 = set()
    for char in string:
        set1.add(char)
    for char in compare:
        set2.add(char)
    print set1
    print set2
    if set1.symmetric_difference(set2):
        return list(set1.symmetric_difference(set2))[0]
