#4.	Написать рекурсивную функцию bin_search(data, target, low=0, high=None),
# выполняющую двоичный поиск в отсортированном списке и
# возвращающую индекс элемента или -1. Образец: bin_search([1, 4, 7, 9], 7) → 2.
import random
def bin_search(data, target, low=0, high=None):
    low=0
    if high is None:
        high=len(data)-1
        low=0
    if low>high:
        return -1

    mid=(low+high)//2
    if data[mid]==target:
        return mid
    elif data[mid]<target:
        return bin_search(data,target,mid+1,high)
    else:
        return bin_search(data,target,low, mid-1)


search_list=[]

for i in range(15):
    search_list.append(random.randint(-50,50))

print("Список по умочанию:", *search_list)
search_list.sort()
print("Введите число для поиска из отсортированного списка:\n", *search_list)
while True:
    n=int(input())
    if n in search_list:
        break
    else:
        print("Ошибка, попробуйте еще раз!")

print("Элемент находится в списке под индексом: ", bin_search(search_list,n))



