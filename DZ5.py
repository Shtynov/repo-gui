proceeds = int(input('Введите выручку за месяц: '))
coast = int(input('ведите издержки за месяц: '))
difference = proceeds - coast
if difference > 0:
    print(f'За расчетный ваша фирма принисла прибыль в размере:{difference}')
    workers = int(input("Для расчета прибыли на единицу персонала введите число работников: "))
    profit_per_person = difference / workers
    print(f"Прибыль на 1 работника состовляет:{profit_per_person}")
else:
    print(f"За расчетный месяц у вас убыток в размере:{difference}")
