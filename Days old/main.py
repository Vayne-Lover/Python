def isleapyear(n):
    if n%400==0 :
        return True
    else :
        if n%100!=0 and n%4==0:
            return True
    return False
#print isleapyear(2004)
