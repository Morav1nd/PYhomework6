import random

a = random.randint (5, 15)
array1 = [random.randint (5, 15) for i in range(a)]
print(array1)
print("введите мнимальное число диапазона")
b = int(input())
print("введите максимальное число диапазона")
c = int(input())
for i in range(len(array1)):
    if b <= array1[i] <= c:
        print(i)
