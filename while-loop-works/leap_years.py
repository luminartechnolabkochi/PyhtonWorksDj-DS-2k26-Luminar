# w.a.p display all leap years from 1800-2025

year = 1800


while(year<=2025):

    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):

        print(year)

    year+=1



