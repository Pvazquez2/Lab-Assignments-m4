str_time = input("What time is it now?")
str_wait_time = input("What is the number of nours to wait?")

time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = (time + wait_time) % 24

print("The alarm will go off at:" , time_when_alarm_go_off)
