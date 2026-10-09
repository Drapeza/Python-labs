n = int(input("Введите количество элементов списка: "))
list = [0] * n

seen = set()
for i in range(n):
    list[i] = int(input("Введите элемент: "))
    seen.add(list[i])

print(*list)
count = 0
for i in range(n):
    if seen[i] != list[i]:
        count += 1
        list[i].pop()

print(*list)
print("Удалено", count)
