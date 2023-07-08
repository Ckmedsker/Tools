total = 0
while True:
    time = input(
        "Enter an amount of time in the format of HOUR:MINUTES; EX: 1:30:\n")
    if ":" in time:
        time_list = time.split(":")
        time_hour = int(time_list[0])
        time_minutes = int(time_list[1])
        time_total = time_minutes + (time_hour * 60)
        total = time_total + total
    else:
        time = int(time)
        total = time + total
    print(total)
