def find_diff(string1, string2):
    return False if string1 is None else \
    ''.join([x for x in string1 if x not in string2]) or ''.join([x for x in \
    string2 if x not in string1])
