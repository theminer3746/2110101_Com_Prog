import datetime as dt
import math

bd, bm, by, d, m, y = [int(e) for e in input().split()]

start_date = dt.date(by - 543, bm, bd)
stop_date = dt.date(y - 543, m, d)

start_years_day_count = (dt.date(by - 543, 12, 31) - start_date).days
stop_years_day_count = (stop_date - dt.date(y - 543, 1, 1)).days

intermediate_day_count = (y - by - 1) * 365

total_day = start_years_day_count + intermediate_day_count + stop_years_day_count + 1

physical = math.sin(2 * math.pi * total_day / 23)
emotional = math.sin(2 * math.pi * total_day / 28)
intellectual = math.sin(2 * math.pi * total_day / 33)

print(total_day, "{:.2f}".format(physical), "{:.2f}".format(emotional), "{:.2f}".format(intellectual))
