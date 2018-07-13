
def find_diff(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError('Input must be string')

    if len(s1) > len(s2):
        return list(set(s1)-set(s2))[0]
    else:
        return list(set(s2)-set(s1))[0]

print(find_diff('abcd', 'abcde'))
