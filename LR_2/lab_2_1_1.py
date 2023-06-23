import random

with open("ip.log", "w") as file:
    for i in range(0, 10000):
        file.write(str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(
            random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "\n")
