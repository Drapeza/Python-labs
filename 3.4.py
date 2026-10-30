#Прочитать staff.json и реализовать перевод сотрудника в другой отдел и изменение оклада
# с сохранением истории изменений в отдельном списке внутри того же файла.
# Обработать отсутствие сотрудника и отдела через KeyError.
import json

def withdraw_menu(choice):
    if choice not in [1,2,3,0]:
        raise ValueError("Указано невозможное значение выбора!\n")

def withdraw(new_salary,salary):
    if new_salary <= salary:
        raise ValueError("Оклад можно только повысить!\n")

def menu():
    print("Выберите действие:\n"
          "[1] - Перевести сотрудника\n"
          "[2] - Повысить оклад сотрудника\n"
          "[3] - Список изменений\n"
          "[0] - ВЫХОД\n")
    choice=int(input("Ваш выбор: "))
    withdraw_menu(choice)
    return choice

workers_info={}
history=[]
try:
    with open("staff.json","r+",encoding="utf-8")as f:
        workers_info = json.load(f)
        history=workers_info.get("История",[])
        while True:
            amount=len(history)+1
            try:
                for i in workers_info:
                    if i == "История":
                        continue
                    print(i,workers_info[i])
                choice = menu()
                if choice==1:
                    try:
                        dept=input("Введите текущий отдел сотрудника: ")
                        surname=input("Введите фамилию сотрудника: ")
                        new_dept = input("Введите новый отдел сотрудника: ")
                        if dept==new_dept:
                            print("Сотрудник уже в этом отделе.")
                            continue
                        else:
                            workers_info[new_dept][surname]=workers_info[dept][surname]
                    except KeyError:
                        print("Сотрудник или отдел не найден.")
                    else:
                        history.append(f"{amount}. Сотрудник: {surname} из {dept} -> {new_dept}\n")
                        print("Сотрудник успешно переведен!")
                        del workers_info[dept][surname]

                elif choice==2:
                    try:
                        dept=input("Введите текущий отдел сотрудника: ")
                        surname=input("Введите фамилию сотрудника: ")
                        new_salary = int(input("Введите новый оклад сотрудника: "))
                        salary=workers_info[dept][surname]["оклад"]
                        withdraw(new_salary, salary)
                        workers_info[dept][surname]["оклад"]=new_salary
                    except KeyError:
                        print("Сотрудник или отдел не найден.")
                    except ValueError as e:
                        print("Ошибка! ", e)
                    else:
                        history.append(f"{amount}. Сотрудник: {surname} оклад {salary} -> {new_salary}")
                        print("Оклад сотрудника успешно повышен!")

                elif choice==3:
                    if history:
                        for i in history:
                            print(i)
                    else:
                        print("Нет изменений.")

                elif choice==0:
                    print("Заврешение работы.")
                    break
            except ValueError:
                print("Ошибка ввода!")
        f.seek(0)
        f.truncate()
        workers_info["История"]=history
        json.dump(workers_info,f,ensure_ascii=False,indent=4)
except FileNotFoundError:
    print("Файл не найден!")







