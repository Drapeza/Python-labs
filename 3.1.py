#Текстовый файл staff.txt содержит строки Фамилия;Отдел;Должность;Оклад.
# Прочитать файл, построить словарь {отдел: [фамилии]},
# вывести численность и фонд оплаты труда каждого отдела.
# Образец: {'ИТ': ['Иванов', 'Петров'], 'Бухгалтерия': ['Сидорова']}.
with open("staff.txt", "w", encoding="utf-8") as f:
    f.write("Иванов;ИТ;Джун;500\n"
            "Петров;ИТ;Миддл;700\n"
            "Капустин;Бухгалтерия;Бухгалтер;600\n"
            "Голубев;Бухгалтерия;Главный Бухгалтер;650\n"
            "Мышкин;Маркетинга;Маркетолог;700\n"
            "Кусков;Разработка;Инженер;800\n")
workers={}
fund=0
amount=0
try:
    with open("staff.txt","r",encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            try:
                surname,dept,job,salary=line.split(";")
                salary=float(salary)
            except ValueError:
                print("Error")
            else:
                workers.setdefault(dept,[])
                workers[dept].append(surname)
                amount+=1
                fund+=salary
except FileNotFoundError:
    print("Error")
else:
    print(f"Кол-во сотрудников: {amount}, общий фонд: {fund}.")



