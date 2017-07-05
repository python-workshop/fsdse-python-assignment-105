def find_diff(a,b) :
    s1 = list(set(list(a)))
    s2 = list(set(list(b)))
    str_out = [item for item in s2 if item not in s1]
    str_out2 = [item for item in s1 if item not in s2]
    str_out = str_out + str_out2
    str_out = str(str_out)
    return str_out[2]
