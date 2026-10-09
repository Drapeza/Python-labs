n=int(input("Введите количество точек: "))
if n<=1:
    print("Ошибка! Введите корректные данные.")
else:
    list1=[]
    for i in range(n):
        x=int(input("Введите координату x: "))
        y=int(input("Введите координату y:"))
        list1.append((x,y))

    max_destination=-1
    min_destination=100000000
    for i in range(len(list1)-1):
        for j in range(i+1,len(list1)):
            x1,y1= list1[i]
            x2,y2=list1[j]
            dist = ((x1-x2)**2+(y1-y2)**2)**0.5
            if  dist > max_destination:
                max_destination=dist
            if dist < min_destination:
                min_destination=dist

    m_center_x = 0
    m_center_y=0
    for i in range(len(list1)):
        x,y = list1[i]
        m_center_x+= x
        m_center_y+= y
    print("Максимальное расстояние между двумя: ", round(max_destination, 3))
    print("Минимальное расстояние между двумя: ", round(min_destination, 3))
    print("Центр масс всех точек: ", round(m_center_x/len(list1), 3), round(m_center_y/len(list1), 3))


