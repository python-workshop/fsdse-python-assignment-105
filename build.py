def find_diff(s1,s2):
    if s1 == None:
        if s2 == None:
            return None
        return None

    str1 = set(s1)
    str2 = set(s2)
    diff_1 = str1.difference(str2)     # empty set
    diff_2 = str2.difference(str1)     # set(different element)
    diff_1.update(diff_2)              # Update the empty set with different element
    return diff_1.pop()                # Removes the different element
