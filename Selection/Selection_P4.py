from math import ceil

enter_hour = int(input())
enter_minute = int(input())

exit_hour = int(input())
exit_minute = int(input())

start_time = 60 * enter_hour + enter_minute
stop_time = 60 * exit_hour + exit_minute

elapsed_time = stop_time - start_time

if elapsed_time <= 15:
    print(0)
elif 15 < elapsed_time <= 180:
    print(ceil(elapsed_time / 60) * 10)
elif 180 < elapsed_time <= 360:
    print(30 + ceil((elapsed_time - 180) / 60) * 20)
else:
    print(200)
