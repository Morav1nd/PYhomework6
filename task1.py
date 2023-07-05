a = int(input())
b = int(input())
c = int(input())
array = []
for i in range(c):
    a +=b 
    array.append(a)
array.insert(0, array[0]-b)
print(array)