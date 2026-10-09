catalog = {}
catalog.setdefault("Корм Royal", ["Сухой корм для кошек, 2 кг", 18.40, 26])
catalog.setdefault("Корм Unica", ["Сухой корм для cобак, 2 кг", 15.40, 38])
catalog.setdefault("Корм Fishka", ["Корм для рыбок, 25 гр", 12.40, 50])
catalog.setdefault("Корм Zubastics", ["Корм для грызунов, 3 кг", 20.45, 30])
catalog.setdefault("Клетка для хомяка", ["Клетка 40*50 с поилкой", 35.00, 10])
catalog.setdefault("Аквариум NEMO", ["Стеклянный аквариум на 10л", 18.40, 26])
catalog.setdefault("Игрушка SMILE", ["Резиновый мячик для собак", 10.00, 45])

catalog_list=list(catalog.keys())
print("Здравствуйте! Вы находитесь в каталоге зоомагазина.")
flag1=True
while flag1:
    flag2=True
    print ("КАТАЛОГ ТОВАРОВ ЗООМАГАЗИНА")
    for i in range(len(catalog_list)):
        print("[",i+1,"] - ", catalog_list[i])
    print("[0] - ВЫХОД")
    print ("Какой товар вас интересует? ")

    catalog_choice=int(input())
    if catalog_choice ==0:
        flag1=False
        break
    elif 0<catalog_choice<=len(catalog_list):
        item=catalog_list[catalog_choice-1]

    while flag2:
        print ("Выберите действие: ")
        print("[1] - просмотр описания (название – описание)")
        print("[2] - просмотр цены")
        print("[3] - просмотр количества")
        print("[4] - вся информация о товаре")
        print("[5] - покупка товара")
        print("[0] - в каталог")
        choice=int(input())
        if choice==1:
            print(item,"-",catalog[item][0])
        elif choice==2:
             print("Цена:", catalog[item][1])
        elif choice==3:
             print("Количество:", catalog[item][2])
        elif choice==4:
             print(item,"описание:", catalog[item][0],"цена:", catalog[item][1], "в наличие:", catalog[item][2])
        elif choice==5:
            if catalog[item][2]==0:
                print("К сожалению, товар закончился")
                break

            else:
                flag3=True
                while flag3:
                    amount = int(input("Введите количество товара (в штуках): "))
                    if amount>catalog[item][2]:
                        print("Недостаточно товара на складе! В наличии: ", (catalog[item][2]))
                    else:
                        flag3=False

                flag4 = True
                while flag4:
                    input_sum = int(input("Внесенная покупателем сумма: "))
                    if (catalog[item][1]*amount)>input_sum:
                        print("Недостаточно средств! Внесите сумму еще раз.")
                    else:
                        flag4 = False

                catalog[item][2] = catalog[item][2] - amount
                print()
                print("Заказ успешно сформирован! Идет печать чека...")
                print()
                print("================== ЧЕК ===================")
                print("Наименование товара: ", item)
                print ("Количество товара (в штуках): ", amount)
                print("Цена за единицу товра: ", catalog[item][1])
                print ("ИТОГО: ", catalog[item][1]*amount)
                print("Сдача: ", input_sum-(catalog[item][1]*amount))
        elif choice==0:
            flag2=False
            break


        
