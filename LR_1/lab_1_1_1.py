print("Введите исходную строку:")
s = input()
print("Введите строку \"вирус\"")
x = input()
lower_x = x.lower()
res = s.lower().find(lower_x)
while res != -1:
    s = s[:res] + s[res + len(x):]
    res = s.lower().find(lower_x)
print(s)