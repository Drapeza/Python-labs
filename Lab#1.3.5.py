s=input("Введите вашу строку: ")
s=s.lower()

b=''.join(s.split())
b=''.join(b.split(","))
b=''.join(b.split('.'))
b=''.join(b.split('?'))
b=''.join(b.split('!'))

f = False
if b!=b[::-1]:
    print("Строка не является палиндромом")
else:
    print("Строка - палиндром!")
    b = ''.join(s.split(","))
    b = ''.join(b.split('.'))
    b = ''.join(b.split('?'))
    b = ''.join(b.split('!'))

    list1=b.split()

    the_longest=""
    for m in list1:
        if m==m[::-1]:
            f=True
            if len(m)>=len(the_longest):
                the_longest=m

if f:
    print('Самое длинное слово-палиндром: ', the_longest )
else:
    print('Нет отдельных слов-палиндромов')
