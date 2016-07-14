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

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    result=0
    if year1==year2 :
        result=daysinyear(year2,month2,day2)-daysinyear(year1,month1,day1)
    else:
        if isleapyear(year1):
            temp1=366-daysinyear(year1,month1,day1)
        else:
            temp1=365-daysinyear(year1,month1,day1)
        temp2=daysinyear(year2,month2,day2)
        temp=0
        yeartemp=year1+1
        while yeartemp<year2:
            if isleapyear(yeartemp):
                temp=temp+366
            else:
                temp=temp+365
            yeartemp=yeartemp+1
        result=temp+temp1+temp2
    return result

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
                  for (args, answer) in test_cases:
                      result = daysBetweenDates(*args)
                          if result != answer:
                              print "Test with data:", args, result,answer
                                  else:
                                      print "Test case passed!"

test()
