def find_diff(s1,s2):
    if len(s1)<len(s2):
        str1=s2
        str2=s1
    else:
        str1=s1
        str2=s2
    for i in str1:
        if i in str2:
            pass
        else:
            #print i
            return i
print(find_diff('aabcddd','abbbbccde'))
