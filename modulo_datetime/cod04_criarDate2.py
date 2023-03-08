from datetime import date

data = date.today()

print(data)

data = data.replace(day=11, month=12, year=2095)

print(data)
