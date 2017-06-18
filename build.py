def find_diff(s1,s2):
    if(s1==None and s2==None):
        return None
    if(s1=="" and s2==""):
        return ""
    if(s1=="" and s2!=""):
        return s2[0]
    if(s1!="" and s2==""):
        return s1[0]
    if((s1=="" and s2==None) or (s1==None and s2=="")):
        return ""
    list1=list(s1)
    list2=list(s2)
    for i in range(len(list1)):
        if list1[i] not in list2:
            return list1[i]
    for i in range (len(list2)):
        if list2[i] not in list1:
            return list2[i]
print find_diff("abcd","abcde")
