import sys
from build import find_diff

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
test(find_diff("IGADKYFHARGNYDAA","KGADKYFHARGNYEAA") == True ) #Two different Strings
test(find_diff("IGADKYFHARGNYDAA","IGADKYFHARGNYDAA") == True ) #Two Equal Strings 

