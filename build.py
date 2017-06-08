def find_diff(s1, s2):
    str1 = set()
    str2 = set()
    for c in s1:
        str1.add(c)
    for c in s2:
        str2.add(c)
    print(str1)
    print(str2)

    if str1.symmetric_difference(str2):
        return list(str1.symmetric_difference(str2))[0]

print(find_diff('123B', '123'))
