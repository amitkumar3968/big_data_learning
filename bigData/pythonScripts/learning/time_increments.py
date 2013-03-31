
import datetime
time_print = str(datetime.timedelta(seconds=37000))
time_print = time_print[:5]
time_new = time_print.split(":")
print time_new
time_new = time_new[0] + time_new[1]
print time_new

