def get_days_later(days):
    if days == 1:
        return "(next day)"
    elif days > 1:
        return f"({days} days later)"


def switch(mer):
    if mer == "AM":
        res = "PM"
    elif mer == "PM":
        res = "AM"
    return res


def add_time(start, duration, day=False):
    week = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]
    days = 0
    half_day = 12
    full_day = half_day * 2
    hrs, mins = start.split(":")
    mins, meridiem = mins.split(" ")
    dur_hrs, dur_min = duration.split(":")

    now_min = int(mins) + int(dur_min)
    now_hrs = int(hrs) + int(dur_hrs) + int(now_min // 60)
    now_min = now_min % 60
    if now_min < 10:
        now_min = "0" + str(now_min)

    if now_hrs >= half_day:
        if meridiem=="PM":
            days+=1
        days += now_hrs // full_day
        now_hrs = now_hrs % full_day
        if now_hrs >= half_day:
            meridiem = switch(meridiem)
            now_hrs -= half_day
        if now_hrs==12 and int(now_min)>0:
            meridiem=switch(meridiem)
        if now_hrs==0:
            now_hrs=12

    if day == False:
        if days == 0:
            res = f"{now_hrs}:{now_min} {meridiem}"
        else:
            res = f"{now_hrs}:{now_min} {meridiem} {get_days_later(days)}"
        return res
    elif day in week:
        week_day = week[int(week.index(day) + days) % 7].capitalize()
        if days!=0:
            res = f"{now_hrs}:{now_min} {meridiem}, {week_day} {get_days_later(days)}"
        else: res = f"{now_hrs}:{now_min} {meridiem}, {week_day}"
        return res
