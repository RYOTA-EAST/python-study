import datetime

words = ["A", "happy", "new", "year"]

year = str(datetime.date.today())

words.append(year)

print(" ".join(words))