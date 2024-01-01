"""
Mayan Calendar

The Mayan civilisation used three different calendars. In their long count calendar there were 20 days (called kins) in a uinal, 18 uinals in a tun, 20 tuns in a katun and 20 katuns in a baktun. In our calendar, we specify a date by giving the day, then month, and finally the year. The Maya specified dates in reverse, giving the baktun (1-20), then katun (1-20), then tun (1-20), then uinal (1-18) and finally the kin (1-20).

The Mayan date 13 20 7 16 3 corresponds to the date 1 January 2000 (which was a Saturday).

Write a program which, given a Mayan date (between 13 20 7 16 3 and 14 1 15 12 3 inclusive), outputs the corresponding date in our calendar. You should output the month as a number.
Example:

13 20 9 2 9  # Mayan date 22 March 2001
22 3 2001  # Gregorian date 22 March 2001

You are reminded that, in our calendar, the number of days in each month is:

1    January    31
2    February    28 / 29 (leap year)
3    March    31
4    April    30
5    May    31
6    June    30
7    July    31
8    August    31
9    September    30
10    October    31
11    November    30
12    December    31

Input/Output

    [input] string representing the Mayan date in the form baktun katun tun uinal kin
    [output] string representing the Gregorian date in the form dd mm yyyy
"""

from datetime import datetime, timedelta

def convert_mayan(date):
    baktun, katun, tun, uinal, kin = [int(x) for x in date.split()]
    days = (144000 * baktun) + (7200 * katun) + (360 * tun) + (20 * uinal) + kin - 2018843 # jan_1_2000
    return (datetime(2000, 1, 1) + timedelta(days=days)).strftime("%-d %-m %Y")
