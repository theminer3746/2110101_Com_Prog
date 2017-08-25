import time

day = int(input())
month = int(input())
year = int(input()) - 543

print(time.strptime(str(day) + " " + str(month) + " " + str(year), "%d %m %Y").tm_yday)
