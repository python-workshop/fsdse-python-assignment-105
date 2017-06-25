def find_diff(s1,s2):
    try:
        if type(s1) != str or type(s2) != str:
            raise TypeError('incorrect data type')
        s1list = list(set(s1))
        s2list = list(set(s2))
        total_list = s1list + list((set(s2) - set(s1)))
        for char in total_list:
            if char in s1list and char not in s2list:
                return char
            elif char in s2list and char not in s1list:
                return char
            else:
                pass
    except TypeError as e:
        print e
