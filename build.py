

def find_diff(str1 , str2):

    for x in str1:
        if x not in str2:
            return x

    for y in str2:
        if y not in str1:
            return y


print find_diff('aaabbcdd', 'abdbacade')                     
