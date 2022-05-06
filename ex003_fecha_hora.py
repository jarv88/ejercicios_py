#import datetime
from datetime import datetime

now = datetime.now()

print(now)

#print(type(now))

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

print("Year:", year)

