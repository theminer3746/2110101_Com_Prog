hour_start = int(input())
minute_start = int(input())
second_start = int(input())

hour_end = int(input())
minute_end = int(input())
second_end = int(input())

timestamp_start = hour_start * 3600 + minute_start * 60 + second_start
timestamp_end = hour_end * 3600 + minute_end * 60 + second_end

total_elapsed_time_in_second = timestamp_end - timestamp_start

elapsed_hour = total_elapsed_time_in_second // 3600
elapsed_minute = (total_elapsed_time_in_second - (3600 * elapsed_hour)) // 60
elapsed_second = (total_elapsed_time_in_second - (3600 * elapsed_hour)) - (60 * elapsed_minute)

if timestamp_start > timestamp_end:  # Hour flip need to be perform
    elapsed_hour += 24

print(str(elapsed_hour) + ":" + str(elapsed_minute) + ":" + str(elapsed_second))
