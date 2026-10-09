#Написать функцию student_report(name, *marks, ndigits=2),
#возвращающую кортеж (имя, средний балл, максимальная оценка, количество оценок).
# Пустой список оценок обработать корректно. Образец: student_report("Иван", 8, 9, 10) → ('Иван', 9.0, 10, 3).

def student_report(name, *marks, ndigits=2):
    if not marks:
        return (name, 0.0, 0, 0)
    else:
        average_mark=round(sum(marks)/len(marks),ndigits)
        max_mark=max(marks)
        min_mark=min(marks)
        return (name,average_mark, max_mark, min_mark)



while True:
    print("[1] - Внести нового ученика\n"
          "[2] - ВЫХОД")
    while True:
        choice = int(input("Введите действие: "))
        if 1<=choice <=2:
            break
        else: print("Ошибка! Попробуйте еще раз!")

    if choice == 1:
        marks=[]
        name=input("Введите имя ученика: ")
        while True:
            a=int(input("Введите оценку(СТОП - [0]): "))
            if a == 0: break
            elif 1<=a<=10: marks.append(a)
            else:print("Ошибка! Попробуйте еще раз!")

        person=student_report(name,*marks)
        print(*person)
    if choice == 2:
        break