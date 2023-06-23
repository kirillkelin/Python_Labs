from datetime import datetime


def nearest_date(dates):
    k = 0
    value_today = datetime.today().day + datetime.today().month * 30 + datetime.today().year * 30 * 12
    # print(value_today)
    save = []
    for i in dates:
        temporary = datetime.strptime(i, "%d.%m.%Y")
        value_dates = temporary.day + temporary.month * 30 + temporary.year * 30 * 12
        save.append(value_dates)
    values = []
    # print(save)
    for i in save:
        value = abs(i - value_today)
        values.append(value)
    # print(values)
    list_of_index = []
    value_min = min(values)
    for i in range(0, len(values)):
        if values[i] == value_min:
            k += 1
            list_of_index.append(i)
    if k > 1:
        for i in range(0, len(list_of_index) - 1):
            if save[i] > save[i + 1]:
                return dates[i]
            else:
                return dates[i + 1]
    else:
        return dates[values.index(value_min)]
    # print(index)


def main():
    n = 0
    while True:
        print("Введите значение n:")
        try:
            n = int(input())
        except ValueError as e:
            print("Некорректный ввод!")
        else:
            if n <= 0:
                print("Некорректный ввод!")
            else:
                break
    dates = []
    k = 0
    while True:
        try:
            for i in range(n):
                date = input("Введите дату(число, месяц, год): ").split(".")
                for j in date:
                    k = int(j)
                date1 = date[0] + "." + date[1] + "." + date[2]
                dates.append(date1)
            break
        except ValueError as e:
            print("Некорректный ввод!")
    print(nearest_date(dates))


if __name__ == "__main__":
    main()
