print("Hello World!")

#Тип змінної int, цілі числа
number = 10

#Тип змінної float, не цілі числа
price = 9.99

#Тип змінної String, рядок або текст
name = "Valentine"

#Тип змінної bool(boolean), True або False(1 або 0)
light = True
night = False

print(number)
print(price, name, light, night)

watermelon = 90
print(type(watermelon))

tymophi = 8
matvii = 7

if tymophi > 6:
    print("12 points tymophi")
elif matvii > 6:
    print("12 points matvii")
else:
    print("boys have 2 points")


for i in range(10):
    print("Hello World!")

a = 5

while a < 10:
    a += 1
    print(a)

cherry = 2

if cherry < 3:
    for i in range(3):
        print("Oh, no!")
elif cherry < 5:
    for i in range(3):
        print("Yes!")
else:
    while cherry < 6:
        cherry += 1
        print(cherry)


num = 5

def game():
    num = 10
    print(num)

print(num)
game()