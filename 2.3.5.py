#3.	Написать функцию group_by(data, key_func), группирующую элементы в словарь по значению переданной функции-ключа.
# Проверить с lambda, группирующей слова по первой букве и по длине.
# Образец: group_by(["кот", "кит", "пёс"], lambda w: w[0]) → {'к': ['кот', 'кит'], 'п': ['пёс']}.

def group_by(data, key_func):
    groups={}
    for w in data:
        groups.setdefault(key_func(w), []).append(w)
    return groups

n=int(input("Введите количество элементов: "))
while True:
    if n>=0:
        break
    else:
        print("Ошибка! Попробуйте еще раз!")

input_list=[]
for i in range(n):
    input_list.append(input("Введите элемент: "))

while True:
    print("Сгруппировать по:\n"
          "[1] - По первой букве\n"
          "[2] - По длине слова\n"
          "[0] - ВЫХОД")
    while True:
        choice=int(input("Введите ваш выбор: "))
        if choice == 0:
            break
        elif 1<=choice<=2:
            break
        else:
            print("Ошибка! Попробуйте еще раз!")

    if choice == 1:
        total=group_by(input_list, lambda w:w[0])
        print(total)
    elif choice == 2:
        total=group_by(input_list, lambda w: len(w))
        print(total)
    elif choice==0:
        break