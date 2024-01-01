"""
Introduction

Not having to go to school or work on your birthday is always a treat, so when your birthday would have fallen on a weekend, it's really annoying if a leap year means you miss out. Some friends are discussing this and think they have missed out more than others, so they need your help.
The Challenge

Given a list of friends, their dates of birth and the date of their conversation, work out who has had the most birthdays fall on a Saturday or Sunday up to and including the date of the conversation. If more than one friend shares that number of weekend birthdays, return the youngest. If the youngest shares their birthday with other friends, then any of the youngest will be accepted.

When counting weekend days, don't include the day on which they were born - after all, they wouldn't have been familiar with the concept of a weekend right then! Friends born on 29th February celebrate their birthdays on 28th February in non-leap years.
Example

The friends are provided as a list of tuples containing their name and their date of birth in the format YYYY-MM-DD. The date of their conversation is provided in the similar format.

most_weekend_birthdays([("Alice", "2010-11-10"), ("Bob", "2010-11-23")], "2022-12-31") ==> "Alice"

Alice has four birthdays falling on a weekend (Saturday in 2012 and 2018, Sunday in 2013 and 2019) compared to three for Bob (Saturday in 2013 and 2019, Sunday in 2014).
"""
from datetime import datetime, date

def most_weekend_birthdays(friends, conversation_date):
    info = {friend: 0 for friend in friends}
    youngest = ["", datetime.strptime("1500-01-01", "%Y-%m-%d")]
    for friend in friends:
        con_date = datetime.strptime(conversation_date, "%Y-%m-%d")
        b_date = datetime.strptime(friend[1], "%Y-%m-%d")
        is_leap = False
        if b_date.day == 29 and b_date.month == 2:
            is_leap = True
            b_date = b_date.replace(year=b_date.year + 1, day=28)
        else:
            b_date = b_date.replace(year=b_date.year + 1)
        years = con_date.year - b_date.year + 1
        if con_date.month < b_date.month or (con_date.month == b_date.month and con_date.day < b_date.day):
            years -= 1
        for _ in range(years):
            if b_date.weekday() > 4:
                info[friend] += 1
            try:
                if is_leap:
                    b_date = b_date.replace(year=b_date.year + 1, day=29)
                else:
                    b_date = b_date.replace(year=b_date.year + 1)
            except:
                b_date = b_date.replace(year=b_date.year + 1, day=28)
    most = max(info.values())        
    for friend, count in info.items():
        b_day = datetime.strptime(friend[1], "%Y-%m-%d")
        if count == most and b_day > youngest[1]:
            youngest = [friend[0], b_day]
    return youngest[0]
