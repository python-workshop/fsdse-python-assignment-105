def find_diff(string1, string2):
    s = set(string1)
    for char in string2:
        if char not in s:
            return char
