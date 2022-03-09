import datetime

now = datetime.datetime.now()


# 날짜만 취득

print(now.year)
print(now.month)
print(now.day)
print(now.date())
print(now.time())
print("=================================")
# 포맷 지정
nowDate = now.strftime('%Y-%m-%d')
nowTime = now.strftime('%H:%M:%S')
print(now)
print(nowDate)
print(nowTime)
nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDateTime)

#timedelta : 기간을 표현하기 위해 사용
print(datetime.timedelta(days=5, seconds=63000))