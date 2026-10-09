#5.	Написать декоратор timer, измеряющий время выполнения функции (модуль time)
# и печатающий его с точностью до миллисекунд, не изменяя возвращаемое значение.
# Применить к рекурсивной и итеративной версиям вычисления факториала и сравнить время на больших значениях.

import time
import sys
sys.setrecursionlimit(3000)

def time_counter(func):
    def wrapper(*args, **kwargs):
        start=time.perf_counter()
        print("Вызов функции:", func.__name__)
        result=func(*args,**kwargs)
        end=time.perf_counter()
        print("Время выполнения:",round((end-start)*1000,3))
        return result
    return wrapper

@time_counter
def recursion(x):

    def rec(a):
        if a<=1:
            return 1
        else:
            return rec(a-1)*a

    return rec(x)

@time_counter
def iterative(x):
    f=1
    for i in range(1,x+1):
        f*=i
    return f

while True:
    n = int(input("Введите число: "))
    if n >0:
        break
    else:
        print("Ошибка! Введите число еще раз.")

while True:

    choice=int(input("Выберите действие:\n"
                     "[1] - Вычислить рекурсивно\n"
                     "[2] - Вычислить итеративно\n"
                     "[0] - ВЫХОД\n"))
    if choice==1:
        print("Результат: ", recursion(n))
    elif choice==2:
        print("Результат: ", iterative(n))
    elif choice==0:
        print("Завершение работы")
        break