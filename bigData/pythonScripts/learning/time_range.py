
from datetime import datetime, timedelta

def parse_time(s):
    ''' Parse 12-hours format '''
    return datetime.strptime(s, '%I:%M %p')

starttime = parse_time('8:00 AM')
endtime   = parse_time('3:00 AM')
if endtime < starttime:
   # add 1 day to the end so that it's after start
   endtime += timedelta(days=1)

checked_time = parse_time('7:00 AM')
print checked_time
# Can compare:
#print starttime <= checked_time < endtime
