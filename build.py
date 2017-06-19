def find_diff(s1,s2):
    set1 = set(s1)
    set2 = set(s2)
    return ''.join(str(s) for s in set1^set2)

#print find_diff('aabcddd','abbbbccde')
