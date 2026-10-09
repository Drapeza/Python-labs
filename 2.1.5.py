#1.	Написать функцию discount(price, percent=10), возвращающую цену со скидкой,
# и функцию final_prices(prices,percent=10), применяющую её ко всему списку цен.
# Образец: final_prices([100, 250]) → [90.0, 225.0].
def discount(price, percent=10):
    price=round (price *(1-percent*0.01), 2)
    return price

def final_price(summ,percent=10):
    for i in range(len(summ)):
        summ[i]=discount(summ[i],percent)
    return summ

while True:
    summa=float(input("Введите цену: "))
    if summa<=0:
        print("Ошибка! Попробуйте еще раз!")
    else:
        summa=round(summa,2)
        break
while True:
    percent_discount=float(input("Введите процент скидки: "))
    if 0<percent_discount<=100:
        percent_discount=round(percent_discount, 2)
        break
    else: print("Ошибка! Попробуйте еще раз!")

print("Ваша цена со скидкой", discount(summa, percent_discount))

sum_list=[]
while True:
    n = int(input("Введите количество цен: "))
    if n<=0:
        print("Ошибка! Попробуйте еще раз!")
    else: break


while True:
    sum_percent_discount = float(input("Введите процент скидок: "))
    if 0<sum_percent_discount<=100:
        sum_percent_discount=round(sum_percent_discount, 2)
        break
    else: print("Ошибка! Попробуйте еще раз!")

for i in range(n):
    while True:
        a=(float(input("Введите цену товара: ")))
        if a <= 0:
            print("Ошибка! Попробуйте еще раз!")
        else:
            a= round(a, 2)
            sum_list.append(a)
            break

b=final_price(sum_list, sum_percent_discount)
print("Итого стоимость каждого товара соответственно: ", b)
