#Сохранить сведения о сотрудниках в staff.json со структурой {отдел: {фамилия: {"должность": ..., "оклад": ...}}}.
# Образец: {"ИТ": {"Иванов": {"должность": "инженер", "оклад": 2400}}}
import json
workers_info={}
try:
    with open("staff.txt","r",encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            surname, dept, job, salary=line.split(";")
            salary=round(float(salary),2)
            workers_info.setdefault(dept,{})
            workers_info[dept].setdefault(surname,{})
            workers_info[dept][surname].setdefault("должность",job)
            workers_info[dept][surname].setdefault("оклад",salary)
except FileNotFoundError:
    print("Не удалось открыть файл!")
try:
    with open("staff.json","w",encoding="utf-8") as f:
        json.dump(workers_info,f,ensure_ascii=False,indent=4)
except FileNotFoundError:
    print("Не удалось записать в файл!")
else:
    print("Данные успешно загружены!")