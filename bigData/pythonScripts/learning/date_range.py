from datetime import date
from dateutil.rrule import rrule, DAILY

def getting_date_range(start_date, end_date):
	date_range = []
	for date_input in rrule(DAILY, dtstart=start_date, until=end_date):
		date_range.append(date_input.strftime("%Y-%m-%d"))
	return date_range

a = date(2009, 5, 30)
b = date(2009, 6, 9)

info_date = getting_date_range(a, b)
for info in info_date:
	print info


