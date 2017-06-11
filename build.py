def find_diff(s1,s2):
    if s1 is not None  and s2 is not None:
        if len(s1) == 0:
            return s2
        elif len(s2) == 0:
            return s1
        else:
            for i in range(0,len(s1)):
                if s2.find(s1[i]) == -1:
                    return s1[i]
            for i in range(0,len(s2)):
                if s1.find(s2[i]) == -1:
                    return s2[i]
