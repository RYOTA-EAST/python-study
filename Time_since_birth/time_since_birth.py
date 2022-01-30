import datetime
import math

year = int(input("誕生年を入力してください:"))
month = int(input("誕生月を入力してください:"))
day = int(input("誕生日を入力してください:"))
hour = int(input("誕生時間を入力してください:"))
birth_time = datetime.datetime(year, month, day, hour)

dt_now = datetime.datetime.now()
td = dt_now - birth_time

print("現在時刻は", dt_now)
print("あなたの誕生時刻は", birth_time)
print(td)
print("あなたは", math.floor(td.days/365), "歳です")

if dt_now.month == birth_time.month and dt_now.day == birth_time.day:
  print("誕生日おめでとう")
