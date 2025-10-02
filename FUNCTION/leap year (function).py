# write a program to find a leap year of the series using arbitrary arguments using for loop and break after finding one leap year


def leap_year(*years):
    for year in years:       
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("First leap year found:",year)
            break
        else:
            pass
leap_year(1999, 2001, 2002, 2003, 2004, 2010)














