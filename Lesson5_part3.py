a = int(input("Сколько денег у Ивана: "))
b = int(input("Сколько денег у Майкла: "))
x = int(input("Минимум для вложений: "))

if (a >= x) and (b >= x):
    print(2)
elif ((a < x) and (b >= x)) or ((b < x) and (a >= x)):
    print(1)
else:
    print(0)
