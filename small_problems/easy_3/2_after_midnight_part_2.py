def after_midnight(time):
    hours, mins = time.split(sep=':')
    return ((int(hours) * 60) + int(mins)) % 1440

def before_midnight(time):
    return -after_midnight(time) % 1440


print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True