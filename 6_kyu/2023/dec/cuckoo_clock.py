"""
"""

def hour_change(h, n):
    if h == 12:
        h = 1
    else:
        h += 1
    return h, 0, n - h

def cuckoo_clock(initial_time, n):
	n = n % 114 if n > 114 + 15 else n
    h, m = map(int, initial_time.split(":"))
    if m % 15:
        m += 15 - (m % 15)
        if m == 60:
            h, m, n = hour_change(h, n)
        else:
            n -= 1
    else:
        if m == 0:
            n -= h
        else:
            n -= 1
    while n > 0:
        if m in [0, 15, 30]:
            n -= 1
            m += 15
        else:
            h, m, n = hour_change(h, n)
    return ":".join([f"{h:02}", f"{m:02}"])
