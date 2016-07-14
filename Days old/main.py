def isleapyear(n):
    if n%400==0 :
        return True
    else :
        if n%100!=0 and n%4==0:
            return True
    return False
#print isleapyear(2004)
def daysinyear(y,m,d):
    daysOfMonths=[ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result=0
    temp=1
    while temp<m :
        result=result+daysOfMonths[temp-1]
        temp=temp+1
    result=result+d
    if isleapyear(y):
        if m>2:
            result=result+1
    return result
