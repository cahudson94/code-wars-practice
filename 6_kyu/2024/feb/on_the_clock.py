"""
In this kata, you are given a list containing the times that employees have clocked in and clocked out of work.

Your job is to convert that list into a list of the hours that employee has worked for each sublist

e.g.:

clock = [ ["2:00pm", "8:00pm"], ["8:00am", "4:30pm"] ] == [6.0, 8.5]

Convert the time into a floating point number where: 15 min == .25 30 min == .5 45 min == .75 60 min == 1.

Also, you MUST round each number to the nearest .25. At this worksite, you pay by intervals of 15 minutes.

So if someone worked 9.21 hours exactly, round it to 9.25.

If the start time and the end time are exactly the same, that person would have worked 0.0 hours

Sometimes an employee will start work in the afternoon and clock out in the am. Your code will need to be able to handle this.
"""

from datetime import datetime, timedelta

def convert_times(start, end):
    start = datetime.strptime(start, '%I:%M%p')
    end = datetime.strptime(end, '%I:%M%p')
    if end < start:
        end += timedelta(days=1)
    return round(4 * (end - start).total_seconds() / 3600) / 4

def get_hours(shifts):
    return [convert_times(start, end) for start, end in shifts]
