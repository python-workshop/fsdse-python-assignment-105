def find_diff(s11, s22):
    s111 = list(set(list(s11)))
    s222 = list(set(list(s22)))
    str_out = [item for item in s222 if item not in s111]
    str_out2 = [item for item in s111 if item not in s222]
    str_out = str_out + str_out2
    str_out = str(str_out)
    return str_out[2]
