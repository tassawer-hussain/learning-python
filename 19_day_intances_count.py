import calendar

def count_days(theyear, themonth, whichday):

    daycount = 0

    weeklist = calendar.monthcalendar(theyear, themonth)

    ## monthcalendar returns an array of week lists, like this:
    # [
    #     [0,0,1,1,1,1,1]
    #     [1,1,1,1,1,1,1]
    #     [1,1,1,1,1,1,1]
    #     [1,1,1,1,1,1,1]
    #     [1,1,1,1,0,0,0]
    # ]

    for week in weeklist:
        if week[whichday] != 0:
            daycount += 1

    return daycount

testyear = 2026
testmonth = 5
testday = 5 # 0E=MON - 6-SUN

print(count_days(testyear, testmonth, testday))