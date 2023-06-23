# import csv
#
# FILENAME = "players.csv"
# players = [
#     ["Иванов", 10, 256],
#     ["Петров", 30, 1000],
#     ["Медведев", 30, 1100],
#     ["Сидоров", 20, 300],
#     ["Уткин", 10, 256],
#     ["Васин", 5, 100]
# ]
# with open(FILENAME, "w", newline="") as file:
#     file.write("Спортсмен;Количество побед;Доп. показатель" + "\n")
#     writer = csv.writer(file, delimiter=";")
#     writer.writerows(players)
# with open(FILENAME, "r", newline="") as file:
#     str1 = file.readline()
#     reader = csv.reader(file, delimiter=';')
#     my_dict = {}
#     fam_list = []
#     for row in reader:
#         my_dict[row[0]] = [int(row[1]), int(row[2])]
#         fam_list.append(row[0])
# # сортировка пузырьком
# for i in range(0, len(fam_list)):
#     for j in range(len(fam_list) - i - 1):
#         if my_dict[fam_list[j]][0] < my_dict[fam_list[j + 1]][0] or (
#                 my_dict[fam_list[j]][0] == my_dict[fam_list[j + 1]][0] and my_dict[fam_list[j]][1] <
#                 my_dict[fam_list[j + 1]][1]):
#             fam_list[j], fam_list[j + 1] = fam_list[j + 1], fam_list[j]
# place = 1
# with open("results.csv", "w", newline="") as file:
#     file.write("Спортсмен;Место" + "\n" + fam_list[0] + ";" + str(place) + "\n")
# for i in range(1, len(fam_list)):
#     with open("results.csv", "a", newline="") as file:
#         if not (my_dict[fam_list[i]][0] == my_dict[fam_list[i - 1]][0] and my_dict[fam_list[i]][1] ==
#                 my_dict[fam_list[i - 1]][1]):
#             place += 1
#         file.write(fam_list[i] + ";" + str(place) + "\n")
