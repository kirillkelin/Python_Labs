import os

p = 0
print("Введите число left: ")
left = int(input())
while (left < 1) or (left > 100):
    print("Ошибка, введите число еще раз: ")
    left = int(input())
print("Введите число right: ")
right = int(input())
while (right < 1) or (right > 100):
    print("Ошибка, введите число еще раз: ")
    right = int(input())
for i in range(0, 100):
    stats = os.stat("example/file" + str(i + 1))
    size = stats.st_size / 1024
    if (size >= left) and (size <= right):
        p += 1
print(p)
