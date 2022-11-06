from datetime import datetime

date_time_str = '02 09 2022'

date_time_obj = datetime.strptime(date_time_str, '%d %m %Y')

print ("The type of the date is now",  type(date_time_obj))
print ("The date is", date_time_obj)

s = date_time_obj.strftime('%Y-%m-%d')
print(s)