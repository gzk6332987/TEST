import datetime
a = datetime.date(2022,9,1)
b = datetime.date(2019,6,3)

print(datetime.datetime.today().strftime("%Y-%m-%d %H:%m:%S"))

x = a - b
print(x.days)