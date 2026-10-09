list1=[]
people={}
people_sum_hours={}
people_sum_days={}
people_date={}

n = int(input("Введите количество записей организации: "))
if n<=0:
    print("Ошибка! Введите корректные данные.")
else:
    for i in range(n):
        name=input("Введите имя сотрудника: ")
        date=input("Введите дату: ")
        people_date[date] = people_date.setdefault(date,0)+1
        people_sum_days[name]=people_sum_days.get(name,0)+1
        hours=int(input("Введите кол-во часов работы: "))
        people.setdefault(name,{})[date]=hours
        people_sum_hours[name] = people_sum_hours.get(name, 0) + hours
        person_tuple = (name, date, hours)
        list1.append(person_tuple)


    people_sum_hours_reversed = [(hours, name) for name, hours in people_sum_hours.items()]
    people_sum_hours_reversed.sort(reverse=True)
    f=False

    #те, кто работал в сумме больше 40 ч
    print("Превысили норму в 40 рабочих часов следующие сотрудники: ")
    for hours, name in people_sum_hours_reversed:
        if hours>40:
            print(name, hours, end="\n")
            f=True
    if not f:
        print("Таких сотрудников пока нет. Надо работать больше!")

    #даты, в которые работали не все
    for date in people_date:
        if people_date.get(date)!=len(people):
            print(date, " - в этот день работали не все сотрудники")

    #cр кол-во часов/день у сотрудника
    print("Все сотрудники(среднее кол-во часов работы в день): ")
    for name, hours in people_sum_hours.items():
        print("Сотрудник:", name, "Среднее кол-во часов работы: ", hours/people_sum_days[name])

    print("Все сотрудники: ", *list1)


