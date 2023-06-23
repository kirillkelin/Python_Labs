import csv
import numpy as np
import pandas as pd
from operator import itemgetter
import codecs

FILENAME = "players.csv"

players = [

    {"Спортсмен": "Иванов", "Количество побед": 10, "Доп. показатель": 256},

    {"Спортсмен": "Петров", "Количество побед": 30, "Доп. показатель": 1000},

    {"Спортсмен": "Медведев", "Количество побед": 30, "Доп. показатель": 1100},

    {"Спортсмен": "Сидоров", "Количество побед": 20, "Доп. показатель": 300},

    {"Спортсмен": "Уткин", "Количество побед": 10, "Доп. показатель": 256},

    {"Спортсмен": "Васин", "Количество побед": 5, "Доп. показатель": 100},

]

with open(FILENAME, "w", newline="") as file:
    columns = ["Спортсмен", "Количество побед", "Доп. показатель"]

    writer = csv.DictWriter(file, fieldnames=columns)

    writer.writeheader()

    writer.writerows(players)

sportsmans = {}

df = pd.read_csv("players.csv", encoding='cp1251')
print(df)
sorted_df = df.sort_values(by=['Количество побед', 'Доп. показатель'], ascending=False)
sorted_df = sorted_df.reset_index(drop=True)
print(sorted_df)

mydict = {}
k = 1
m = 0
for i in range(0, len(sorted_df), 1):
    if (m > i):
        l = m
        k += 1
    else:
        l = i
    mydict[sorted_df.loc[sorted_df.index[l], 'Спортсмен']] = k
    for j in range(i + 1, len(sorted_df), 1):
        if sorted_df.loc[sorted_df.index[j], 'Количество побед'] == sorted_df.loc[
            sorted_df.index[i], 'Количество побед'] and sorted_df.loc[sorted_df.index[j], 'Доп. показатель'] == \
                sorted_df.loc[sorted_df.index[i], 'Доп. показатель']:
            mydict[sorted_df.loc[sorted_df.index[j], 'Спортсмен']] = k
            k -= 1
            m = i + 2

    k += 1
print(mydict)

with open("results.csv", "w") as file:
    for key in mydict.keys():
        file.write(key + ";" + str(mydict[key]) + "\n")
