#Текстовый файл staff.txt содержит строки Фамилия;Отдел;Должность;Оклад. П
# рочитать файл, построить словарь {отдел: [фамилии]},
# вывести численность и фонд оплаты труда каждого отдела.
# Образец: {'ИТ': ['Иванов', 'Петров'], 'Бухгалтерия': ['Сидорова']}.

with open("staff.txt", "w", encoding="utf-8") as f:
    f.write("Иванов;ИТ;Джун;500\n"
            "Петров;ИТ;Миддл;700\n"
            "Капустин;Бухгалтерия;Бухгалтер;600\n"
            "Голубев;Бухгалтерия;Главный Бухгалтер;650\n"
            "Мышкин;Маркетинга;Маркетолог;700\n"
            "Кусков;Разработка;Инженер;800\n")


stock={}
people_dict={}
dept_amount={}
with open("staff.txt","r",encoding="utf-8") as f:
    for line in f:
        if not line:
            continue

        parts = line.strip().split(";")
        if len(parts)!=4:
            continue
        surname, dept, job, salary = parts
        salary=float(salary)

        if dept not in people_dict:
            people_dict[dept]=[]
            people_dict.setdefault(dept,[]).append(surname)
        else:
            people_dict.setdefault(dept, []).append(surname)

        if dept not in dept_amount:
            dept_amount[dept]=[0,0.0]

        dept_amount[dept][0]+=1
        dept_amount[dept][1]+=salary

print("Словарь отделов:", people_dict)

print("Статитстика по отделам:")
for dept, stats in dept_amount.items():
    amount=stats[0]
    budget=stats[1]
    print(f"Отдел: {dept}, кол-во сотрудников: {amount}, фонд отдела: {budget}")










