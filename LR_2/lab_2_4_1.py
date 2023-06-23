import os
import random

os.mkdir("example")
for i in range(0, 100):
    file = open("example/file" + str(i + 1), "wb")
    file.seek(random.randint(1024, 100 * 1024))
    file.write("t".encode())
    file.close()
