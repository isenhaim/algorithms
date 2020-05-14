print("Введите год для определения високосности: ")
year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Год високосный")
        else:
            print("Год не високосный")
    else:
        print("Год високосный")
else:
    print("Год не високосный")
