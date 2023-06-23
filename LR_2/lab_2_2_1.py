print("Введите маску подсети: ")
mask = input().split(".")
with open("ip.log", "r") as file:
    with open("ip_solve.log", "w") as file2:
        flag = True
        while flag:
            str_0 = file.readline()
            if not str_0:
                flag = False
                file.close()
                break
            print(str_0, end="")
            ip = str_0.split(".")
            file2.write(str(int(mask[0]) & int(ip[0])) + "." + str(int(mask[1]) & int(ip[1])) + "." +
                        str(int(mask[2]) & int(ip[2])) + "." + str(int(mask[3]) & int(ip[3])) + "\n")
