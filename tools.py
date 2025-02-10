from datetime import datetime

# Function to convert input date to unix date system
def times_unix(date_time):
    date,time=date_time.split(' ')
    year,month,day=[int(item) for item in date.split('-')]
    hour,minute,seconds=[int(item) for item in time.split(':')]

    time_unix=datetime(year,month,day,hour,minute,seconds).timestamp()
    return int(time_unix)