with open("F1.txt", "w") as f1:
    while 1:
        user_input = input("Введите данные (пустая строка для завершения ввода): ")
        if user_input == "":
            break
        f1.write(user_input + "\n")
with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    for line in f1:
        words = line.strip().split()
        if len(words) == 1:
            f2.write(line)
with open("F2.txt", "r") as f2:
    longest_word = ""
    for line in f2:
        word = line.strip()
        if len(word) > len(longest_word):
            longest_word = word
print(f"Самое длинное слово в файле F2: {longest_word}")