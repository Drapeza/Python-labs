n = int(input("Введите количество элементов списка: "))
list1 = [0] * n
seen = set()
res=[]
for i in range(n):
    list1[i] = int(input("Введите элемент: "))
    if list1[i] not in seen:
        seen.add(list1[i])
        res.append(list1[i])

print(*list1)
count = 0
if len(seen)!=len(list1):
    count=len(list1)-len(seen)

print(*res)
print("Удалено", count)
