day = int(input(f"Введите результат пробежки в перввый день в км.:  "))
result = int(input(f":Желаемый результат в км.: "))
while day <= 0 or result <= day:
    print('Введите положительное число: ')
    break
else:
    day2 = (day*0.1) + day
    day3 = (day2*0.1) + day2
    day4 = (day3*0.1) + day3
    day5 = (day4*0.1) + day4
    day6 = (day5*0.1) + day5
    print(f'1-й день:{day}')
    print('2-й день:' + '{:=2.3}'.format(day2))
    print('3-й день:' + '{:=2.3}'.format(day3))
    print('4-й день:' + '{:=2.3}'.format(day4))
    print('5-й день:' + '{:=2.3}'.format(day5))
    print('6-й день:' + '{:=2.3}'.format(day6))
    if result <= day:
        print("Требуется 1 день")
    if day < result < day2:
        print("Требуется 2 дня")
    if day2 < result < day3:
        print("Требуется 3 дня")
    if day3 < result < day4:
        print("Требуется 4 дня")
    if day4 < result < day5:
        print("Требуется 5 дней")
    if day5 < result < day6:
        print("Требуется 6 дней")
    if day6 < result:
        print("Требуется больше 6 дней")