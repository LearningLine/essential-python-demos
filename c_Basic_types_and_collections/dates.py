from datetime import datetime
from datetime import date
from datetime import timedelta

def run_dates():
    now = datetime.now()
    print(now)

    print("The year is {0}".format(now.year))

    print(date.today())

    dt = timedelta(hours=32)
    later = now + dt

    print(later)