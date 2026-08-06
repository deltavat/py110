#def time_of_day(minutes):
#   time = divmod(minutes, 60)
#
#   if -1440 < minutes < 0:
#       return f'{24 - abs(time[0]):02d}:{time[1]:02d}'
#   if minutes < -1440:
#       return f'{time[0] // (24 * (minutes//1440)//2):02d}:{time[1]:02d}'
#   elif minutes > 1440:
#       return f'{time[0] // (24 * (minutes//1440)//2):02d}:{time[1]:02d}'
#   else:
#       return f'{time[0]:02d}:{time[1]:02d}'

def time_of_day(minutes):
    minutes_in_day = minutes % 1440
    hours, minutes = divmod(minutes_in_day, 60)
    
    return f"{hours:02d}:{minutes:02d}"

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

