#To get the single different char between two strings

def find_diff(inputString1,inputString2):
    for i in inputString1:
        if(i in inputString2):
            flag = True
        else:
            print i
            return i


    if(flag == True):
        for j in inputString2:
            if(j in inputString1):
                flag = True
            else:
                print j
                return j


find_diff("aaabbcdd","abdbacade")
