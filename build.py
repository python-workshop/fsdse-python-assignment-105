def find_diff(ustring1,ustring2):

    if len(ustring1) > len(ustring2):
        str1 = ustring1
        str2 = ustring2
    else:
        str1 = ustring2
        str2 = ustring2

    for i in str1:
        if i in str2:
            pass
        else:
            print i
    return i
