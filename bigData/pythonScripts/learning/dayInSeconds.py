from datetime import datetime, time

utcnow = datetime.utcnow()
midnight_utc = datetime.combine(utcnow.date(), time(0))
delta = utcnow - midnight_utc
print delta.seconds # <-- careful





