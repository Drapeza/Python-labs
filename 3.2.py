#Записать в файл raise.txt результат повышения окладов: сотрудникам
# с окладом ниже среднего по отделу – на 10 %,
# остальным – на 5 %; указать старый и новый оклад.
# Исходный файл не изменять.

average_salary={}#фонд отдела
worker_salary={}# информация о каждом работнике
dept_worker={}#количество сотрудников в отделе
try:
    with open("staff.txt", "r", encoding="utf-8")as f:
        for numbers, line in enumerate(f,start=1):
            line=line.strip()
            if not line:
                continue
            surname,dept,job,salary=line.split(";")
            salary=float(salary)
            if dept not in average_salary:
                average_salary.setdefault(dept, 0)
                dept_worker.setdefault(dept, 0)
            average_salary[dept]=average_salary.get(dept,0)+salary
            worker_salary.setdefault(surname,[]).append(dept)
            worker_salary.setdefault(surname, []).append(salary)
            dept_worker[dept]=dept_worker.get(dept,0)+1

        for dept in average_salary:
            average_salary[dept]/=dept_worker[dept]

        for surname in worker_salary:
            if worker_salary[surname][1] < average_salary[dept]:
                worker_salary[surname].append(round(worker_salary[surname][1] * 1.1,2))
            else:
                worker_salary[surname].append(round(worker_salary[surname][1] * 1.05,2))
except FileNotFoundError:
    print("Ошибка открытия файла!")
else:
    print("Зарплата по отделам")
    with open("raise.txt","w",encoding="utf-8") as f:
        for surname,info in worker_salary.items():
            print(f"Сотрудник: {surname}; отдел {info[0]}; старая зарпалата {info[1]}; новая зарплата {info[2]}.")
            f.write(f"Сотрудник: {surname}; отдел {info[0]}; старая зарпалата {info[1]}; новая зарплата {info[2]}.\n")