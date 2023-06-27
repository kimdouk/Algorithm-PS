date = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
x,y = map(int,input().split())
day = 0
for i in range(1,x):
    day+=month[i]
day += y
print(date[day%7])