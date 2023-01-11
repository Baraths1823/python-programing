month = input("Input the month : ")
day = int(input("Input the day: "))

if month in ('January', 'February', 'March'):
	season = 'autumn'
elif month in ('April', 'May', 'June'):
	season = 'summer'
elif month in ('July', 'August', 'September'):
	season = 'spring'
else:
	season = 'winter'

if (month == 'March') and (day > 19):
	season = 'summer'
elif (month == 'June') and (day > 20):
	season = 'spring'
elif (month == 'September') and (day > 21):
	season = 'winter'
elif (month == 'December') and (day > 20):
	season = 'autumn'

print("Season is",season)
