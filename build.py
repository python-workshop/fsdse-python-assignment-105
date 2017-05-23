def find_diff(str1, str2):
    if str1 is None or str2 is None:
        raise TypeError('str1 or str2 cannot be None')
    seen = {}
    for char in str1:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1
    for char in str2:
        try:
            seen[char] -= 1
        except KeyError:
            return char
        if seen[char] < 0:
            return char
    return None
