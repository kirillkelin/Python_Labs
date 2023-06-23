filename = "Gogol.txt"
with open(filename, encoding="utf8") as file:
    words = file.read()
words = words.lower()
# print(len(words))
letters = {}
for i in range(ord('а'), ord('я') + 1):
    letter = chr(i)
    k = 0
    for words_letter in words:
        if words_letter == letter:
            k += 1
    frequency = k / len(words)
    frequency = float('{:.4f}'.format(frequency))
    letters[letter] = frequency
# print(letters)
value = sorted(letters.values())
sorted_value = list(reversed(value))
print(sorted_value)
result = {}
for i in range(0, len(sorted_value)):
    for key in letters:
        if letters[key] == sorted_value[i]:
            result[key] = sorted_value[i]
# print(result)
with open("article_rus_solve.txt", "w") as file:
    for key in result:
        file.write(str(key) + ":" + str(result[key]) + "\n")
