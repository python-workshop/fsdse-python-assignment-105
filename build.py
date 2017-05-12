#Given two strings, find the single different char

def find_diff(x,y):
    u = list(zip(x,y))
    for i,j in u:
        if i!=j:
            return True
            print(i,j)
        else:
            return False
          
find_diff("IGADKYFHARGNYDAA","KGADKYFHARGNYEAA")